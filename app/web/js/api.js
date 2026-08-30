/* Thin fetch wrapper. One place that knows how the backend reports an error,
   so every caller can just catch and show err.message. */

const API = (() => {
  async function call(path, options = {}) {
    let res;
    try {
      res = await fetch(path, options);
    } catch (e) {
      // The server is local, so a network error here means it died or never
      // came up -- worth saying plainly rather than "failed to fetch".
      throw new Error(typeof t === 'function' ? t('msg.noServer')
                                              : 'Cannot reach the local server.');
    }
    let body = null;
    const text = await res.text();
    if (text) { try { body = JSON.parse(text); } catch { /* not json */ } }
    if (!res.ok) {
      // FastAPI puts the message in `detail`; fall back to the status line.
      throw new Error((body && body.detail) || `${res.status} ${res.statusText}`);
    }
    return body;
  }

  const post = (path, data) => call(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data || {}),
  });

  return {
    health:  ()      => call('/api/health'),
    pick:    (kind)  => post('/api/pick', { kind }),
    open:    (path)  => post('/api/open', { path }),
    results:   ()    => call('/api/results'),
    startRun:  (input, target, skipExisting) =>
                       post('/api/runs', { input, target, skip_existing: skipExisting }),
    runState:  (id)  => call('/api/runs/' + id),
    cancelRun: (id)  => post('/api/runs/' + id + '/cancel', {}),
    rescan:    ()    => post('/api/rescan', {}),
    download:  (packages, target) => post('/api/downloads', { packages, target }),
  };
})();
