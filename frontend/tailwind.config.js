/** @type {import('tailwindcss').Config} */
export default {
	darkMode: 'class',
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				surface: '#F9F9FB',
				'surface-bright': '#F9F9FB',
				'surface-dim': '#D9DADC',
				'surface-variant': '#E2E2E4',

				'surface-container-lowest': '#FFFFFF',
				'surface-container-low': '#F3F3F5',
				'surface-container': '#EEEEF0',
				'surface-container-high': '#E8E8EA',
				'surface-container-highest': '#E2E2E4',

				'on-surface': '#1A1C1D',
				'on-surface-variant': '#434751',
				'on-background': '#1A1C1D',

				primary: '#004490',
				'primary-container': '#2A5CAA',
				'on-primary': '#FFFFFF',
				'on-primary-container': '#C6D7FF',

				secondary: '#4F5E7E',
				'secondary-container': '#CBDAFF',
				'on-secondary': '#FFFFFF',
				'on-secondary-container': '#505F7F',

				outline: '#737782',
				'outline-variant': '#C3C6D3',

				error: '#BA1A1A',
				'error-container': '#FFDAD6',
				'on-error': '#FFFFFF',
				'on-error-container': '#93000A'
			},
			borderRadius: {
				bento: '1.5rem',
				pill: '9999px'
			},
			fontFamily: {
				headline: ['Manrope', 'sans-serif'],
				body: ['Manrope', 'sans-serif'],
				label: ['Manrope', 'sans-serif']
			}
		}
	}
};
