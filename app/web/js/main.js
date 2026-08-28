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

function coverageBits(a) {
  // The engine's own honesty rules, carried through unchanged: a packed DEX or
  // a sample too small to rate gets a reason, never a flattering number.
  if (a.coverage_status === 'ok')     return a.coverage_pct + '% coverage';
  if (a.coverage_status === 'packed') return 'coverage not measurable';
  if (a.coverage_status === 'low')    return 'too few refs to rate';
  return null;
}

function appRow(a) {
  const row = document.createElement('div');
  row.className = 'result' + (a.status === 'failed' ? ' fail' : '');
  row.tabIndex = 0;
  row.setAttribute('role', 'button');

  const bits = [];
  if (a.package_name) bits.push(a.package_name);
  const cov = coverageBits(a);
  if (cov) bits.push(cov);
  if (a.version) bits.push('v' + a.version);

  row.innerHTML = '<div class="grow"><div class="name">' +
    escapeHtml(a.app_name || a.source_file) + '</div><div class="meta">' +
    escapeHtml(a.status === 'failed' ? (a.error || 'failed') : bits.join('  ·  ')) +
    '</div></div>';

  // A failed app gets no chips and nothing to open. The caller appends it --
  // returning early here must not also append, or the row lands twice.
  if (a.status === 'failed') return row;

  if (a.packer) {
    row.insertAdjacentHTML('beforeend',
      '<span class="chip packed">DEX packed · ' + escapeHtml(a.packer) + '</span>');
  } else if (a.framework) {
    row.insertAdjacentHTML('beforeend', '<span class="chip">' + escapeHtml(a.framework) + '</span>');
  }
  if (a.kit_count !== null && a.kit_count !== undefined) {
    row.insertAdjacentHTML('beforeend', '<span class="chip kits">' + a.kit_count + ' kits</span>');
  }
  const art = a.artifacts || {};
  if (art.xlsx) {
    const btn = document.createElement('button');
    btn.className = 'btn ghost';
    btn.textContent = 'Excel';
    btn.addEventListener('click', (ev) => { ev.stopPropagation(); openPath(art.xlsx); });
    row.appendChild(btn);
  }
  if (art.html) {
    const open = () => openPath(art.html);
    row.addEventListener('click', open);
    row.addEventListener('keydown', (ev) => {
      if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); open(); }
    });
  }
  return row;
}

function runGroup(r) {
  const wrap = document.createElement('div');
  wrap.className = 'rungroup';

  const when = r.started_at ? r.started_at.replace('T', ' ') : '';
  const ok = r.apps.filter(a => a.status !== 'failed').length;
  const bad = r.apps.length - ok;
  const head = document.createElement('div');
  head.className = 'runhead';
  head.innerHTML = '<span class="title">' + escapeHtml(r.input_path || 'Run ' + r.id) + '</span>' +
    '<span class="when">' + escapeHtml(when) + '</span>' +
    '<span class="chip">' + ok + ' app' + (ok === 1 ? '' : 's') +
    (bad ? ' · ' + bad + ' failed' : '') +
    // A run that skipped everything would otherwise read as "0 apps" and look
    // like it did nothing. The skipped files belong to the run that produced
    // them, so they are counted here but listed there.
    (r.skipped_count ? ' · ' + r.skipped_count + ' reused' : '') + '</span>' +
    (r.status === 'cancelled' ? '<span class="chip packed">cancelled</span>' : '');
  wrap.appendChild(head);

  const body = document.createElement('div');
  body.className = 'results';
  r.apps.forEach(a => body.appendChild(appRow(a)));
  wrap.appendChild(body);
  return wrap;
}

async function loadResults() {
  const box = $('#results');
  box.innerHTML = '<div class="empty">Loading&hellip;</div>';
  try {
    const data = await API.results();
    box.innerHTML = '';

    if (data.workbooks && Object.keys(data.workbooks).length) {
      const wb = document.createElement('div');
      wb.className = 'workbooks';
      wb.innerHTML = '<span class="label">Batch workbooks</span>';
      Object.entries(data.workbooks).forEach(([name, path]) => {
        const b = document.createElement('button');
        b.className = 'btn ghost';
        b.textContent = name;
        b.addEventListener('click', () => openPath(path));
        wb.appendChild(b);
      });
      box.appendChild(wb);
    }

    if (!data.runs.length) {
      box.insertAdjacentHTML('beforeend',
        '<div class="empty">No reports yet. Analyse something and it shows up here.</div>');
      return;
    }
    data.runs.forEach(r => box.appendChild(runGroup(r)));
  } catch (e) {
    box.innerHTML = '';
    toast(e.message, true);
  }
}

$('#rescan').addEventListener('click', async () => {
  try {
    const c = await API.rescan();
    toast(`Rebuilt from disk — ${c.runs} run(s), ${c.apps} app(s).`);
    loadResults();
  } catch (e) { toast(e.message, true); }
});

/* -------------------------------------------------------------- boot */
(async () => {
  try {
    const h = await API.health();
    $('#status').textContent = h.mappings ? 'engine ready' : 'mappings missing';
  } catch {
    $('#status').textContent = 'server unreachable';
  }
})();
