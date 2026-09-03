/* Starting a run, and showing progress while it happens.
   Uses $, escapeHtml, toast, showPanel, openPath and `state` from main.js. */

/* The stages the engine reports, in the order it reports them. There is no
   synthetic percentage inside a stage: androguard gives no progress signal, and
   a bar driven by elapsed time would be most wrong on the long files. */
/* Labels resolve through t() at draw time, so switching language redraws them
   and the stage machinery needs to know nothing about i18n. */
const STAGE_KEYS = ['loading', 'dex', 'scan', 'imports', 'kits', 'api', 'render'];
const STAGE_ORDER = STAGE_KEYS;
const stageLabel = (key) => t('stage.' + key);

const run = {
  id: null, total: 0, done: 0, source: null,
  fileStart: 0, timer: null, seen: new Set(),
};

function renderStages(active) {
  const box = $('#run-stages');
  const activeIdx = STAGE_ORDER.indexOf(active);
  box.innerHTML = '';
  STAGE_ORDER.forEach((key, i) => {
    // Stages are input-dependent: "imports" is EXE-only, "dex"/"scan" are
    // APK-only. Show a stage once it has been seen, or once it is the current
    // one -- so a pill never appears for a phase this input will never reach.
    if (!run.seen.has(key) && key !== active) return;
    const el = document.createElement('span');
    el.className = 'stage' + (key === active ? ' active' : (activeIdx > i || activeIdx === -1 ? ' done' : ''));
    el.textContent = stageLabel(key);
    box.appendChild(el);
  });
}

function logLine(text, cls) {
  const box = $('#run-log');
  const atBottom = box.scrollHeight - box.scrollTop - box.clientHeight < 24;
  const d = document.createElement('div');
  if (cls) d.className = cls;
  d.textContent = text;
  box.appendChild(d);
  // Autoscroll only if the user had not scrolled up to read something.
  if (atBottom) box.scrollTop = box.scrollHeight;
}

function tickElapsed() {
  if (!run.fileStart) return;
  const s = Math.round((Date.now() - run.fileStart) / 1000);
  $('#run-elapsed').textContent = s >= 60 ? Math.floor(s / 60) + 'm ' + (s % 60) + 's' : s + 's';
}

function updateBar() {
  const pct = run.total ? Math.round((run.done / run.total) * 100) : 0;
  $('#run-bar').style.width = pct + '%';
  $('#run-count').textContent = run.total > 1 ? run.done + ' / ' + run.total : '';
}

function doneRow(row, failed) {
  const el = document.createElement('div');
  el.className = 'result' + (failed ? ' fail' : '');
  if (failed) {
    el.innerHTML = '<div class="grow"><div class="name">' + escapeHtml(row.source_file) +
      '</div><div class="meta">' + escapeHtml(row.error || 'failed') + '</div></div>';
    $('#run-done').appendChild(el);
    return;
  }
  const bits = [];
  if (row.package_name) bits.push(row.package_name);
  // coverage_status carries the engine's own honesty rules: a packed DEX or a
  // sample too small to rate has no percentage and must not be given one here.
  if (row.coverage_status === 'ok') bits.push(row.coverage_pct + '% ' + t('msg.coverage'));
  else if (row.coverage_status === 'packed') bits.push(t('msg.notMeasurable'));
  else if (row.coverage_status === 'low') bits.push(t('msg.tooFew'));
  if (row.analysis_time_sec) bits.push(row.analysis_time_sec + 's');

  el.innerHTML = '<div class="grow"><div class="name">' +
    escapeHtml(row.app_name || row.source_file) + '</div><div class="meta">' +
    escapeHtml(bits.join('  ·  ')) + '</div></div>';
  if (row.packer) {
    el.insertAdjacentHTML('beforeend',
      '<span class="chip packed">' + t('msg.packed') + ' · ' + escapeHtml(row.packer) + '</span>');
  } else if (row.framework) {
    el.insertAdjacentHTML('beforeend', '<span class="chip">' + escapeHtml(row.framework) + '</span>');
  }
  el.insertAdjacentHTML('beforeend',
    '<span class="chip kits">' + row.kit_count + ' ' + t('msg.kits') + '</span>');
  el.addEventListener('click', () => openPath(row.report));
  $('#run-done').appendChild(el);
}

function handleEvent(ev) {
  switch (ev.stage) {
    case 'run_started':
      run.total = ev.file_count; updateBar(); break;
    case 'download_started':
      run.seen = new Set(); run.fileStart = Date.now();
      $('#run-file').textContent = ev.file;
      renderStages(null);
      logLine('── ' + t('msg.downloading') + ' ' + ev.file);
      break;
    case 'download_progress': {
      // The only place a real percentage exists in this app: a download knows
      // its Content-Length. Analysis does not, which is why nothing else shows
      // one.
      const mb = (n) => (n / 1048576).toFixed(1);
      $('#run-elapsed').textContent = mb(ev.got) + ' / ' + mb(ev.total) + ' MB';
      $('#run-bar').style.width =
        Math.round(((run.done + ev.got / ev.total) / (run.total || 1)) * 100) + '%';
      break;
    }
    case 'download_done':
      logLine(t('msg.fetched') + ' ' + ev.file + (ev.version ? ' v' + ev.version : '') +
              ' — ' + t('msg.from') + ' ' + ev.source, 'ok');
      // Say when the config splits were dropped. The analysis is still valid --
      // most of the reference corpus is base splits too -- but native libraries
      // will be missing and the reader should know why.
      if (ev.note) logLine('  ' + ev.note, 'warn');
      break;
    case 'download_failed':
      run.done++; updateBar();
      doneRow({ source_file: ev.file, error: ev.error }, true);
      logLine('DOWNLOAD FAILED ' + ev.file + ' — ' + ev.error, 'err');
      break;
    case 'file_started':
      run.seen = new Set();
      run.fileStart = Date.now();
      $('#run-file').textContent = ev.file;
      renderStages(null);
      logLine('── ' + ev.file);
      break;
    case 'file_skipped':
      run.done++; updateBar();
      logLine(t('msg.skipped') + ' ' + ev.file + ' — ' + ev.reason, 'ok');
      break;
    case 'file_done':
      run.done++; updateBar(); doneRow(ev.result, false);
      logLine(t('msg.done') + ' ' + ev.file, 'ok');
      break;
    case 'file_failed':
      run.done++; updateBar();
      doneRow({ source_file: ev.file, error: ev.error }, true);
      logLine('FAILED ' + ev.file + ' — ' + ev.error, 'err');
      break;
    case 'run_finished':
      finishRun(ev);
      break;
    case 'log':
      if (ev.level === 'warn' || ev.level === 'raw') logLine(ev.detail, 'warn');
      break;
    default:
      if (ev.stage && STAGE_KEYS.includes(ev.stage)) {
        run.seen.add(ev.stage);
        renderStages(ev.stage);
        logLine('  ' + stageLabel(ev.stage) + (ev.detail ? ': ' + ev.detail : ''));
      }
  }
}

function finishRun(ev) {
  clearInterval(run.timer); run.timer = null; run.fileStart = 0;
  if (run.source) { run.source.close(); run.source = null; }
  $('#run-file').textContent = t(ev.status === 'cancelled' ? 'run.cancelled' : 'run.finished');
  $('#run-cancel').disabled = true;
  run.seen = new Set();
  renderStages(null);
  $('#run-bar').style.width = '100%';
  toast(ev.status === 'cancelled'
    ? t('msg.cancelled')
    : t('msg.finished') + ' — ' + ev.ok + ' ' + t('msg.ok') + ', ' +
      ev.failed + ' ' + t('msg.failed') + '.', ev.failed > 0);
  $('#start').disabled = false;
}

/* Shared by "Start analysis" and "Download & analyse": both create a run and
   then watch the same event stream. */
function beginRun(res) {
  run.id = res.run_id; run.total = res.file_count; run.done = 0; run.seen = new Set();
  $('#nav-run').hidden = false;
  $('#run-done').innerHTML = '';
  $('#run-log').innerHTML = '';
  $('#run-cancel').disabled = false;
  $('#run-file').textContent = res.input;
  updateBar();
  showPanel('run');
  if (res.skip_existing) logLine(t('msg.skipping'), 'ok');

  run.source = new EventSource('/api/runs/' + res.run_id + '/events');
  run.source.onmessage = (m) => {
    try { handleEvent(JSON.parse(m.data)); } catch (e) { /* keep-alive or partial */ }
  };
  run.source.addEventListener('end', () => {
    if (run.source) { run.source.close(); run.source = null; }
  });
  run.source.onerror = () => {
    // EventSource reconnects by itself; only a hard close is worth reporting,
    // and even then the run keeps going server-side.
    if (run.source && run.source.readyState === EventSource.CLOSED) {
      logLine(t('msg.streamLost'), 'warn');
    }
  };
  clearInterval(run.timer);
  run.timer = setInterval(tickElapsed, 1000);
}

async function startRun() {
  const input = state.file || state.folder;
  if (!input) return;
  $('#start').disabled = true;
  try {
    const res = await API.startRun(input, $('#target').value, null);
    beginRun(res);
  } catch (e) {
    toast(e.message, true);
    $('#start').disabled = false;
  }
}

$('#start').addEventListener('click', startRun);

$('#run-cancel').addEventListener('click', async () => {
  if (!run.id) return;
  try {
    await API.cancelRun(run.id);
    logLine(t('msg.cancelling'), 'warn');
  } catch (e) {
    toast(e.message, true);
  }
});


/* ------------------------------------------------------------ download */
async function startDownload() {
  const packages = $('#packages').value.trim();
  if (!packages) { toast(t('msg.pickFirst'), true); return; }
  $('#download').disabled = true;
  try {
    const res = await API.download(packages, $('#target').value);
    beginRun(res);
  } catch (e) {
    toast(e.message, true);
  } finally {
    $('#download').disabled = false;
  }
}

$('#download').addEventListener('click', startDownload);

/* i18n hook: redraw the stage pills in the new language, keeping the active one. */
function redrawStages() {
  const active = document.querySelector('.stage.active');
  const key = active ? STAGE_KEYS.find((k) => stageLabel(k) === active.textContent) : null;
  renderStages(key || null);
}
