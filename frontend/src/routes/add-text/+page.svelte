<!-- 
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0 

src/routes/add-text/+page.svelte
-->

<script lang="ts">
	import PageHeader from '$lib/components/pageheader.svelte';
	import Bento from '$lib/components/bento.svelte';
	import Hint from '$lib/components/hint.svelte';

	let { form } = $props();
	let is_mandatory = $state('false');
	let material_type = $state('book');
</script>

<main class="max-w-[1400px] mx-auto px-6 md:px-12">
	<PageHeader title="Add Text" subtitle="Define the parameters of your next reading commitment." />

	<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
		<Bento class="lg:col-span-8 relative overflow-hidden">
			<span
				class="material-symbols-outlined absolute -bottom-10 -right-10 text-[200px] text-surface-container-low opacity-50 pointer-events-none select-none"
			>
				post_add
			</span>

			<form method="POST" class="space-y-8 relative z-10">
				{#if form?.error}
					<div class="rounded-DEFAULT bg-error-container text-on-error-container px-5 py-4 font-semibold text-sm">
						{form.error}
					</div>
				{/if}

				{#if form?.success}
					<div class="rounded-DEFAULT bg-tertiary-container text-on-tertiary-container px-5 py-4 font-semibold text-sm">
						Text added successfully
					</div>
				{/if}

                <div class="space-y-3">
                    <label class="block font-label text-sm uppercase tracking-widest text-on-surface-variant font-bold" for="title">
                        Title
                    </label>
                    <input
                        id="title"
                        name="title"
                        type="text"
                        placeholder="The Hungry Caterpillar"
                        required
                        class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-6 py-4 text-on-surface placeholder:text-outline text-lg outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
                    />
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    
                    <div class="space-y-3">
						<label class="block font-label text-sm uppercase tracking-widest text-on-surface-variant font-bold" for="author">
                            Author <span class="text-xs font-normal text-on-surface-variant">(optional)</span>
                        </label>
                        <input
                            id="author"
                            name="author"
                            type="text"
                            placeholder="Eric Carle"
                            class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-6 py-4 text-on-surface placeholder:text-outline text-lg outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
                        />
                    </div>

                    <!-- boolean for whether it's for leisure or for study-->

                    <fieldset class="space-y-3">
                        <legend class="block font-label text-sm uppercase tracking-widest text-on-surface-variant font-bold">
                            Reading for...
                        </legend>
                        <div class="grid grid-cols-2 gap-4">
                            <label class="cursor-pointer">
                                <input 
                                    class="sr-only" 
                                    name="is_mandatory" 
                                    type="radio" 
                                    value="false"
                                    bind:group={is_mandatory}
                                />
                                <div class="rounded-DEFAULT py-2 px-2 flex flex-col items-center gap-2 transition-colors" class:bg-secondary-container={is_mandatory === 'false'} class:text-on-secondary-container={is_mandatory === 'false'} class:bg-surface-container-low={is_mandatory === 'true'} class:text-on-surface-variant={is_mandatory === 'true'} class:hover:bg-surface-container-high={is_mandatory === 'true'}>
                                    <span class="material-symbols-outlined fill text-2xl">book</span>
                                    <span class="font-semibold text-sm -mt-2">Leisure</span>
                                </div>
                            </label>
                            <label class="cursor-pointer">
                                <input 
                                    class="sr-only" 
                                    name="is_mandatory" 
                                    type="radio" 
                                    value="true"
                                    bind:group={is_mandatory}
                                />
                                <div
                                    class="rounded-DEFAULT py-2 px-2 flex flex-col items-center gap-2 transition-colors" class:bg-secondary-container={is_mandatory === 'true'} class:text-on-secondary-container={is_mandatory === 'true'} class:bg-surface-container-low={is_mandatory === 'false'} class:text-on-surface-variant={is_mandatory === 'false'} class:hover:bg-surface-container-high={is_mandatory === 'false'}
                                >
                                    <span class="material-symbols-outlined text-2xl">school</span>
                                    <span class="font-medium text-sm -mt-2">Study</span>
                                </div>
                            </label>
                        </div>
                    </fieldset>
                </div>

				<fieldset class="space-y-3">
					<legend class="block font-label text-sm uppercase tracking-widest text-on-surface-variant font-bold">
						Material Type
					</legend>
					<div class="grid grid-cols-3 gap-4">
						<label class="cursor-pointer">
							<input class="sr-only" name="material_type" type="radio" value="book" bind:group={material_type} />
							<div class="rounded-DEFAULT py-4 px-2 flex flex-col items-center gap-2 transition-colors" class:bg-secondary-container={material_type === 'book'} class:text-on-secondary-container={material_type === 'book'} class:bg-surface-container-low={material_type !== 'book'} class:text-on-surface-variant={material_type !== 'book'} class:hover:bg-surface-container-high={material_type !== 'book'}>
								<span class="material-symbols-outlined fill text-2xl">book</span>
								<span class="font-semibold text-sm">Book</span>
							</div>
						</label>
						<label class="cursor-pointer">
							<input class="sr-only" name="material_type" type="radio" value="article" bind:group={material_type} />
							<div
								class="rounded-DEFAULT py-4 px-2 flex flex-col items-center gap-2 transition-colors" class:bg-secondary-container={material_type === 'article'} class:text-on-secondary-container={material_type === 'article'} class:bg-surface-container-low={material_type !== 'article'} class:text-on-surface-variant={material_type !== 'article'} class:hover:bg-surface-container-high={material_type !== 'article'}
							>
								<span class="material-symbols-outlined text-2xl">article</span>
								<span class="font-medium text-sm">Article</span>
							</div>
						</label>
						<label class="cursor-pointer">
							<input class="sr-only" name="material_type" type="radio" value="paper" bind:group={material_type} />
							<div
								class="rounded-DEFAULT py-4 px-2 flex flex-col items-center gap-2 transition-colors" class:bg-secondary-container={material_type === 'paper'} class:text-on-secondary-container={material_type === 'paper'} class:bg-surface-container-low={material_type !== 'paper'} class:text-on-surface-variant={material_type !== 'paper'} class:hover:bg-surface-container-high={material_type !== 'paper'}
							>
								<span class="material-symbols-outlined text-2xl">description</span>
								<span class="font-medium text-sm">Paper</span>
							</div>
						</label>
					</div>
				</fieldset>

				<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
					<div class="space-y-3">
						<label class="block font-label text-sm uppercase tracking-widest text-on-surface-variant font-bold" for="pages">
							Total Pages
						</label>
						<input
							id="pages"
							name="pages"
							type="number"
							min="0"
							placeholder="0"
							class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-6 py-4 text-on-surface placeholder:text-outline text-lg outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
						/>
					</div>
					<div class="space-y-3">
						<label class="block font-label text-sm uppercase tracking-widest text-on-surface-variant font-bold" for="date">
							Target Completion
						</label>
						<input
							id="date"
							name="date"
							type="date"
							class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-6 py-4 text-on-surface text-lg outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
						/>
					</div>
				</div>

				<div class="pt-6">
					<button
						type="submit"
						class="w-full md:w-auto md:px-12 bg-gradient-to-r from-primary to-primary-container text-on-primary rounded-pill py-4 text-lg font-bold flex items-center justify-center gap-3 transition-transform hover:scale-[0.99] focus:outline-none disabled:opacity-75 disabled:cursor-not-allowed"
					>
						<span class="material-symbols-outlined fill">bookmark_add</span>
						Add to List
					</button>
				</div>
			</form>
		</Bento>

		<aside class="lg:col-span-4 flex flex-col gap-8">
			<Hint/>
		</aside>
	</div>
</main>
