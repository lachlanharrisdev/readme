<!-- 
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0 

src/lib/components/navbar.svelte
-->

<script lang="ts">
	import { page } from '$app/state';

	type NavItem = {
		href: string;
		label: string;
	};

	const navItems: NavItem[] = [
		{ href: '/', label: 'Dashboard' },
		{ href: '/schedule', label: 'Schedule' },
		{ href: '/add-text', label: 'Add Text' },
		{ href: '/settings', label: 'Settings' }
	];

	const isActive = (href: string) => {
		if (href === '/') return page.url.pathname === '/';
		return page.url.pathname.startsWith(href);
	};
</script>

<nav
	class="fixed top-0 left-0 w-full z-50 flex items-center justify-between px-6 md:px-8 py-4 bg-surface/80 backdrop-blur-xl"
>
	<div class="flex items-center gap-4">
		<a href="/" class="text-xl font-extrabold tracking-tighter text-on-surface">ReadMe</a>
	</div>

	<div class="flex-1 flex justify-center">
		<div class="flex items-center gap-2 sm:gap-1 text-sm tracking-tight">
			{#each navItems as item (item.href)}
				<a
					href={item.href}
					data-sveltekit-preload-data="hover"
					class={isActive(item.href)
						? 'bg-primary-container text-on-primary rounded-pill px-3 md:px-6 py-3 font-semibold transition-transform'
						: 'text-on-surface-variant hover:text-on-surface px-3 md:px-6 py-3 hover:bg-surface-container-low rounded-pill transition-colors duration-200'}
				>
					<span class="whitespace-nowrap">{item.label}</span>
				</a>
			{/each}
		</div>
	</div>

	<div class="flex items-center gap-3">
		<a
			href="/settings"
			aria-label="Profile"
			class="w-10 h-10 rounded-full bg-surface-container-low flex items-center justify-center text-on-surface-variant hover:bg-surface-container-high transition-colors"
		>
			<span class="material-symbols-outlined">person</span>
		</a>
	</div>
</nav>
