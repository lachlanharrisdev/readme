<!-- 
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0 

src/lib/components/streakitem.svelte
-->

<script lang="ts">
	let { class: className = '', title, stat, unit, icon, bg, text } = $props<{
        class?: string;
        title?: string;
        stat?: string;
        unit?: string;
		icon?: string;
        bg?: string;
        text?: string;
	} & Record<string, unknown>>();
</script>

<div class={`flex items-center gap-5 ${className}`.trim()}>
    <div
        class="w-16 h-16 rounded-full bg-{bg || 'secondary-container/50'} flex items-center justify-center text-{text || 'primary-container'}"
    >
        <span class="material-symbols-outlined fill text-3xl">{icon || 'local_fire_department'}</span>
    </div>
    <div>
        <div class="flex items-baseline gap-1">
            <div class="text-4xl font-headline font-bold text-on-surface flex">{stat || '0'}</div>
            <div class="text-xl font-semibold flex h-full">{unit || 'days'}</div>
        </div>
        <div class="text-sm text-on-surface-variant font-medium pt-1">{title || 'Current Streak'}</div>
    </div>
</div>