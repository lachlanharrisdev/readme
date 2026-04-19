<!-- 
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0 

src/routes/auth/signup/+page.svelte
-->

<script lang="ts">
	import PageHeader from '$lib/components/pageheader.svelte';
	import Bento from '$lib/components/bento.svelte';
	import Hint from '$lib/components/hint.svelte';
</script>

<main class="max-w-[1400px] mx-auto px-6 md:px-12">
	<PageHeader title="Signup" subtitle="Your reading journey starts with a generic signup screen." />

	<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
		<Bento class="lg:col-span-8 p-8 md:p-12 relative overflow-hidden">
			<span
				class="material-symbols-outlined absolute -bottom-10 -right-10 text-[200px] text-surface-container-low opacity-50 pointer-events-none select-none"
			>
				post_add
			</span>

			<form class="space-y-8 relative z-10">
				<div class="space-y-3">
					<label class="block font-label text-sm uppercase tracking-widest text-on-surface-variant font-bold" for="username">
						Username
					</label>
					<input
						id="username"
						type="text"
						placeholder="Username"
						class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-6 py-4 text-on-surface placeholder:text-outline text-lg outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
					/>
				</div>

				<div class="space-y-3">
					<label class="block font-label text-sm uppercase tracking-widest text-on-surface-variant font-bold" for="password">
						Password
					</label>
					<input
						id="password"
						type="password"
						placeholder="Password"
						class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-6 py-4 text-on-surface placeholder:text-outline text-lg outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
					/>
				</div>

				<a href="/auth/login" class="text-sm text-primary hover:underline">
					Already have an account? Login here.
				</a>

				<div class="pt-6">
					<button
						type="button"
						class="w-full md:w-auto md:px-12 bg-gradient-to-r from-primary to-primary-container text-on-primary rounded-pill py-4 text-lg font-bold flex items-center justify-center gap-3 transition-transform hover:scale-[0.99] focus:outline-none"
					>
						Signup
						<span class="material-symbols-outlined fill">chevron_right</span>
					</button>
				</div>
			</form>
		</Bento>

		<aside class="lg:col-span-4 flex flex-col gap-8">
			<Hint/>
		</aside>
	</div>
</main>
