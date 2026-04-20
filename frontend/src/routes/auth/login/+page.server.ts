/*
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0

src/routes/auth/login/+page.server.ts
server-side logic for the login page
*/

import { fail, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';

import { backendLoginWithPassword, setAccessTokenCookie } from '$lib/server/auth';

export const actions: Actions = {
	default: async ({ request, cookies, fetch, url }) => {
		const form = await request.formData();
		const username = String(form.get('username') ?? '').trim();
		const password = String(form.get('password') ?? '');

		if (!username || !password) {
			return fail(400, { error: 'Username and password are required.' });
		}

		try {
			const token = await backendLoginWithPassword(fetch, { username, password });
			setAccessTokenCookie(cookies, { token: token.access_token, url });

			const redirectTo = url.searchParams.get('redirectTo');
			throw redirect(303, redirectTo || '/');
		} catch (err) {
			return fail(401, {
				error: err instanceof Error ? err.message : 'Login failed.'
			});
		}
	}
};
