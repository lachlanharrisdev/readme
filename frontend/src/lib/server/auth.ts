/*
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0

src/lib/server/auth.ts
Auth helper functions for communicating with the backend
and managing auth cookies
*/

import type { Cookies } from '@sveltejs/kit';
import { redirect } from '@sveltejs/kit';

import { getBackendApiV1BaseUrl } from './backend';

// Types
// -----

// see backend/app/api/v1/models.py
export type JwtTokenResponse = {
	access_token: string;
	token_type: 'bearer' | string;
};

// see backend/app/api/v1/models.py
export type BackendUser = {
	id: number;
	username: string;
	created_at: string;
};

// Acces Tokens
// ------------

// name of the cookie for client-side retrieval
const ACCESS_TOKEN_COOKIE = 'access_token';

export function getAccessTokenFromCookies(cookies: Cookies): string | undefined {
	return cookies.get(ACCESS_TOKEN_COOKIE);
}

export function setAccessTokenCookie(cookies: Cookies, params: { token: string; url: URL }): void {
	cookies.set(ACCESS_TOKEN_COOKIE, params.token, {
		httpOnly: true,
		secure: params.url.protocol === 'https:',
		sameSite: 'lax',
		path: '/',
		maxAge: 60 * 60 * 24 * 7
	});
}

export function clearAccessTokenCookie(cookies: Cookies): void {
	cookies.delete(ACCESS_TOKEN_COOKIE, { path: '/' });
}

// Server-side auth helpers
// ------------------------

/**
 * Returns the access token cookie or redirects to login.
 * 
 * @param cookies    - the cookies object from the load function or actions context
 * @param params     - redirectTo is the url to return to after login
 * @returns the access token if it exists
 */
export function requireAccessToken(cookies: Cookies, params: { redirectTo: string }): string {
	const accessToken = getAccessTokenFromCookies(cookies);
	if (!accessToken) {
		throw redirect(303, `/auth/login?redirectTo=${encodeURIComponent(params.redirectTo)}`);
	}
	return accessToken;
}

/**
 * Calls the backend API using the JWT from cookies and parses json response
 *
 * - if no token exists, redirects to login
 * - if backend returns 401/403, clears cookie and redirects to login
 * 
 * @param fetchFn     - pass in fetch from the load function or actions context
 * @param params      - cookies, redirect url, API path, method, and body
 * @returns the parsed JSON response from the backend on success
 */
export async function backendAuthedJson<T>(
	fetchFn: typeof fetch,
	params: {
		cookies: Cookies;
		redirectTo: string;
		path: string;
		method?: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE';
		body?: unknown;
	}
): Promise<T> {
	const accessToken = requireAccessToken(params.cookies, { redirectTo: params.redirectTo });

	const res = await fetchFn(`${getBackendApiV1BaseUrl()}${params.path}`, {
		method: params.method ?? 'GET',
		headers: {
			...(params.body ? { 'content-type': 'application/json' } : {}),
			authorization: `Bearer ${accessToken}`
		},
		body: params.body ? JSON.stringify(params.body) : undefined
	});

	if (res.status === 401 || res.status === 403) {
		clearAccessTokenCookie(params.cookies);
		throw redirect(303, `/auth/login?redirectTo=${encodeURIComponent(params.redirectTo)}`);
	}

	if (!res.ok) {
		let detail = 'Request failed';
		try {
			const body = await res.json();
			if (typeof body?.detail === 'string') detail = body.detail;
			if (Array.isArray(body?.detail)) detail = 'Invalid request';
		} catch {
			// ignore
		}
		throw new Error(detail);
	}

	return (await res.json()) as T;
}

// Primary auth functions
// ----------------------

/**
 * Logs in a user with a username and password
 * 
 * @param fetchFn - pass in fetch from the load function or actions context
 * @param params  - username and password for login
 * @returns JWT token on success
 */
export async function backendLoginWithPassword(
	fetchFn: typeof fetch,
	params: { username: string; password: string }
): Promise<JwtTokenResponse> {
	const res = await fetchFn(`${getBackendApiV1BaseUrl()}/auth/token`, {
		method: 'POST',
		headers: {
			'content-type': 'application/x-www-form-urlencoded'
		},
		body: new URLSearchParams({
			username: params.username,
			password: params.password
		})
	});

	if (!res.ok) {
		let detail = 'Login failed';
		try {
			const body = await res.json();
			if (typeof body?.detail === 'string') detail = body.detail;
		} catch {
			// ignore
		}
		throw new Error(detail);
	}

	return (await res.json()) as JwtTokenResponse;
}

/**
 * Registers a user with a username and password
 * 
 * @param fetchFn - pass in fetch from the load function or actions context
 * @param params  - username and password for registration
 * @returns JWT token on success
 */
export async function backendSignup(
	fetchFn: typeof fetch,
	params: { username: string; password: string }
): Promise<BackendUser> {
	const res = await fetchFn(`${getBackendApiV1BaseUrl()}/auth/signup`, {
		method: 'POST',
		headers: {
			'content-type': 'application/json'
		},
		body: JSON.stringify({
			username: params.username,
			password: params.password
		})
	});

	if (!res.ok) {
		let detail = 'Signup failed';
		try {
			const body = await res.json();
			if (typeof body?.detail === 'string') detail = body.detail;
		} catch {
			// ignore
		}
		throw new Error(detail);
	}

	return (await res.json()) as BackendUser;
}

/**
 * Returns information about the currently authenticated user
 * 
 * @param fetchFn     - pass in fetch from the load function or actions context
 * @param accessToken - the JWT token for authentication
 * @returns user information on success
 */
export async function backendGetMe(fetchFn: typeof fetch, accessToken: string): Promise<BackendUser> {
	const res = await fetchFn(`${getBackendApiV1BaseUrl()}/auth/me`, {
		method: 'GET',
		headers: {
			authorization: `Bearer ${accessToken}`
		}
	});

	if (!res.ok) {
		let detail = 'Not authenticated';
		try {
			const body = await res.json();
			if (typeof body?.detail === 'string') detail = body.detail;
		} catch {
			// ignore
		}
		throw new Error(detail);
	}

	return (await res.json()) as BackendUser;
}
