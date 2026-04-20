/*
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0

src/routes/settings/+page.server.ts
server-side logic for the settings page
*/

import { redirect } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';

import {
	backendGetMe,
	clearAccessTokenCookie,
	getAccessTokenFromCookies
} from '$lib/server/auth';

export const load: PageServerLoad = async ({ cookies, fetch }) => {
	const accessToken = getAccessTokenFromCookies(cookies);
	if (!accessToken) {
		throw redirect(303, '/auth/login');
	}

	try {
		const user = await backendGetMe(fetch, accessToken);
		return { user };
	} catch {
		clearAccessTokenCookie(cookies);
		throw redirect(303, '/auth/login');
	}
};

export const actions: Actions = {
	logout: async ({ cookies }) => {
		clearAccessTokenCookie(cookies);
		throw redirect(303, '/auth/login');
	}
};
