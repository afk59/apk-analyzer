/* Panels, pickers, and the results list. */

const $  = (sel) => document.querySelector(sel);
const $$ = (sel) => Array.from(document.querySelectorAll(sel));

const state = { file: null, folder: null, program: null };

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
  // A program folder is EXE/DLL with no APK/IPA beside it; the server says so
  // by sending the counts its options can produce.
  state.program = (kind === 'folder' && res.program) ? res.program : null;
  $('#picked-file').hidden   = !state.file;
  $('#picked-folder').hidden = !state.folder;
  $('#skip-wrap').hidden     = !state.folder;
  $('#pc-opts').hidden       = !state.program;
  const input = state.file || state.folder;
  // Picking during a run must not re-enable Start (run.js owns that).
  const busy = typeof run !== 'undefined' && run.source;
  $('#start').disabled = !input || !!busy;
  $('#start-hint').textContent = input ? '' : t('analyze.hint');

  const box = kind === 'folder' ? $('#picked-folder') : $('#picked-file');
  let html = `<strong>${escapeHtml(res.name)}</strong><br>${escapeHtml(res.path)}`;
  if (kind === 'folder' && state.program) {
    html += '<br>' + t('pc.program');
  } else if (kind === 'folder') {
    const n = res.file_count || 0;
    html += '<br><strong>' + n + '</strong> ' + t('msg.supportedFiles');
    if (n === 0) {
      html += ' <span class="warn">' + t('msg.nothingHere') + '</span>';
    }
    // APKM/XAPK are ZIPs of split APKs with no dex of their own. Saying so beats
    // letting someone wonder why their file was ignored.
    if (res.skipped_bundles && res.skipped_bundles.length) {
      html += '<br><span class="warn">' + res.skipped_bundles.length + ' ' +
              t('msg.skippedBundles') + ': ' +
              escapeHtml(res.skipped_bundles.join(', ')) + '</span>';
    }
  }
  box.innerHTML = html;
  box.hidden = false;
  updatePcCount();
}

/* The options a program-folder run is started with, or null for any other
   input. Read at Start, so what runs is what the boxes say. */
function pcOptions() {
  if (!state.program) return null;
  const mode = (document.querySelector('input[name="pc-mode"]:checked') || {}).value || 'batch';
  return { pc_mode: mode, recursive: $('#pc-recursive').checked,
           include_resources: $('#pc-resources').checked };
}

/* The number on screen is the number that will run: every combination the
   checkboxes can make was counted by the server when the folder was picked. */
function updatePcCount() {
  const p = state.program;
  if (!p) return;
  const o = pcOptions();
  const batch = o.pc_mode === 'batch';
  $('#pc-recursive').disabled = !batch;
  $('#pc-resources').disabled = !batch;
  const n = !batch ? null
    : (o.recursive ? p.all + (o.include_resources ? p.all_resources : 0)
                   : p.top + (o.include_resources ? p.top_resources : 0));
  $('#pc-count').innerHTML = batch
    ? '<strong>' + n + '</strong> ' + escapeHtml(t('pc.willRun'))
    : escapeHtml(t('pc.combined'));
  // Never re-enables Start while a run is streaming (run.js owns that).
  const busy = typeof run !== 'undefined' && run.source;
  $('#start').disabled = !!busy || (batch && n === 0);
}

$$('#pc-opts input').forEach((el) => el.addEventListener('change', updatePcCount));

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
  if (a.coverage_status === 'ok')     return a.coverage_pct + '% ' + t('msg.coverage');
  if (a.coverage_status === 'packed') return t('msg.notMeasurable');
  if (a.coverage_status === 'low')    return t('msg.tooFew');
  return null;
}

/* ---------------------------------------------------------- selection
   Keyed by what the server deletes by -- a report path, or a manifest entry
   for a failed row -- so the same report listed under two runs is one item,
   and a rescan that renumbers every row cannot change what is selected. */
const selection = new Map();          // key -> delete target
const targetOf = (a, group) => {
  const art = a.artifacts || {};
  if (art.html) return { report: art.html };
  if (a.status === 'failed' && group && group.manifest) {
    return { manifest: group.manifest, source_file: a.source_file };
  }
  return null;                        // nothing the server could delete
};
const keyOf = (target) => JSON.stringify(target);

function pickBox(target) {
  const box = document.createElement('input');
  box.type = 'checkbox';
  box.className = 'pick';
  box.dataset.key = keyOf(target);
  box.checked = selection.has(box.dataset.key);
  box.setAttribute('aria-label', t('results.select'));
  // The row itself opens the report; ticking a box must not.
  box.addEventListener('click', (ev) => ev.stopPropagation());
  box.addEventListener('keydown', (ev) => ev.stopPropagation());
  box.addEventListener('change', () => {
    setSelected(box.dataset.key, target, box.checked);
    syncSelection();
  });
  return box;
}

function setSelected(key, target, on) {
  if (on) selection.set(key, target); else selection.delete(key);
}

/* Every checkbox, the per-run boxes and the bar are derived from `selection`,
   so a row ticked in one run shows ticked wherever else it is listed. */
function syncSelection() {
  const boxes = $$('#results input.pick');
  boxes.forEach((b) => { b.checked = selection.has(b.dataset.key); });
  $$('#results input.pick-run').forEach((rb) => {
    const mine = Array.from(rb.closest('.rungroup').querySelectorAll('input.pick'));
    const n = mine.filter((b) => b.checked).length;
    rb.checked = mine.length > 0 && n === mine.length;
    rb.indeterminate = n > 0 && n < mine.length;
  });
  const all = $('#sel-all');
  const keys = new Set(boxes.map((b) => b.dataset.key));
  const n = selection.size;
  all.checked = keys.size > 0 && n === keys.size;
  all.indeterminate = n > 0 && n < keys.size;
  $('#sel-count').textContent = n ? n + ' ' + t('results.selected') : '';
  const del = $('#del-selected');
  del.disabled = n === 0;
  disarmBulk();
}

let bulkTimer = null;
function disarmBulk() {
  const del = $('#del-selected');
  clearTimeout(bulkTimer);
  del.classList.remove('armed');
  del.textContent = t('results.deleteSelected');
}

/* Same two-step as the row x: the first click says how many will go. */
async function deleteSelected() {
  const del = $('#del-selected');
  if (!selection.size) return;
  if (!del.classList.contains('armed')) {
    del.classList.add('armed');
    del.textContent = t('results.confirmMany').replace('{n}', selection.size);
    bulkTimer = setTimeout(disarmBulk, 4000);
    return;
  }
  clearTimeout(bulkTimer);
  del.disabled = true;
  try {
    const res = await API.deleteMany(Array.from(selection.values()));
    const gone = (res.reports || 0) + (res.failures || 0);
    const refused = (res.refused || []).length;
    toast(t('msg.deleted') + ': ' + gone + (refused ? ' · ' + refused + ' ' + t('msg.refused') : '') + '.',
          refused > 0);
    selection.clear();
    loadResults();
  } catch (e) {
    toast(e.message, true);
    syncSelection();
  }
}

$('#sel-all').addEventListener('change', () => {
  const on = $('#sel-all').checked;
  $$('#results input.pick').forEach((b) => setSelected(b.dataset.key, JSON.parse(b.dataset.key), on));
  syncSelection();
});
$('#del-selected').addEventListener('click', deleteSelected);

function appRow(a, group) {
  const row = document.createElement('div');
  row.className = 'result' + (a.status === 'failed' ? ' fail' : '');
  row.tabIndex = 0;
  row.setAttribute('role', 'button');
  const target = targetOf(a, group);

  const bits = [];
  if (a.package_name) bits.push(a.package_name);
  const cov = coverageBits(a);
  if (cov) bits.push(cov);
  if (a.version) bits.push('v' + a.version);

  row.innerHTML = '<div class="grow"><div class="name">' +
    escapeHtml(a.app_name || a.source_file) + '</div><div class="meta">' +
    escapeHtml(a.status === 'failed' ? (a.error || t('msg.failed')) : bits.join('  ·  ')) +
    '</div></div>';
  if (target) row.prepend(pickBox(target));

  // A failed app gets no chips and nothing to open. The caller appends it --
  // returning early here must not also append, or the row lands twice.
  if (a.status === 'failed') {
    if (group && group.manifest) {
      row.appendChild(deleteButton({ manifest: group.manifest, source_file: a.source_file }));
    }
    return row;
  }

  if (a.packer) {
    row.insertAdjacentHTML('beforeend',
      '<span class="chip packed">' + t('msg.packed') + ' · ' + escapeHtml(a.packer) + '</span>');
  } else if (a.framework) {
    row.insertAdjacentHTML('beforeend', '<span class="chip">' + escapeHtml(a.framework) + '</span>');
  }
  if (a.kit_count !== null && a.kit_count !== undefined) {
    row.insertAdjacentHTML('beforeend',
      '<span class="chip kits">' + a.kit_count + ' ' + t('msg.kits') + '</span>');
  }
  const art = a.artifacts || {};
  if (art.xlsx) {
    const btn = document.createElement('button');
    btn.className = 'btn ghost';
    btn.textContent = 'Excel';
    btn.addEventListener('click', (ev) => { ev.stopPropagation(); openPath(art.xlsx); });
    row.appendChild(btn);
  }
  if (art.html) row.appendChild(deleteButton({ report: art.html }));
  if (art.html) {
    const open = () => openPath(art.html);
    row.addEventListener('click', open);
    row.addEventListener('keydown', (ev) => {
      if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); open(); }
    });
  }
  return row;
}

/* The x on a result row. Two clicks: the first arms it and says what it will
   do, the second deletes. A native confirm() is not used -- whether it shows at
   all depends on the webview backend, and a delete that cannot be undone must
   not depend on that. Disarms itself after a few seconds. */
function deleteButton(target) {
  const b = document.createElement('button');
  b.className = 'del';
  b.innerHTML = '&times;';
  b.title = t('results.delete');
  b.setAttribute('aria-label', t('results.delete'));
  let timer = null;
  b.addEventListener('click', async (ev) => {
    ev.stopPropagation();
    if (!b.classList.contains('armed')) {
      b.classList.add('armed');
      b.textContent = t('results.confirm');
      timer = setTimeout(() => { b.classList.remove('armed'); b.innerHTML = '&times;'; }, 4000);
      return;
    }
    clearTimeout(timer);
    b.disabled = true;
    try {
      await API.deleteResult(target);
      toast(t('msg.deleted') + '.');
      loadResults();
    } catch (e) {
      toast(e.message, true);
      b.disabled = false;
    }
  });
  b.addEventListener('keydown', (ev) => ev.stopPropagation());
  return b;
}

function runGroup(r) {
  const wrap = document.createElement('div');
  wrap.className = 'rungroup';

  const when = r.started_at ? r.started_at.replace('T', ' ') : '';
  const ok = r.apps.filter(a => a.status !== 'failed').length;
  const bad = r.apps.length - ok;
  const head = document.createElement('div');
  head.className = 'runhead';
  head.innerHTML = '<span class="title">' + escapeHtml(r.input_path || t('msg.run') + ' ' + r.id) + '</span>' +
    '<span class="when">' + escapeHtml(when) + '</span>' +
    '<span class="chip">' + ok + ' ' + t('msg.apps') +
    (bad ? ' · ' + bad + ' ' + t('msg.failed') : '') +
    // A run that skipped everything would otherwise read as "0 apps" and look
    // like it did nothing. The skipped files belong to the run that produced
    // them, so they are counted here but listed there.
    (r.skipped_count ? ' · ' + r.skipped_count + ' ' + t('msg.reused') : '') + '</span>' +
    (r.status === 'cancelled' ? '<span class="chip packed">' + t('run.cancelled') + '</span>' : '');
  // Select every row of this run. Only when the run has something deletable.
  if (r.apps.some((a) => targetOf(a, r))) {
    const rb = document.createElement('input');
    rb.type = 'checkbox';
    rb.className = 'pick-run';
    rb.setAttribute('aria-label', t('results.selectRun'));
    rb.addEventListener('change', () => {
      wrap.querySelectorAll('input.pick').forEach((b) =>
        setSelected(b.dataset.key, JSON.parse(b.dataset.key), rb.checked));
      syncSelection();
    });
    head.prepend(rb);
  }
  wrap.appendChild(head);

  const body = document.createElement('div');
  body.className = 'results';
  r.apps.forEach(a => body.appendChild(appRow(a, r)));
  wrap.appendChild(body);
  return wrap;
}

async function loadResults() {
  const box = $('#results');
  box.innerHTML = '<div class="empty">' + t('results.loading') + '</div>';
  try {
    const data = await API.results();
    box.innerHTML = '';

    if (data.workbooks && Object.keys(data.workbooks).length) {
      const wb = document.createElement('div');
      wb.className = 'workbooks';
      wb.innerHTML = '<span class="label">' + t('results.workbooks') + '</span>';
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
        '<div class="empty">' + t('results.empty') + '</div>');
      selection.clear();
      $('#selbar').hidden = true;
      return;
    }
    data.runs.forEach(r => box.appendChild(runGroup(r)));
    // What was selected and is still listed stays selected; what was deleted
    // or vanished in a rescan drops out.
    const listed = new Set($$('#results input.pick').map((b) => b.dataset.key));
    Array.from(selection.keys()).forEach((k) => { if (!listed.has(k)) selection.delete(k); });
    $('#selbar').hidden = listed.size === 0;
    syncSelection();
  } catch (e) {
    box.innerHTML = '';
    toast(e.message, true);
  }
}

$('#rescan').addEventListener('click', async () => {
  try {
    const c = await API.rescan();
    toast(t('msg.rebuilt') + ' — ' + c.runs + ' / ' + c.apps + ' ' + t('msg.apps') + '.');
    loadResults();
  } catch (e) { toast(e.message, true); }
});

/* -------------------------------------------------------------- boot */
(async () => {
  try {
    const h = await API.health();
    $('#status').textContent = t(h.mappings ? 'status.ready' : 'status.nomappings');
  } catch {
    $('#status').textContent = t('status.unreachable');
  }
})();

/* Called by i18n.setLang. applyI18n only touches elements carrying data-i18n,
   so anything the scripts built themselves has to be redrawn here. */
function onLanguageChanged() {
  const input = state.file || state.folder;
  $('#start-hint').textContent = input ? '' : t('analyze.hint');
  if (!$('#panel-results').hidden) loadResults();
  if (typeof redrawStages === 'function') redrawStages();
  if (typeof setTheme === 'function' && typeof storedTheme === 'function') setTheme(storedTheme());
}
