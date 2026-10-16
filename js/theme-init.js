/*
 * Luci theme bootstrap. Paste this INLINE in <head>, before any stylesheet,
 * so the right theme is set before first paint (no flash of the wrong theme).
 *
 *   1. A script element whose body is this file's contents
 *   2. Then the stylesheet link to /css/index.css
 *
 * Stored preference: localStorage "luci-theme" = "light" | "dark" | "system" (default).
 * Resolved theme goes on <html data-theme="light|dark">; the preference on data-theme-pref.
 */
(function () {
  var pref = 'system';
  try { pref = localStorage.getItem('luci-theme') || 'system'; } catch (e) {}
  var dark = pref === 'dark' ||
    (pref === 'system' && window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches);
  var root = document.documentElement;
  root.setAttribute('data-theme', dark ? 'dark' : 'light');
  root.setAttribute('data-theme-pref', pref);
})();
