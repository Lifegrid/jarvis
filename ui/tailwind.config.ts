import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: 'class',
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './modules/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        jarvis: {
          blue: '#00BFFF',
          neon: '#00FFF7',
          dark: '#0B0F1A',
          gray: '#1C1F26',
          white: '#F0F8FF',
        },
      },
      backgroundImage: {
        'grid-light': "radial-gradient(circle, rgba(255,255,255,0.05) 1px, transparent 1px)",
      },
      animation: {
        pulse: 'pulse-bg 10s ease-in-out infinite',
      },
      fontFamily: {
        inter: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
export default config
