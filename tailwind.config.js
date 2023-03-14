/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './pages/**/*.{html,js}',
    './templates/*.{html,js}',
  ],
  theme: {
    extend: {},
  },
  plugins: [
      require('@tailwindcss/forms'),
      require('@tailwindcss/aspect-ratio'),
      require('@tailwindcss/typography'),
      require('tailwindcss-children'),
  ],
}
