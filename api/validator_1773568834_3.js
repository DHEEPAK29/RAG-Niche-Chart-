/**
 * Module: validator
 * Project: RAG-Niche-Chart-
 */

const { fontFamily } = require('tailwindcss/defaultTheme');

/** @type {import('tailwindcss').Config} */

module.exports = {
  darkMode: ['selector'],
  content: [
    './src/pages/**/*.tsx',
    './src/components/**/*.tsx',
    './src/layouts/**/*.tsx',
  ],
  theme: {
    container: {
      center: true,
      padding: '2rem',
