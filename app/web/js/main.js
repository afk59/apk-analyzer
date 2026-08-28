/* Panels, pickers, and the results list. */

const $  = (sel) => document.querySelector(sel);
const $$ = (sel) => Array.from(document.querySelectorAll(sel));

const state = { file: null, folder: null };

/* -------------------------------------------------------------- toast */
let toastTimer = null;
function toast(message, isError) {
  const el = $('#toast');
  el.textContent = message;
  el.classList.toggle('error', !!isError);
  el.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => el.classList.remove('show'), 3600);
}

/* ------------------------------------------------------------- panels */
function showPanel(name) {
  $$('.panel').forEach(p => { p.hidden = p.id !== `panel-${name}`; });
  $$('nav.side button').forEach(b => {
    if (b.dataset.panel === name) b.setAttribute('aria-current', 'page');
    else b.removeAttribute('aria-current');
  });
  if (name === 'results') loadResults();
}

$$('nav.side button').forEach(b => b.addEventListener('click', () => showPanel(b.dataset.panel)));

/* ------------------------------------------------------------ pickers */
function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

async function pick(kind) {
  const btn = kind === 'folder' ? $('#pick-folder') : $('#pick-file');
  btn.disabled = true;
  try {
    const res = await API.pick(kind);
    // A cancelled dialog returns {path: null}. Leaving the previous selection
    // alone is the right behaviour -- cancel means "never mind", not "clear".
    if (!res || !res.path) return;
    state[kind === 'folder' ? 'folder' : 'file'] = res.path;
    renderPicked(kind, res);
  } catch (e) {
    toast(e.message, true);
  } finally {
    btn.disabled = false;
  }
}

function renderPicked(kind, res) {
  // The most recent pick wins, so choosing a folder after a file does what it
  // looks like it does instead of silently keeping the earlier selection.
  if (kind === 'folder') state.file = null; else state.folder = null;
  $('#picked-file').hidden   = !state.file;
  $('#picked-folder').hidden = !state.folder;
  const input = state.file || state.folder;
  $('#start').disabled = !input;
  $('#start-hint').textContent = input ? '' : 'pick a file or a folder first';

  const box = kind === 'folder' ? $('#picked-folder') : $('#picked-file');
  let html = `<strong>${escapeHtml(res.name)}</strong><br>${escapeHtml(res.path)}`;
  if (kind === 'folder') {
    const n = res.file_count || 0;
    html += `<br><strong>${n}</strong> supported file${n === 1 ? '' : 's'}`;
    if (n === 0) {
      html += ' <span class="warn">&mdash; nothing here to analyse</span>';
    }
    // APKM/XAPK are ZIPs of split APKs with no dex of their own. Saying so beats
    // letting someone wonder why their file was ignored.
    if (res.skipped_bundles && res.skipped_bundles.length) {
      html += `<br><span class="warn">Skipped ${res.skipped_bundles.length} split-APK bundle(s):
               ${escapeHtml(res.skipped_bundles.join(', '))} &mdash; extract and use base.apk</span>`;
    }
  }
  box.innerHTML = html;
  box.hidden = false;
}

$('#pick-file').addEventListener('click',   () => pick('file'));
$('#pick-folder').addEventListener('click', () => pick('folder'));

/* ------------------------------------------------------------ results */
async function openPath(path) {
  try {
    await API.open(path);
  } catch (e) {
    toast(e.message, true);
  }
}

function resultRow(item) {
  const row = document.createElement('div');
  row.className = 'result';
  row.tabIndex = 0;
  row.setAttribute('role', 'button');

  const title = item.app_name || item.name;
  const bits = [];
  if (item.package) bits.push(item.package);
  if (item.mode)    bits.push(item.mode.toUpperCase());
  bits.push(new Date(item.modified * 1000).toLocaleString());

  row.innerHTML = `
    <div class="grow">
      <div class="name">${escapeHtml(title)}</div>
      <div class="meta">${escapeHtml(bits.join('  ·  '))}</div>
    </div>`;

  if (item.packer) {
    row.insertAdjacentHTML('beforeend',
      `<span class="chip packed">DEX packed &middot; ${escapeHtml(item.packer)}</span>`);
  } else if (item.framework) {
    row.insertAdjacentHTML('beforeend', `<span class="chip">${escapeHtml(item.framework)}</span>`);
  }
  if (item.kits !== null && item.kits !== undefined) {
    row.insertAdjacentHTML('beforeend', `<span class="chip kits">${item.kits} kits</span>`);
  }
  if (item.xlsx) {
    const btn = document.createElement('button');
    btn.className = 'btn ghost';
    btn.textContent = 'Excel';
    btn.addEventListener('click', (ev) => { ev.stopPropagation(); openPath(item.xlsx); });
    row.appendChild(btn);
  }

  const open = () => openPath(item.report);
  row.addEventListener('click', open);
  row.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); open(); }
  });
  return row;
}

async function loadResults() {
  const box = $('#results');
  box.innerHTML = '<div class="empty">Loading&hellip;</div>';
  try {
    const { items } = await API.results();
    box.innerHTML = '';
    if (!items.length) {
      box.innerHTML = '<div class="empty">No reports yet. Analyse something and it shows up here.</div>';
      return;
    }
    items.forEach(item => box.appendChild(resultRow(item)));
  } catch (e) {
    box.innerHTML = '';
    toast(e.message, true);
  }
}

/* -------------------------------------------------------------- boot */
(async () => {
  try {
    const h = await API.health();
    $('#status').textContent = h.mappings ? 'engine ready' : 'mappings missing';
  } catch {
    $('#status').textContent = 'server unreachable';
  }
})();
