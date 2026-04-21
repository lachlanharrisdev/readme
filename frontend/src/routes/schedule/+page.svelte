<!-- 
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0 

src/routes/schedule/+page.svelte
-->

<script lang="ts">
	import PageHeader from '$lib/components/pageheader.svelte';
	import Bento from '$lib/components/bento.svelte';
	import Textitem from '$lib/components/textitem.svelte';

	let { data, form } = $props();

	const getMinutes = (availability: Record<string, number> | undefined, day: number): number => {
		if (!availability) return 0;
		const v = availability[String(day)];
		return typeof v === 'number' && Number.isFinite(v) ? v : 0;
	};

	const availability = $derived(
		((form as any)?.schedule?.availability as Record<string, number> | undefined) ||
			((data as any)?.schedule?.availability as Record<string, number> | undefined)
	);
</script>

<main class="max-w-[1400px] mx-auto px-6 md:px-12">
	<PageHeader title="Schedule" subtitle="Track your reading path over the next two weeks" />

	<section class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-10">
		<Bento class="relative overflow-hidden flex flex-col justify-between min-h-[260px]">
			<span
				class="material-symbols-outlined fill absolute -bottom-8 -right-8 text-9xl text-surface-container-high opacity-40 select-none pointer-events-none"
			>
				calendar_view_week
			</span>
			<div class="relative z-10">
				<h2 class="text-xl font-bold tracking-tight text-on-surface mb-1">Weekly Load</h2>
				<p class="text-on-surface-variant text-sm font-medium">April 19 — April 26</p>
			</div>
			<div class="relative z-10 mt-8">
				<div class="flex items-baseline gap-2">
					<span
						class="text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-primary to-primary-container"
					>
						0
					</span>
					<span class="text-on-surface-variant font-semibold tracking-wide">pages</span>
				</div>
				<div class="w-full bg-surface-container-low rounded-pill h-2.5 mt-5 overflow-hidden">
					<div class="bg-gradient-to-r from-primary to-primary-container h-full rounded-pill w-[0%]"></div>
				</div>
				<p class="text-xs text-on-surface-variant mt-3 tracking-widest uppercase font-bold">
					0 / 9293822332 completed
				</p>
			</div>
		</Bento>

		<Bento class="flex flex-col justify-between lg:col-span-2">
			<div class="flex items-start justify-between gap-8">
				<div>
					<h3 class="text-xl font-bold tracking-tight text-on-surface mb-3">Pace Analysis</h3>
					<p class="text-on-surface-variant text-base max-w-lg leading-relaxed">
						You're laziness is through the roof! At this rate, you'll finish <strong class="text-on-surface">Blood Meridian</strong> in the year 2194. Try picking up the pace to hit your target date of April 24.
                    </p>
				</div>
				<div class="w-16 h-16 rounded-full bg-secondary-container flex items-center justify-center flex-shrink-0">
					<span class="material-symbols-outlined text-primary text-3xl">trending_up</span>
				</div>
			</div>
		</Bento>
	</section>

	<section>
		<div class="flex overflow-x-auto space-x-6 pb-12 snap-x snap-mandatory">
			<div
				class="snap-start flex-shrink-0 w-[400px] max-w-[90vw] bg-surface-container-lowest rounded-bento p-7 relative"
			>

				<div class="mb-8 flex justify-between items-start">
					<div>
						<span class="block text-xs font-bold text-on-surface-variant uppercase tracking-widest mb-1">Wed</span>
						<span class="block text-4xl font-extrabold text-on-surface">24</span>
					</div>
					<div class="bg-secondary-container text-primary-container px-4 py-1.5 rounded-pill text-sm font-bold">
						Today
					</div>
				</div>

				<div class="space-y-4">
					<Textitem title="Blood Meridian" pages="50" author="Cormac McCarthy"/>
				</div>
			</div>

			<div
				class="snap-start flex-shrink-0 w-[400px] max-w-[90vw] bg-surface-container-lowest rounded-bento p-7 opacity-90 hover:opacity-100 transition-opacity"
			>
				<div class="mb-8 flex justify-between items-start">
					<div>
						<span class="block text-xs font-bold text-on-surface-variant uppercase tracking-widest mb-1">Thu</span>
						<span class="block text-4xl font-extrabold text-on-surface">25</span>
					</div>
				</div>
				<div class="space-y-4">
					<Textitem title="Orbital" pages="50" author="Samantha Harvey"/>
				</div>
			</div>

			<div
				class="snap-start flex-shrink-0 w-[400px] max-w-[90vw] bg-surface-container-lowest rounded-bento p-7 opacity-90 hover:opacity-100 transition-opacity"
			>
				<div class="mb-8 flex justify-between items-start">
					<div>
						<span class="block text-xs font-bold text-on-surface-variant uppercase tracking-widest mb-1">Fri</span>
						<span class="block text-4xl font-extrabold text-on-surface">26</span>
					</div>
				</div>
				<div class="space-y-4">
					<Textitem title="Eng Ext 1 BM Article" pages="20" icon="contract" />
				</div>
			</div>

			<div class="snap-start flex-shrink-0 w-4"></div>
		</div>
	</section>

	<section class="mb-10">
		<Bento>
			<h3 class="text-xl font-bold tracking-tight text-on-surface mb-6">Set Your Weekly Schedule</h3>
			<form method="POST" class="space-y-6">
				{#if form?.error}
					<div class="rounded-DEFAULT bg-error-container text-on-error-container px-5 py-4 font-semibold text-sm">
						{form.error}
					</div>
				{/if}
				{#if form?.success}
					<div class="rounded-DEFAULT bg-secondary-container text-on-secondary-container px-5 py-4 font-semibold text-sm">
						Schedule updated.
					</div>
				{/if}
				<div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-3">
					<div class="flex flex-col gap-1.5">
						<label class="block text-xs uppercase tracking-widest text-on-surface-variant font-bold" for="sunday">
							Sun
						</label>
						<input
							id="sunday"
							name="0"
							type="number"
							placeholder="0"
							min="0"
							max="1440"
							value={getMinutes(availability, 0)}
							class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-3 py-2 text-on-surface placeholder:text-outline text-sm outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
						/>
					</div>
					<div class="flex flex-col gap-1.5">
						<label class="block text-xs uppercase tracking-widest text-on-surface-variant font-bold" for="monday">
							Mon
						</label>
						<input
							id="monday"
							name="1"
							type="number"
							placeholder="0"
							min="0"
							max="1440"
							value={getMinutes(availability, 1)}
							class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-3 py-2 text-on-surface placeholder:text-outline text-sm outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
						/>
					</div>
					<div class="flex flex-col gap-1.5">
						<label class="block text-xs uppercase tracking-widest text-on-surface-variant font-bold" for="tuesday">
							Tue
						</label>
						<input
							id="tuesday"
							name="2"
							type="number"
							placeholder="0"
							min="0"
							max="1440"
							value={getMinutes(availability, 2)}
							class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-3 py-2 text-on-surface placeholder:text-outline text-sm outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
						/>
					</div>
					<div class="flex flex-col gap-1.5">
						<label class="block text-xs uppercase tracking-widest text-on-surface-variant font-bold" for="wednesday">
							Wed
						</label>
						<input
							id="wednesday"
							name="3"
							type="number"
							placeholder="0"
							min="0"
							max="1440"
							value={getMinutes(availability, 3)}
							class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-3 py-2 text-on-surface placeholder:text-outline text-sm outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
						/>
					</div>
					<div class="flex flex-col gap-1.5">
						<label class="block text-xs uppercase tracking-widest text-on-surface-variant font-bold" for="thursday">
							Thu
						</label>
						<input
							id="thursday"
							name="4"
							type="number"
							placeholder="0"
							min="0"
							max="1440"
							value={getMinutes(availability, 4)}
							class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-3 py-2 text-on-surface placeholder:text-outline text-sm outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
						/>
					</div>
					<div class="flex flex-col gap-1.5">
						<label class="block text-xs uppercase tracking-widest text-on-surface-variant font-bold" for="friday">
							Fri
						</label>
						<input
							id="friday"
							name="5"
							type="number"
							placeholder="0"
							min="0"
							max="1440"
							value={getMinutes(availability, 5)}
							class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-3 py-2 text-on-surface placeholder:text-outline text-sm outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
						/>
					</div>
					<div class="flex flex-col gap-1.5">
						<label class="block text-xs uppercase tracking-widest text-on-surface-variant font-bold" for="saturday">
							Sat
						</label>
						<input
							id="saturday"
							name="6"
							type="number"
							placeholder="0"
							min="0"
							max="1440"
							value={getMinutes(availability, 6)}
							class="w-full bg-surface-container-low border-none focus:ring-0 rounded-DEFAULT px-3 py-2 text-on-surface placeholder:text-outline text-sm outline outline-2 outline-transparent focus:outline-primary/30 outline-offset-2"
						/>
					</div>
				</div>
				<p class="text-xs text-on-surface-variant font-medium tracking-wide">minutes per day</p>
				<div class="pt-2">
					<button
						type="submit"
						class="w-full md:w-auto md:px-12 bg-gradient-to-r from-primary to-primary-container text-on-primary rounded-pill py-3 text-base font-bold flex items-center justify-center gap-3 transition-transform hover:scale-[0.99] focus:outline-none"
					>
						<span class="material-symbols-outlined fill text-lg">update</span>
						Update Schedule
					</button>
				</div>
			</form>
		</Bento>
	</section>
</main>
