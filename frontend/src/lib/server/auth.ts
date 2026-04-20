/*
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0

src/lib/server/auth.ts
Auth helper functions for communicating with the backend
and managing auth cookies
*/

import type { Cookies } from '@sveltejs/kit';

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
