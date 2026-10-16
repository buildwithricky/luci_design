/*
 * Luci runtime theme control. Load after theme-init.js (e.g. as a module in your app shell).
 *
 *   import { setTheme, getThemePreference } from './theme.js';
 *   setTheme('dark');    // 'light' | 'dark' | 'system'
 */
const KEY = 'luci-theme';
const media = window.matchMedia('(prefers-color-scheme: dark)');
const root = document.documentElement;

export function getThemePreference() {
  try { return localStorage.getItem(KEY) || 'system'; } catch { return 'system'; }
}

function apply(pref) {
  const dark = pref === 'dark' || (pref === 'system' && media.matches);
  root.setAttribute('data-theme', dark ? 'dark' : 'light');
  root.setAttribute('data-theme-pref', pref);
  // Keep the browser chrome (mobile address bar) in step with the canvas colour.
  const meta = document.querySelector('meta[name="theme-color"]');
  if (meta) meta.setAttribute('content', getComputedStyle(root).getPropertyValue('--color-background-canvas').trim());
}

export function setTheme(pref) {
  try {
    if (pref === 'system') localStorage.removeItem(KEY);
    else localStorage.setItem(KEY, pref);
  } catch { /* private mode: theme still applies for this page view */ }
  // Suppress transitions for the one frame the theme flips, so colours don't animate.
  root.classList.add('theme-switching');
  apply(pref);
  requestAnimationFrame(() => requestAnimationFrame(() => root.classList.remove('theme-switching')));
}

// Follow the OS when the user has chosen "system".
media.addEventListener('change', () => {
  if (getThemePreference() === 'system') apply('system');
});

// Keep several open tabs in step.
window.addEventListener('storage', (e) => {
  if (e.key === KEY) apply(e.newValue || 'system');
});

apply(getThemePreference());
