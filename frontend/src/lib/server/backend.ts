/*
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0

src/lib/server/backend.ts
Backend utility functions
*/

import { env } from '$env/dynamic/private';

// redundancy function; should be set by docker env variables for prod
// or the local .env file for dev
export function getBackendUrl(): string {
	return env.BACKEND_URL ?? 'http://localhost:8000';
}

export function getBackendApiV1BaseUrl(): string {
	return `${getBackendUrl()}/api/v1`;
}
