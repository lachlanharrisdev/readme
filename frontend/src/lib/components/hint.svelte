<!-- 
Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
This project is licensed under Apache 2.0 

src/lib/components/hint.svelte
-->

<script lang="ts">
    import Bento from '$lib/components/bento.svelte';
    import { onMount } from 'svelte';

    const messages = [
        {
            title: 'Reading compounds like interest',
            body: [
                'Reading isn\'t just about finishing a book-it\'s about stacking tiny insights over time. One idea might not change much, but hundreds of small ideas start shaping how you think, solve problems, and understand the world.',
                'Even 10-15 minutes a day adds up fast. Over a year, that\'s multiple books\' worth of knowledge, vocabulary, and perspective-without ever feeling overwhelming.',
                'If you\'re consistent, reading quietly becomes one of the highest ROI habits you can build.'
            ],
            info: 'Reading just 10 minutes a day can expose you to hundreds of thousands of words per year.'
        },
        {
            title: 'You don\'t have to finish every book',
            body: [
                'One of the biggest mistakes people make is treating books like obligations. If a book isn\'t engaging, useful, or relevant right now, it\'s okay to stop.',
                'Your time matters more than your completion rate. Dropping a book you don\'t enjoy frees you to find one that actually pulls you in.',
                'Good readers aren\'t the ones who finish everything-they\'re the ones who choose well and read intentionally.'
            ],
        },
        {
            title: 'Match the book to your energy',
            body: [
                'Not all reading sessions are equal. Sometimes you\'re focused and ready for something dense; other times you just want something light and easy.',
                'Have different “types” of reading ready-one challenging, one casual, one purely fun. This makes it much easier to stay consistent without burning out.',
                'Reading shouldn\'t always feel like work. If it does, you\'re probably reading the wrong thing at the wrong time.'
            ]
        },
        {
            title: 'Reading is a skill, not just a habit',
            body: [
                'The more you read, the better you get at it. You\'ll notice faster comprehension, better retention, and a stronger ability to connect ideas across topics.',
                'At first, it might feel slow or effortful-but that\'s normal. Like any skill, it compounds with practice.',
                'Stick with it, and eventually reading becomes something you do effortlessly rather than something you push yourself to start.'
            ],
            info: 'Frequent readers often develop stronger comprehension and critical thinking skills over time.'
        },
        {
            title: 'Your environment matters more than motivation',
            body: [
                'Relying on motivation is unreliable. Instead, make reading the default option by shaping your environment.',
                'Keep a book within reach, reduce distractions, and make it easier to start reading than to scroll on your phone.',
                'When the friction is low, consistency becomes almost automatic.'
            ]
        },
        {
            title: 'You\'re allowed to read for fun',
            body: [
                'Not every book needs to be educational, deep, or “productive.” Reading for enjoyment is just as valuable.',
                'Stories, fiction, and even “easy” books still build vocabulary, imagination, and focus.',
                'If you enjoy what you\'re reading, you\'ll naturally read more-and that\'s what actually matters.'
            ]
        },
        {
            title: 'Small sessions beat big bursts',
            body: [
                'Reading for 10 minutes every day is far more effective than reading for 2 hours once a week.',
                'Short, consistent sessions keep ideas fresh and reduce the mental effort needed to restart.',
                'Think of reading like training-frequency matters more than intensity.'
            ],
            info: 'Consistency is one of the strongest predictors of habit formation.'
        },
        {
            title: 'Rereading is underrated',
            body: [
                'Going back to a book you\'ve already read can be surprisingly valuable. You\'ll notice ideas you missed the first time.',
                'As you change, your interpretation changes too-meaning the same book can teach you something new at different points in your life.',
                'Not every book is worth rereading, but the right ones are worth it.'
            ]
        },
        {
            title: 'Skimming is a valid strategy',
            body: [
                'You don\'t need to read every word of every book. Sometimes it\'s better to skim for key ideas and move on.',
                'This is especially useful for non-fiction where the main value is in a few core concepts.',
                'Reading efficiently doesn\'t mean rushing-it means focusing on what actually matters.'
            ]
        },
        {
            title: 'Books are conversations across time',
            body: [
                'When you read, you\'re effectively having a conversation with someone-sometimes from decades or even centuries ago.',
                'You get access to their experiences, ideas, and mistakes without having to live through them yourself.',
                'That\'s a pretty unfair advantage if you think about it.'
            ],
            info: 'Many influential ideas in science, philosophy, and technology are preserved and shared through books.'
        },
        {
            title: 'It\'s okay to read multiple books at once',
            body: [
                'You don\'t have to stick to one book at a time. Having multiple books lets you switch based on your mood or energy.',
                'This can actually increase your total reading time, since you\'re less likely to get stuck or bored.',
                'Just don\'t overload yourself-2-3 books is usually a good balance.'
            ]
        },
        {
            title: 'Reading builds focus in a distracted world',
            body: [
                'Modern apps are designed to fragment your attention. Reading does the opposite-it trains you to focus deeply for extended periods.',
                'This ability carries over into studying, problem-solving, and even coding or creative work.',
                'In a world full of distractions, focus is becoming a rare and valuable skill.'
            ],
            info: 'Deep focus is increasingly linked to productivity and learning efficiency.'
        },
        {
            title: 'You don\'t need the “perfect” system',
            body: [
                'It\'s easy to overthink reading-tracking systems, note-taking methods, schedules, and goals.',
                'Those can help, but they\'re optional. The most important thing is simply reading regularly.',
                'A simple system you actually use beats a perfect system you don\'t.'
            ]
        },
        {
            title: 'Curiosity is your best guide',
            body: [
                'If something sparks your interest, follow it. Read more about it, explore related topics, and let your curiosity lead.',
                'This makes reading feel natural instead of forced, and helps you build deeper understanding over time.',
                'The best reading paths aren\'t always linear-they\'re driven by what genuinely interests you.'
            ]
        },
        {
            title: 'Stopping is easier if starting is easy',
            body: [
                'One trick to building a reading habit is making it ridiculously easy to start.',
                'Tell yourself you\'ll read just one page. Most of the time, you\'ll keep going anyway.',
                'The hardest part is starting-once you\'re in, momentum does the rest.'
            ]
        }
    ];

    let currentMessage = $state(messages[0]);

    onMount(() => {
        currentMessage = messages[Math.floor(Math.random() * messages.length)];
    });
</script>

<Bento class="h-full flex flex-col relative overflow-hidden">
    <div class="w-14 h-14 rounded-full bg-secondary-container flex items-center justify-center mb-6">
        <span class="material-symbols-outlined text-on-secondary-container text-2xl">wb_incandescent</span>
    </div>
    <h2 class="font-headline text-2xl font-bold text-on-surface tracking-tight mb-4">{currentMessage.title}</h2>
    <div class="space-y-4 text-on-surface-variant text-base leading-relaxed flex-grow">
        {#each currentMessage.body as paragraph}
            <p>{paragraph}</p>
        {/each}
    </div>
    {#if currentMessage.info}
        <div class="mt-8 bg-surface-container-low rounded-DEFAULT p-4 flex items-start gap-3">
            <span class="material-symbols-outlined text-primary mt-0.5">info</span>
            <p class="text-sm text-on-surface-variant">
                {currentMessage.info}
            </p>
        </div>
    {/if}
</Bento>
