<!-- 
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0 

src/routes/settings/+page.svelte
-->

<script lang="ts">
	import PageHeader from '$lib/components/pageheader.svelte';
	import Bento from '$lib/components/bento.svelte';
    import Streakitem from '$lib/components/streakitem.svelte';
</script>

<main class="max-w-[1400px] mx-auto px-6 md:px-12">
	<PageHeader
		title="Settings"
		subtitle="Manage your account details and reading preferences"
	/>

	<div class="grid grid-cols-1 md:grid-cols-12 gap-6">
		<Bento class="md:col-span-12 flex flex-col md:flex-row items-start md:items-center gap-8 relative overflow-hidden">
			<span
				class="material-symbols-outlined fill absolute -right-12 -bottom-12 text-[200px] text-surface-container-low opacity-50 pointer-events-none select-none"
			>
				account_circle
			</span>

			<div class="relative z-10 flex-shrink-0">
				<div
					class="w-32 h-32 rounded-full bg-secondary-container flex items-center justify-center text-primary-container text-4xl font-extrabold"
				>
					L
				</div>
				<button
					type="button"
					aria-label="Edit avatar"
					class="absolute bottom-0 right-0 w-10 h-10 rounded-full bg-primary-container text-on-primary flex items-center justify-center hover:scale-105 transition-transform hidden"
				>
					<span class="material-symbols-outlined fill text-sm">edit</span>
				</button>
			</div>

			<div class="relative z-10 flex-1">
				<h2 class="text-3xl font-headline font-bold text-on-surface tracking-tight mb-4">@lachlanharrisdev</h2>
				<div class="hidden md:flex flex-wrap gap-x-20 gap-y-4">
					<Streakitem title="Books Read" stat="0" unit="" icon="menu_book" bg="surface-container-low" text="on-surface"/>
					<Streakitem title="Current Streak" stat="0" unit="days" icon="local_fire_department"/>
				</div>
			</div>
		</Bento>

		<Bento class="md:col-span-6 relative overflow-hidden">
			<div class="flex items-center gap-3 mb-8">
				<span class="material-symbols-outlined text-on-surface-variant">manage_accounts</span>
				<h3 class="text-xl font-headline font-semibold text-on-surface tracking-tight">Account Settings</h3>
			</div>
			<div class="space-y-6">
				<div>
					<label class="block text-xs font-label uppercase tracking-wider text-on-surface-variant mb-2" for="username">
						Username
					</label>
					<input
						id="username"
						type="text"
						value="lachlanharrisdev"
						class="w-full bg-surface-container-low border-none rounded-sm px-4 py-3 text-on-surface font-body focus:ring-0 outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
					/>
				</div>

				<div>
					<label class="block text-xs font-label uppercase tracking-wider text-on-surface-variant mb-2" for="password">
						Password
					</label>
					<div class="relative">
						<input
							id="password"
							disabled
							type="password"
							value="••••••••••••"
							class="w-full bg-surface-container-low border-none rounded-sm px-4 py-3 text-on-surface font-body focus:ring-0 outline outline-2 outline-transparent outline-offset-2"
						/>
						<button
							type="button"
							class="absolute right-4 top-1/2 -translate-y-1/2 text-primary text-sm font-semibold hover:text-primary-container transition-colors"
						>
							Change
						</button>
					</div>
				</div>

				<div class="pt-4">
					<button
						type="button"
						class="w-full md:w-auto py-3 px-8 rounded-pill bg-gradient-to-r from-primary to-primary-container text-on-primary font-semibold hover:opacity-90 transition-opacity text-sm"
					>
						Save Changes
					</button>
				</div>
			</div>
		</Bento>

		<Bento class="md:col-span-6">
			<div class="flex items-center gap-3 mb-8">
				<span class="material-symbols-outlined text-on-surface-variant">tune</span>
				<h3 class="text-xl font-headline font-semibold text-on-surface tracking-tight">App Preferences</h3>
			</div>

			<div class="space-y-8">
				<div class="flex items-center justify-between p-4 bg-surface-container-low rounded-DEFAULT">
					<div class="flex items-center gap-4">
						<div class="w-10 h-10 bg-surface rounded-full flex items-center justify-center">
							<span class="material-symbols-outlined text-on-surface-variant">dark_mode</span>
						</div>
						<div>
							<h4 class="font-semibold text-on-surface font-body">Dark Mode</h4>
							<p class="text-xs text-on-surface-variant font-body">Use dark theme across the app</p>
						</div>
					</div>
					<label class="relative inline-flex items-center cursor-pointer">
						<input class="sr-only peer" type="checkbox" />
						<div
							class="w-11 h-6 bg-outline-variant/30 rounded-full peer peer-checked:bg-primary-container after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:after:translate-x-full"
						></div>
					</label>
				</div>

				<div class="flex items-center justify-between p-4 bg-surface-container-low rounded-DEFAULT">
					<div class="flex items-center gap-4">
						<div class="w-10 h-10 bg-surface rounded-full flex items-center justify-center">
							<span class="material-symbols-outlined text-on-surface-variant">notifications_active</span>
						</div>
						<div>
							<h4 class="font-semibold text-on-surface font-body">Push Notifications</h4>
							<p class="text-xs text-on-surface-variant font-body">Reading reminders and updates</p>
						</div>
					</div>
					<label class="relative inline-flex items-center cursor-pointer">
						<input class="sr-only peer" type="checkbox" checked />
						<div
							class="w-11 h-6 bg-outline-variant/30 rounded-full peer peer-checked:bg-primary-container after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:after:translate-x-full"
						></div>
					</label>
				</div>
			</div>
		</Bento>

		<Bento class="md:col-span-12 border border-error-container/50">
			<div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
				<div>
					<h3 class="text-lg font-headline font-semibold text-error tracking-tight mb-2 flex items-center gap-2">
						<span class="material-symbols-outlined fill text-error">warning</span>
						Danger Zone
					</h3>
					<p class="text-on-surface-variant font-body text-sm max-w-xl">
						Once you delete your account, there is no going back. All your reading history, streak & preferences will be
						permanently erased.
					</p>
				</div>
				<button
					type="button"
					class="whitespace-nowrap py-3 px-6 rounded-pill bg-error-container text-on-error-container font-semibold hover:bg-error hover:text-on-error transition-colors text-sm"
				>
					Delete Account
				</button>
			</div>
		</Bento>
	</div>
</main>
