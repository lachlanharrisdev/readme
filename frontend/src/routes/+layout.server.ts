/*
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0

src/routes/+layout.server.ts
server-side logic shared between pages
acts as a middleware
*/

import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';

import { getAccessTokenFromCookies } from '$lib/server/auth';

function isAuthRoute(pathname: string): boolean {
	return pathname === '/auth' || pathname.startsWith('/auth/');
}

export const load: LayoutServerLoad = async ({ url, cookies }) => {
	const accessToken = getAccessTokenFromCookies(cookies);
	const isAuthed = Boolean(accessToken);

	if (!isAuthed && !isAuthRoute(url.pathname)) {
		const redirectTo = `${url.pathname}${url.search}`;
		throw redirect(303, `/auth/login?redirectTo=${encodeURIComponent(redirectTo)}`);
	}

	if (isAuthed && isAuthRoute(url.pathname)) {
		throw redirect(303, url.searchParams.get('redirectTo') || '/');
	}

	return {};
};

