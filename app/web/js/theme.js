/* Theme: system / light / dark.

   tokens.css defines all three states; this only lets the user override the
   system and remembers the choice. THREE states, not two: "system" has to stay
   reachable, and the stamped attribute is what stops prefers-color-scheme
   applying.

   Loaded FIRST in index.html and applied synchronously, so the attribute is on
   <html> before the stylesheet paints. */

const THEME_KEY = 'ma.theme';
const THEMES = ['system', 'light', 'dark'];

function applyTheme(mode) {
  const root = document.documentElement;
  if (mode === 'system') root.removeAttribute('data-theme');
  else root.setAttribute('data-theme', mode);
}

function storedTheme() {
  try {
    const v = localStorage.getItem(THEME_KEY);
    return THEMES.includes(v) ? v : 'system';
  } catch {
    // Private windows and locked-down policies can throw on access, not just
    // return null. Falling back to system is the correct answer either way.
    return 'system';
  }
}

function setTheme(mode) {
  if (!THEMES.includes(mode)) mode = 'system';
  applyTheme(mode);
  try { localStorage.setItem(THEME_KEY, mode); } catch { /* not fatal */ }
  const btn = document.getElementById('theme-toggle');
  if (btn) {
    btn.dataset.mode = mode;
    btn.textContent = { system: 'Auto', light: 'Light', dark: 'Dark' }[mode];
    btn.title = `Theme: ${mode} (click to change)`;
    btn.setAttribute('aria-label', `Theme: ${mode}. Click to change.`);
  }
}

function cycleTheme() {
  setTheme(THEMES[(THEMES.indexOf(storedTheme()) + 1) % THEMES.length]);
}

// Before first paint.
applyTheme(storedTheme());

document.addEventListener('DOMContentLoaded', () => {
  setTheme(storedTheme());
  const btn = document.getElementById('theme-toggle');
  if (btn) btn.addEventListener('click', cycleTheme);
});
