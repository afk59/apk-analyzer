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
    'analyze.download.body': 'Fetch APKs from a public mirror and analyse them as one batch. Separate packages with commas or new lines. Each APK starts analysing as soon as it arrives while the rest keep downloading. Each download is checked: it must be a real APK, and its manifest package must be the one you asked for.',
    'analyze.download.btn': 'Download &amp; start analysis',
    'analyze.download.ph': 'com.example.app, com.example.other',
    'analyze.start': 'Start analysis',
    'analyze.target': 'Target',
    'analyze.hint': 'pick a file or a folder first',

    'run.title': 'Running',
    'run.cancel': 'Cancel',
    'run.finished': 'Finished',
    'run.cancelled': 'Cancelled',

    'results.title': 'Results',
    'results.rescan': 'Rescan disk',
    'results.lede': 'Grouped by run, newest first. Click a row to open its report; the button opens the Excel export, and &times; deletes the report from disk and from the library. <em>Rescan disk</em> rebuilds the index from <code>engine/result/</code> alone &mdash; the index is only ever a copy of what is already there.',
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
    'msg.streamLost': 'Lost the event stream. The run continues — reload the window (F5) to resync.',
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

    'analyze.skip': 'Skip files that already have a report',
    'run.aggregating': 'Building the batch workbooks',
    'msg.downloadFailed': 'DOWNLOAD FAILED',
    'msg.fileFailed': 'FAILED',
    'msg.alreadyAnalysed': 'already analysed',
    'msg.workbooksWritten': 'Batch workbooks written.',
    'msg.workbooksFailed': 'Could not build the batch workbooks',
    'msg.run': 'Run',
    'theme.title': 'Theme',
    'theme.system': 'Auto',
    'theme.light': 'Light',
    'theme.dark': 'Dark',

    'pc.batch': 'Each EXE/DLL its own report (batch)',
    'pc.combined': 'One combined report for the whole program',
    'pc.recursive': 'Include subfolders',
    'pc.resources': 'Include .resources.dll (.NET language packs, no code)',
    'pc.willRun': 'binaries will be analysed',
    'pc.program': 'Program folder',
    'dl.queued': 'queued',
    'dl.downloading': 'downloading',
    'dl.ready': 'downloaded',
    'dl.analysing': 'analysing',
    'dl.analysed': 'analysed',
    'dl.failed': 'failed',
    'results.delete': 'Delete this report',
    'results.confirm': 'Delete?',
    'msg.deleted': 'Deleted',
    'results.selectAll': 'Select all',
    'results.select': 'Select',
    'results.selectRun': 'Select this run',
    'results.selected': 'selected',
    'results.deleteSelected': 'Delete selected',
    'results.confirmMany': 'Delete {n}?',
    'msg.refused': 'refused',
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
    'analyze.download.body': 'APK’ları açık bir aynadan indirip tek bir toplu analiz olarak çalıştırır. Paketleri virgülle ya da alt alta yazın. Her APK iner inmez analize girer, diğerleri arka planda inmeye devam eder. Her indirme denetlenir: gerçek bir APK olmalı ve manifest’teki paket adı istediğinizle aynı olmalı.',
    'analyze.download.btn': 'İndir ve analizi başlat',
    'analyze.download.ph': 'com.ornek.uygulama, com.ornek.diger',
    'analyze.start': 'Analizi başlat',
    'analyze.target': 'Hedef',
    'analyze.hint': 'önce bir dosya veya klasör seçin',

    'run.title': 'Çalışıyor',
    'run.cancel': 'İptal',
    'run.finished': 'Bitti',
    'run.cancelled': 'İptal edildi',

    'results.title': 'Sonuçlar',
    'results.rescan': 'Diski yeniden tara',
    'results.lede': 'Koşulara göre gruplanmış, en yenisi üstte. Raporu açmak için satıra tıklayın; düğme Excel çıktısını açar, &times; raporu diskten ve kütüphaneden siler. <em>Diski yeniden tara</em>, dizini yalnızca <code>engine/result/</code> içeriğinden yeniden kurar &mdash; dizin her zaman orada zaten var olanın bir kopyasıdır.',
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
    'msg.streamLost': 'Olay akışı koptu. Koşu devam ediyor — eşitlemek için pencereyi yenileyin (F5).',
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

    'analyze.skip': 'Raporu olan dosyaları atla',
    'run.aggregating': 'Toplu çalışma kitapları oluşturuluyor',
    'msg.downloadFailed': 'İNDİRME BAŞARISIZ',
    'msg.fileFailed': 'BAŞARISIZ',
    'msg.alreadyAnalysed': 'zaten analiz edilmiş',
    'msg.workbooksWritten': 'Toplu çalışma kitapları yazıldı.',
    'msg.workbooksFailed': 'Toplu çalışma kitapları oluşturulamadı',
    'msg.run': 'Koşu',
    'theme.title': 'Tema',
    'theme.system': 'Otomatik',
    'theme.light': 'Açık',
    'theme.dark': 'Koyu',

    'pc.batch': 'Her EXE/DLL için ayrı rapor (toplu)',
    'pc.combined': 'Tüm program için tek birleşik rapor',
    'pc.recursive': 'Alt klasörleri dahil et',
    'pc.resources': '.resources.dll dosyalarını dahil et (.NET dil paketleri, kod içermez)',
    'pc.willRun': 'ikili dosya analiz edilecek',
    'pc.program': 'Program klasörü',
    'dl.queued': 'sırada',
    'dl.downloading': 'iniyor',
    'dl.ready': 'indi',
    'dl.analysing': 'analiz ediliyor',
    'dl.analysed': 'analiz edildi',
    'dl.failed': 'başarısız',
    'results.delete': 'Bu raporu sil',
    'results.confirm': 'Silinsin mi?',
    'msg.deleted': 'Silindi',
    'results.selectAll': 'Tümünü seç',
    'results.select': 'Seç',
    'results.selectRun': 'Bu koşuyu seç',
    'results.selected': 'seçili',
    'results.deleteSelected': 'Seçilenleri sil',
    'results.confirmMany': '{n} rapor silinsin mi?',
    'msg.refused': 'reddedildi',
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
    'analyze.download.body': '从公开镜像获取 APK 并作为一个批次进行分析。包名之间用逗号或换行分隔。每个 APK 下载完成后立即开始分析，其余的继续在后台下载。每次下载都会校验：必须是真正的 APK，且清单中的包名必须与所请求的一致。',
    'analyze.download.btn': '下载并开始分析',
    'analyze.download.ph': 'com.example.app, com.example.other',
    'analyze.start': '开始分析',
    'analyze.target': '目标平台',
    'analyze.hint': '请先选择文件或文件夹',

    'run.title': '正在运行',
    'run.cancel': '取消',
    'run.finished': '已完成',
    'run.cancelled': '已取消',

    'results.title': '结果',
    'results.rescan': '重新扫描磁盘',
    'results.lede': '按运行分组，最新的在前。点击行可打开其报告；按钮打开 Excel 导出，&times; 从磁盘和库中删除该报告。<em>重新扫描磁盘</em> 仅根据 <code>engine/result/</code> 重建索引 &mdash; 索引始终只是磁盘内容的副本。',
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
    'msg.streamLost': '事件流已断开。运行仍在继续 — 刷新窗口 (F5) 以同步。',
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

    'analyze.skip': '跳过已有报告的文件',
    'run.aggregating': '正在生成批量工作簿',
    'msg.downloadFailed': '下载失败',
    'msg.fileFailed': '失败',
    'msg.alreadyAnalysed': '已分析过',
    'msg.workbooksWritten': '批量工作簿已写入。',
    'msg.workbooksFailed': '无法生成批量工作簿',
    'msg.run': '运行',
    'theme.title': '主题',
    'theme.system': '自动',
    'theme.light': '浅色',
    'theme.dark': '深色',

    'pc.batch': '每个 EXE/DLL 单独生成报告（批量）',
    'pc.combined': '整个程序生成一份合并报告',
    'pc.recursive': '包含子文件夹',
    'pc.resources': '包含 .resources.dll（.NET 语言包，不含代码）',
    'pc.willRun': '个二进制文件将被分析',
    'pc.program': '程序文件夹',
    'dl.queued': '排队中',
    'dl.downloading': '下载中',
    'dl.ready': '已下载',
    'dl.analysing': '分析中',
    'dl.analysed': '已分析',
    'dl.failed': '失败',
    'results.delete': '删除此报告',
    'results.confirm': '删除？',
    'msg.deleted': '已删除',
    'results.selectAll': '全选',
    'results.select': '选择',
    'results.selectRun': '选择此次运行',
    'results.selected': '已选择',
    'results.deleteSelected': '删除所选',
    'results.confirmMany': '删除 {n} 项？',
    'msg.refused': '被拒绝',
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
