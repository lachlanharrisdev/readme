<!-- 
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0 

src/routes/+page.svelte
-->

<script lang="ts">
	import PageHeader from '$lib/components/pageheader.svelte';
	import Bento from '$lib/components/bento.svelte';
    import Textitem from '$lib/components/textitem.svelte';
</script>

<main class="max-w-[1400px] mx-auto px-6 md:px-12">
	<PageHeader title="Good morning" subtitle="Something motivational would go here but I can't be bothered" />

	<div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
		<Bento class="lg:col-span-2 relative overflow-hidden flex flex-col justify-between min-h-[360px]">
			<div class="absolute right-0 hidden sm:block opacity-[0.03] text-on-surface pointer-events-none md:block ">
				<span class="material-symbols-outlined" style="font-size: 240px">menu_book</span>
			</div>

			<div class="relative z-10">
				<h2 class="text-3xl lg:text-4xl font-headline font-bold text-on-surface tracking-tight mb-2">
					Blood Meridian
				</h2>
				<p class="text-lg text-on-surface-variant mb-8">by Cormac McCarthy</p>

				<div class="max-w-md sm:max-w-xs md:max-w-sm lg:max-w-xs xl:max-w-md">
					<div class="flex justify-between text-sm font-semibold text-on-surface-variant mb-3">
						<span>Progress</span>
						<span>0%</span>
					</div>
					<div class="h-2 w-full bg-surface-container-low rounded-pill overflow-hidden">
						<div class="h-full bg-primary-container rounded-pill w-[0%]"></div>
					</div>
				</div>

                <p class="text-lg text-on-surface-variant mt-4 max-w-lg">Todays target is <span class="font-bold">0</span> pages (0%)</p>
			</div>

			<div class="relative z-10 mt-12 flex items-center gap-4">
				<button
					type="button"
					class="bg-gradient-to-r from-primary to-primary-container text-on-primary px-8 py-4 rounded-pill font-semibold text-base flex items-center gap-3 transition-transform hover:scale-[0.99]"
				>
					<span class="material-symbols-outlined fill">play_arrow</span>
					Continue Reading
				</button>
				<button
					type="button"
					aria-label="More"
					class="w-14 h-14 rounded-full bg-surface-container-low flex items-center justify-center text-on-surface hover:bg-surface-container-highest transition-colors"
				>
					<span class="material-symbols-outlined">more_horiz</span>
				</button>
			</div>
		</Bento>

		<Bento class="flex flex-col min-h-[360px]">
			<h3 class="text-xl font-headline font-semibold text-on-surface tracking-tight mb-10">Reading Stats</h3>
			<div class="space-y-10">
				<div class="flex items-center gap-5">
					<div
						class="w-16 h-16 rounded-full bg-secondary-container/50 flex items-center justify-center text-primary-container"
					>
						<span class="material-symbols-outlined fill text-3xl">local_fire_department</span>
					</div>
					<div>
						<div class="text-4xl font-headline font-bold text-on-surface">0 Days</div>
						<div class="text-sm text-on-surface-variant font-medium">Current Streak</div>
					</div>
				</div>
				<div class="flex items-center gap-5">
					<div class="w-16 h-16 rounded-full bg-surface-container-low flex items-center justify-center text-on-surface">
						<span class="material-symbols-outlined text-3xl">auto_stories</span>
					</div>
					<div>
						<div class="text-4xl font-headline font-bold text-on-surface">0</div>
						<div class="text-sm text-on-surface-variant font-medium">Pages this week</div>
					</div>
				</div>
			</div>
		</Bento>

		<Bento class="lg:col-span-2">
			<div class="flex items-center justify-between mb-8">
				<h3 class="text-xl font-headline font-semibold text-on-surface tracking-tight">Upcoming</h3>
				<button type="button" class="text-primary-container text-sm font-semibold hover:text-primary transition-colors">
					Manage Schedule
				</button>
			</div>

			<div class="flex flex-col gap-2">
				<Textitem title="Orbital" due="Tomorrow" pages="50" />
				<Textitem title="Eng Ext 1 BM Article 1" due="In 2 days" pages="20" icon="contract" />
			</div>
		</Bento>

		<a
			href="/add-text"
			class="block"
			data-sveltekit-preload-data="hover"
		>
			<Bento class="flex flex-col justify-center items-center text-center cursor-pointer hover:bg-surface-container-low transition-colors group">
				<div
					class="w-16 h-16 rounded-full bg-surface-container-highest flex items-center justify-center text-on-surface mb-6 group-hover:scale-110 transition-transform duration-300"
				>
					<span class="material-symbols-outlined text-3xl">add</span>
				</div>
				<h3 class="text-lg font-headline font-bold text-on-surface tracking-tight mb-2">Quick Add</h3>
				<p class="text-sm text-on-surface-variant max-w-[200px]">
					Add a new text to track
				</p>
			</Bento>
		</a>
	</div>
</main>
