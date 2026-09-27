/* Theme: system / light / dark.

   tokens.css already defines all three states -- light on bare :root, dark
   under both `prefers-color-scheme` and `[data-theme="dark"]`. All this does is
   let the user override the system, and remember the choice.

   THREE states, not two. "System" has to stay reachable: dropping it would mean
   an app that ignores the OS setting forever after one stray click, and the
   stamped attribute is exactly what stops prefers-color-scheme applying.

   Loaded FIRST in index.html and applied synchronously, so the attribute is on
   <html> before the stylesheet paints. Doing it after would show one frame of
   the wrong theme on every start. */

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
    // theme.js runs before i18n.js, so t() may not exist yet on the very
    // first call; main.js calls setTheme again when the language changes.
    const tr = (k, en) => (typeof t === 'function' ? t(k, en) : en);
    const label = tr('theme.' + mode, { system: 'Auto', light: 'Light', dark: 'Dark' }[mode]);
    btn.textContent = label;
    btn.title = tr('theme.title', 'Theme') + ': ' + label;
    btn.setAttribute('aria-label', btn.title);
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
