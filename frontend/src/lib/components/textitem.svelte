<!-- 
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0 

src/lib/components/textitem.svelte
-->

<script lang="ts">
	let { title, due, pages, author, icon, ...rest } = $props<{
        title?: string;
        due?: string;
        pages?: string;
        author?: string;
		icon?: string;
	} & Record<string, unknown>>();
</script>

<div
    class="flex items-center gap-2 md:gap-5 p-3 md:p-4 rounded-[16px] hover:bg-surface-container-low transition-colors cursor-pointer group"
>
    <div
        class="w-12 h-12 rounded-full bg-surface-container-highest flex items-center justify-center text-on-surface group-hover:bg-surface-container-lowest transition-colors"
    >
        <span class="material-symbols-outlined">{icon || 'menu_book'}</span>
    </div>
    <div class="flex-1">
        <h4 class="text-base font-bold text-on-surface">{title || 'Unknown'}</h4>
        {#if due}
            <p class="text-sm text-on-surface-variant">{due}</p>
        {:else}
            <p class="text-sm text-on-surface-variant">{author || 'No Author'}</p>
        {/if}
    </div>
    <div class="text-sm font-medium text-on-surface-variant bg-surface px-3 py-1.5 rounded-pill">{pages || '0'} pages</div>
</div>