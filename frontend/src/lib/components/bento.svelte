<!-- 
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0 

src/lib/components/bento.svelte
-->

<script lang="ts">
	let { class: className = '', style, children, ...rest } = $props<{
		class?: string;
		style?: string;
		children?: () => unknown;
	} & Record<string, unknown>>();
</script>

<div {...rest} class={`bg-surface-container-lowest rounded-bento p-6 md:p-10 ${className}`.trim()} {style}>
	{@render children?.()}
</div>
