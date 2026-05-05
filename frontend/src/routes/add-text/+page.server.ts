/*
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0

src/routes/add-text/+page.server.ts
server-side logic for the add text page
*/

import { fail, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';

import { backendAuthedJson } from '$lib/server/auth';

interface TextFormData {
    title: string;
    author?: string;
    type: 'book' | 'article' | 'paper' | 'other';
    total_pages?: number;
    is_mandatory: boolean;
    priority?: number;
    due_date?: string;
}

export const actions: Actions = {
    default: async ({ request, cookies, fetch }) => {
        const form = await request.formData();

        const title = String(form.get('title') ?? '').trim();
        const author = String(form.get('author') ?? '').trim() || undefined;
        const material_type = String(form.get('material_type') ?? 'book');
        const is_mandatory = form.get('is_mandatory') === 'true';
        const total_pages = form.get('pages') ? Number(form.get('pages')) : undefined;
        const due_date = form.get('date') ? String(form.get('date')) : undefined;

        if (!title) {
            return fail(400, { error: 'Title is required' });
        }

        const textData: TextFormData = {
            title,
            author,
            type: (material_type as 'book' | 'article' | 'paper' | 'other') || 'book',
            total_pages: total_pages && total_pages > 0 ? total_pages : undefined,
            is_mandatory,
            priority: is_mandatory ? 0 : 1,
            due_date
        };

        try {
            await backendAuthedJson(fetch, {
                cookies,
                path: '/texts/new',
                method: 'POST',
                body: textData,
                redirectTo: ''
            });
            return { success: true };
        } catch (err) {
            const message = err instanceof Error ? err.message : 'Failed to add text.';
            return fail(400, { error: message });
        }
    }
};
