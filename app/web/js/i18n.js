/* Interface language: English, Turkish, Simplified Chinese.

   The UI chrome is translated. The ANALYSIS OUTPUT is not: kit tokens,
   permission names, package names, framework labels and the HTML/Excel reports
   stay exactly as the engine produced them. Those are identifiers and
   deliverables, not prose.

   Applied by scanning for data-i18n attributes, so markup stays the source of
   truth for structure. Anything built at runtime calls t() directly. */

const I18N_KEY = 'ma.lang';
const LANGS = ['en', 'tr', 'zh'];

const STRINGS = {
  en: {
    'app.subtitle': 'Android / Windows / iOS &rarr; HarmonyOS NEXT',
    'nav.analyze': 'Analyze',
    'nav.progress': 'Progress',
    'nav.results': 'Results',
    'nav.note': 'Reports and workbooks are written by the same engine the CLI uses, into <code>engine/result/</code>.',

    'analyze.title': 'Analyze',
    'analyze.lede': 'Pick a single file, or a folder to analyse every supported file inside it. The picker is a native dialog, so what comes back is a real path the engine can read.',
    'analyze.single.title': 'Single file',
    'analyze.single.body': 'One APK, EXE, DLL or IPA. Produces an HTML report and an agent JSON.',
    'analyze.single.btn': 'Choose file&hellip;',
    'analyze.folder.title': 'Batch folder',
    'analyze.folder.body': 'Every supported file in one folder, analysed one after another, plus the two summary workbooks.',
    'analyze.folder.btn': 'Choose folder&hellip;',
    'analyze.download.title': 'Download by package name',
    'analyze.download.body': 'Fetch the APK from a public mirror and analyse it. One package per line. Each download is checked: it must be a real APK, and its manifest package must be the one you asked for.',
    'analyze.download.btn': 'Download &amp; analyse',
    'analyze.start': 'Start analysis',
    'analyze.target': 'Target',
    'analyze.hint': 'pick a file or a folder first',

    'run.title': 'Running',
    'run.cancel': 'Cancel',
    'run.finished': 'Finished',
    'run.cancelled': 'Cancelled',

    'results.title': 'Results',
    'results.rescan': 'Rescan disk',
    'results.lede': 'Grouped by run, newest first. Click a row to open its report; the button opens the Excel export. <em>Rescan disk</em> rebuilds the index from <code>engine/result/</code> alone &mdash; the index is only ever a copy of what is already there.',
    'results.empty': 'No reports yet. Analyse something and it shows up here.',
    'results.loading': 'Loading&hellip;',
    'results.workbooks': 'Batch workbooks',

    'status.connecting': 'connecting…',
    'status.ready': 'engine ready',
    'status.nomappings': 'mappings missing',
    'status.unreachable': 'server unreachable',

    'msg.pickFirst': 'Enter at least one package name.',
    'msg.cancelled': 'Run cancelled.',
    'msg.noServer': 'Cannot reach the local server.',
    'msg.skipping': 'Files that already have a report will be skipped.',
    'msg.cancelling': 'Cancelling — the file in flight is stopped, the rest are skipped.',
    'msg.streamLost': 'Lost the event stream. The run continues — reopen Progress to resync.',
    'msg.rebuilt': 'Rebuilt from disk',
    'msg.finished': 'Finished',
    'msg.ok': 'ok',
    'msg.failed': 'failed',
    'msg.nothingHere': '&mdash; nothing here to analyse',
    'msg.supportedFiles': 'supported file(s)',
    'msg.skippedBundles': 'split-APK bundle(s) skipped &mdash; extract and use base.apk',
    'msg.downloading': 'downloading',
    'msg.fetched': 'fetched',
    'msg.from': 'from',
    'msg.done': 'done',
    'msg.skipped': 'skipped',
    'msg.reused': 'reused',
    'msg.apps': 'app(s)',
    'msg.kits': 'kits',
    'msg.coverage': 'coverage',
    'msg.notMeasurable': 'coverage not measurable',
    'msg.tooFew': 'too few refs to rate',
    'msg.packed': 'DEX packed',

    'stage.loading': 'Loading',
    'stage.dex': 'DEX',
    'stage.scan': 'Scanning refs',
    'stage.imports': 'Imports',
    'stage.kits': 'Matching kits',
    'stage.api': 'Matching APIs',
    'stage.render': 'Rendering',
  },

  tr: {
    'app.subtitle': 'Android / Windows / iOS &rarr; HarmonyOS NEXT',
    'nav.analyze': 'Analiz',
    'nav.progress': 'İlerleme',
    'nav.results': 'Sonuçlar',
    'nav.note': 'Raporlar ve çalışma kitapları, komut satırının kullandığı motorla <code>engine/result/</code> içine yazılır.',

    'analyze.title': 'Analiz',
    'analyze.lede': 'Tek bir dosya seçin ya da içindeki tüm desteklenen dosyaları analiz etmek için bir klasör seçin. Seçici yerel bir pencere olduğu için geriye motorun okuyabileceği gerçek bir yol döner.',
    'analyze.single.title': 'Tek dosya',
    'analyze.single.body': 'Bir APK, EXE, DLL veya IPA. HTML rapor ve agent JSON üretir.',
    'analyze.single.btn': 'Dosya seç&hellip;',
    'analyze.folder.title': 'Toplu klasör',
    'analyze.folder.body': 'Bir klasördeki tüm desteklenen dosyalar sırayla analiz edilir, ayrıca iki özet çalışma kitabı üretilir.',
    'analyze.folder.btn': 'Klasör seç&hellip;',
    'analyze.download.title': 'Paket adıyla indir',
    'analyze.download.body': 'APK’yı açık bir aynadan indirip analiz eder. Her satıra bir paket adı. Her indirme denetlenir: gerçek bir APK olmalı ve manifest’teki paket adı istediğinizle aynı olmalı.',
    'analyze.download.btn': 'İndir ve analiz et',
    'analyze.start': 'Analizi başlat',
    'analyze.target': 'Hedef',
    'analyze.hint': 'önce bir dosya veya klasör seçin',

    'run.title': 'Çalışıyor',
    'run.cancel': 'İptal',
    'run.finished': 'Bitti',
    'run.cancelled': 'İptal edildi',

    'results.title': 'Sonuçlar',
    'results.rescan': 'Diski yeniden tara',
    'results.lede': 'Koşulara göre gruplanmış, en yenisi üstte. Raporu açmak için satıra tıklayın; düğme Excel çıktısını açar. <em>Diski yeniden tara</em>, dizini yalnızca <code>engine/result/</code> içeriğinden yeniden kurar &mdash; dizin her zaman orada zaten var olanın bir kopyasıdır.',
    'results.empty': 'Henüz rapor yok. Bir şey analiz edin, burada görünecek.',
    'results.loading': 'Yükleniyor&hellip;',
    'results.workbooks': 'Toplu çalışma kitapları',

    'status.connecting': 'bağlanıyor…',
    'status.ready': 'motor hazır',
    'status.nomappings': 'mapping bulunamadı',
    'status.unreachable': 'sunucuya erişilemiyor',

    'msg.pickFirst': 'En az bir paket adı girin.',
    'msg.cancelled': 'Koşu iptal edildi.',
    'msg.noServer': 'Yerel sunucuya erişilemiyor.',
    'msg.skipping': 'Raporu zaten olan dosyalar atlanacak.',
    'msg.cancelling': 'İptal ediliyor — işlenen dosya durduruluyor, kalanlar atlanıyor.',
    'msg.streamLost': 'Olay akışı koptu. Koşu devam ediyor — eşitlemek için İlerleme’yi yeniden açın.',
    'msg.rebuilt': 'Diskten yeniden kuruldu',
    'msg.finished': 'Bitti',
    'msg.ok': 'başarılı',
    'msg.failed': 'başarısız',
    'msg.nothingHere': '&mdash; burada analiz edilecek bir şey yok',
    'msg.supportedFiles': 'desteklenen dosya',
    'msg.skippedBundles': 'bölünmüş APK paketi atlandı &mdash; açıp base.apk kullanın',
    'msg.downloading': 'indiriliyor',
    'msg.fetched': 'indirildi',
    'msg.from': 'kaynak',
    'msg.done': 'tamam',
    'msg.skipped': 'atlandı',
    'msg.reused': 'yeniden kullanıldı',
    'msg.apps': 'uygulama',
    'msg.kits': 'kit',
    'msg.coverage': 'kapsam',
    'msg.notMeasurable': 'kapsam ölçülemiyor',
    'msg.tooFew': 'derecelendirmek için çok az referans',
    'msg.packed': 'DEX paketlenmiş',

    'stage.loading': 'Yükleniyor',
    'stage.dex': 'DEX',
    'stage.scan': 'Referans taraması',
    'stage.imports': 'İçe aktarmalar',
    'stage.kits': 'Kit eşleştirme',
    'stage.api': 'API eşleştirme',
    'stage.render': 'Rapor üretimi',
  },

  zh: {
    'app.subtitle': 'Android / Windows / iOS &rarr; HarmonyOS NEXT',
    'nav.analyze': '分析',
    'nav.progress': '进度',
    'nav.results': '结果',
    'nav.note': '报告和工作簿由命令行所用的同一引擎写入 <code>engine/result/</code>。',

    'analyze.title': '分析',
    'analyze.lede': '选择单个文件，或选择一个文件夹以分析其中所有受支持的文件。选择器是系统原生对话框，因此返回的是引擎可读取的真实路径。',
    'analyze.single.title': '单个文件',
    'analyze.single.body': '一个 APK、EXE、DLL 或 IPA。生成 HTML 报告和 agent JSON。',
    'analyze.single.btn': '选择文件&hellip;',
    'analyze.folder.title': '批量文件夹',
    'analyze.folder.body': '依次分析文件夹中所有受支持的文件，并生成两个汇总工作簿。',
    'analyze.folder.btn': '选择文件夹&hellip;',
    'analyze.download.title': '按包名下载',
    'analyze.download.body': '从公开镜像获取 APK 并进行分析。每行一个包名。每次下载都会校验：必须是真正的 APK，且清单中的包名必须与所请求的一致。',
    'analyze.download.btn': '下载并分析',
    'analyze.start': '开始分析',
    'analyze.target': '目标平台',
    'analyze.hint': '请先选择文件或文件夹',

    'run.title': '正在运行',
    'run.cancel': '取消',
    'run.finished': '已完成',
    'run.cancelled': '已取消',

    'results.title': '结果',
    'results.rescan': '重新扫描磁盘',
    'results.lede': '按运行分组，最新的在前。点击行可打开其报告；按钮打开 Excel 导出。<em>重新扫描磁盘</em> 仅根据 <code>engine/result/</code> 重建索引 &mdash; 索引始终只是磁盘内容的副本。',
    'results.empty': '暂无报告。分析任意内容后即会显示在此。',
    'results.loading': '加载中&hellip;',
    'results.workbooks': '批量工作簿',

    'status.connecting': '连接中…',
    'status.ready': '引擎就绪',
    'status.nomappings': '缺少映射文件',
    'status.unreachable': '无法连接服务器',

    'msg.pickFirst': '请至少输入一个包名。',
    'msg.cancelled': '运行已取消。',
    'msg.noServer': '无法连接到本地服务器。',
    'msg.skipping': '已有报告的文件将被跳过。',
    'msg.cancelling': '正在取消 — 当前文件已停止，其余文件跳过。',
    'msg.streamLost': '事件流已断开。运行仍在继续 — 重新打开“进度”以同步。',
    'msg.rebuilt': '已从磁盘重建',
    'msg.finished': '已完成',
    'msg.ok': '成功',
    'msg.failed': '失败',
    'msg.nothingHere': '&mdash; 此处没有可分析的内容',
    'msg.supportedFiles': '个受支持的文件',
    'msg.skippedBundles': '个拆分 APK 包已跳过 &mdash; 请解压并使用 base.apk',
    'msg.downloading': '正在下载',
    'msg.fetched': '已获取',
    'msg.from': '来源',
    'msg.done': '完成',
    'msg.skipped': '已跳过',
    'msg.reused': '复用',
    'msg.apps': '个应用',
    'msg.kits': '个 kit',
    'msg.coverage': '覆盖率',
    'msg.notMeasurable': '覆盖率无法测量',
    'msg.tooFew': '引用过少，无法评级',
    'msg.packed': 'DEX 已加壳',

    'stage.loading': '加载中',
    'stage.dex': 'DEX',
    'stage.scan': '扫描引用',
    'stage.imports': '导入表',
    'stage.kits': '匹配 kit',
    'stage.api': '匹配 API',
    'stage.render': '生成报告',
  },
};

function storedLang() {
  try {
    const v = localStorage.getItem(I18N_KEY);
    if (LANGS.includes(v)) return v;
  } catch { /* private window */ }
  // Follow the browser, but only into a language we actually have.
  const nav = (navigator.language || 'en').toLowerCase();
  if (nav.startsWith('tr')) return 'tr';
  if (nav.startsWith('zh')) return 'zh';
  return 'en';
}

let LANG = storedLang();

/** Translate a key. Falls back to English, then to the key itself -- a missing
 *  string must never render as "undefined". */
function t(key, fallback) {
  const table = STRINGS[LANG] || STRINGS.en;
  return table[key] !== undefined ? table[key]
       : (STRINGS.en[key] !== undefined ? STRINGS.en[key]
       : (fallback !== undefined ? fallback : key));
}

function applyI18n() {
  document.documentElement.lang = LANG;
  document.querySelectorAll('[data-i18n]').forEach((el) => {
    el.innerHTML = t(el.dataset.i18n);
  });
  document.querySelectorAll('[data-i18n-ph]').forEach((el) => {
    el.placeholder = t(el.dataset.i18nPh);
  });
  document.querySelectorAll('[data-i18n-title]').forEach((el) => {
    el.title = t(el.dataset.i18nTitle);
  });
  const sel = document.getElementById('lang');
  if (sel) sel.value = LANG;
}

function setLang(lang) {
  if (!LANGS.includes(lang)) lang = 'en';
  LANG = lang;
  try { localStorage.setItem(I18N_KEY, lang); } catch { /* not fatal */ }
  applyI18n();
  // Re-render anything the scripts built themselves.
  if (typeof onLanguageChanged === 'function') onLanguageChanged();
}

document.addEventListener('DOMContentLoaded', () => {
  applyI18n();
  const sel = document.getElementById('lang');
  if (sel) sel.addEventListener('change', () => setLang(sel.value));
});
