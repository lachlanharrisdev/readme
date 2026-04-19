<!-- 
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0 

src/lib/components/pageheader.svelte
-->

<script lang="ts">
	let { title, subtitle } = $props<{ title: string; subtitle?: string }>();
</script>

<header class="mb-12">
	<h1 class="text-5xl font-extrabold tracking-tight text-on-surface mb-3">{title}</h1>
	{#if subtitle}
		<p class="text-on-surface-variant text-lg max-w-2xl">{subtitle}</p>
	{/if}
</header>
