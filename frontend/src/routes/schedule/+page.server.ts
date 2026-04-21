/*
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0

src/routes/schedule/+page.server.ts
server-side logic for the schedule page
*/

import { fail } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';

import { backendAuthedJson } from '$lib/server/auth';

type ScheduleForm = {
	availability: Record<string, number>;
};

function clampMinutes(value: number): number {
	if (!Number.isFinite(value)) return 0;
	return Math.min(1440, Math.max(0, value));
}

/**
 * reads a "minutes" field from the form. names are the weekday numbers 0-6
 * empty/invalid values become 0; clamped to 0..1440.
 */
function minutesFromForm(form: FormData, dayKey: string): number {
	const raw = String(form.get(dayKey) ?? '').trim();
	if (!raw) return 0;
	const parsed = Number.parseInt(raw, 10);
	return clampMinutes(Number.isNaN(parsed) ? 0 : parsed);
}

export const load: PageServerLoad = async ({ cookies, fetch }) => {
	const schedule = await backendAuthedJson<ScheduleForm>(fetch, {
		cookies,
		redirectTo: '/schedule',
		path: '/scheduling/schedule'
	});
	return { schedule };
};

export const actions: Actions = {
	default: async ({ request, cookies, fetch }) => {
		const form = await request.formData();
		const availability: Record<string, number> = Object.fromEntries(
			Array.from({ length: 7 }, (_, day) => [String(day), minutesFromForm(form, String(day))])
		);

		try {
			const schedule = await backendAuthedJson<ScheduleForm>(fetch, {
				cookies,
				redirectTo: '/schedule',
				path: '/scheduling/schedule',
				method: 'POST',
				body: { availability }
			});
			return { success: true, schedule };
		} catch (err) {
			const message = err instanceof Error ? err.message : 'Failed to update schedule.';
			return fail(400, { error: message });
		}
	}
};
