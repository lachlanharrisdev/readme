/*
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0

src/routes/auth/signup/+page.server.ts
server-side logic for the signup page
*/

import { fail, redirect, type Actions } from '@sveltejs/kit';

import { backendLoginWithPassword, backendSignup, setAccessTokenCookie } from '$lib/server/auth';

export const actions: Actions = {
	default: async ({ request, cookies, fetch, url }) => {
		const form = await request.formData();
		const username = String(form.get('username') ?? '').trim();
		const password = String(form.get('password') ?? '');

		if (!username || !password) {
			return fail(400, { error: 'Username and password are required.' });
		}

		try {
			await backendSignup(fetch, { username, password });
			const token = await backendLoginWithPassword(fetch, { username, password });
			setAccessTokenCookie(cookies, { token: token.access_token, url });

			const redirectTo = url.searchParams.get('redirectTo');
			throw redirect(303, redirectTo || '/');
		} catch (err) {
			return fail(400, {
				error: err instanceof Error ? err.message : 'Signup failed.'
			});
		}
	}
};
