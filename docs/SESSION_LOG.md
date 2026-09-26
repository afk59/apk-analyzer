# v2 Çalışma Günlüğü

Bakım yapan kişiye yönelik, Türkçe, kalıcı kayıt. v1'in `OTURUM_2026-08-20.txt` dosyasının
devamı — o dosya `docs/v1/SESSION_LOG_2026-08-20.txt` altında duruyor ve hâlâ geçerli.

**Kural:** her oturumun sonunda buraya yaz. Ne yapıldı, ne ölçüldü, ne bilinçli olarak
yapılmadı, ve sıradaki adım ne. Ölçülmemiş bir iddia yazma.

---

## 2026-08-28 — v2 kuruldu

### Öncesinde: v1 GitHub'a eksiksiz alındı

Şirketin özel repolarına aktarılacağı için `main` kendi kendine yeter hale getirildi.

- **Dört fix** (housekeeping turu): UTF-8 stdio + batch özetinin sona alınması, split-APK
  bundle'a artık "Native" denmemesi, `--mode exe_folder`, `hmos_api.xlsx`'in repoya alınması.
  Hiçbiri analiz çıktısını değiştirmiyor — `com.mtr.mobile` öncesi/sonrası hash birebir aynı.
- **gitignore denetimi**: `ohpm_registry_cache.json` (3.499 paketlik OHPM taraması) ve
  `play_metadata_cache.json` repoya alındı. Bunlar olmadan temiz bir klon sessizce bozuk
  çalışıyordu — OHPM paket varlığı doğrulanamıyor, çevrimdışı batch "No internet connection"
  yazıyordu.
- **`docs-ref/` commit edildi**: 8.495 dosya / ~110 MB, pack sonrası 21.7 MB.
- Repoda kalmayanlar sadece: APK/EXE/IPA test korpusu ve üretilen çıktılar.
- `main` fast-forward ile 15 commit ileri alındı ve push'landı.

> **Windows uzun yol uyarısı:** korpustaki en derin yol 212 karakter. Şirket tarafında klondan
> önce `git config --global core.longpaths true` gerekiyor, yoksa checkout yarıda "Filename too
> long" ile kalıyor — ve bu bir *clone* hatası olarak değil *checkout* hatası olarak görünüyor,
> yani repo sağlam sanılıyor.

### v2 iskeleti

`v2` branch'i açıldı ve `C:/Users/AFK/Claude/projects/apk-analyzer-v2` klasöründe ayrı bir
git worktree olarak duruyor. Aynı repo, aynı origin, ayrı klasör — v1 klasörü `main`'de kaldı,
ikisi birbirini etkilemiyor.

- `src/` → `engine/` (sadece klasör adı değişti; iç importlar ve veri yolları o klasöre göreli
  olduğu için hiçbir şey kırılmadı). **Doğrulandı:** yeni konumdan `python engine/analyzer.py`
  rapor üretiyor.
- v1 dokümanları `docs/v1/` altına taşındı — hiçbiri silinmedi.
- Yeni kök `CLAUDE.md` **kısa** yazıldı. v1'inki 149 KB'a çıkmıştı ve her oturum başında
  tamamı yükleniyordu; ayrıntı artık `docs/` altında konu başına bir dosyada.
- `app/` iskeleti: karar içeren yerler gerçek kod (`config.py`, `store/db.py` şeması), geri
  kalanı sözleşme (docstring) — çalışmayan kodu çalışıyormuş gibi göstermemek için.

### Alınan kararlar (hepsi `docs/decisions/` altında)

| # | Karar | Kısa gerekçe |
|---|---|---|
| 0001 | pywebview + FastAPI + elle yazılmış HTML/CSS | Node/Electron kurumsal makinede en riskli parça; tarayıcı ise gerçek path veremiyor ve Excel açamıyor |
| 0002 | SQLite **indeks**, çıktılar dosya olarak kalıyor | Sorgu gereken özellikler geliyor; ama DB silinip yeniden taranabilir olmalı |
| 0003 | `engine/` miras ve davranışı donuk | Mapping'ler ve kurallar ürünün kendisi; test yok, yeniden yapılandırma riski taşımıyor |
| 0004 | Mapping işi **sadece v2**'de | Tek dal `mapping.json`'a dokunuyor, çakışma yok; bedeli: aktif işler v2 stabil olana kadar eski mapping ile |
| 0005 | Dosya başına bir subprocess | androguard belleği geri vermiyor; ölçüldü: tek süreç 4 kez düştü, süreç-başına 42/43 sıfır hata |
| 0006 | İndirici izole + indirileni **doğrula** | Korpusta zaten yanlış uygulama olan iki dosya var; otomasyon bu hatayı azaltmaz, artırır |

### `docs-ref` daha ilk bakışta bir v1 sorusunu çözdü

v1, v1.10.0'da 8 adet HTTP client satırını `@kit.NetworkKit`'e maplerken şunu yazmıştı:
*"`@kit.RemoteCommunicationKit` (`rcp`) KULLANILMADI: index'te sıfır kez geçiyor… Eğer rcp
gerçekse ve sadece index'te yoksa bu satırlar tekrar gözden geçirilmeli."*

**rcp gerçek.** Korpusta
`harmonyos-guides/system/network/remote-communication-kit/` var — About This Kit, *Network
Communication Using HTTP*, HTTP transmission performance, URPC scenarios. Yani v1'in kendi
istediği revizyon artık yapılabilir. M5'in ilk maddesi.

Ayrıca doğrulandı ve rehbere yazıldı: `kits/` klasöründe **sadece 47 açık SDK kiti** var.
ScanKit, PushKit, MapKit, PaymentKit gibi kapalı/HMS kitlerinin `.d.ts`'i **yok** ama hepsi
doküman korpusunda mevcut. Yani ".d.ts'te yoksa yoktur" demek, v1'in `hmos_api_index.json`
hatasını yeni bir biçimde tekrarlamak olur.

### Bilinçli olarak yapılmayanlar

- UI'ın kendisi (M1). İskelet hazır, kod gece yazılacak.
- Test harness'ı hâlâ yok. **Radikal değişiklik öncesi en büyük risk bu** ve v2 daha da çok
  hareketli parça getiriyor. M2'nin kabul kriteri (üretilen HTML/XLSX'in v1 CLI çıktısıyla
  bayt bayt aynı olması) bunun yerini kısmen tutuyor ama yeterli değil.
- `engine/`'e hiç dokunulmadı.

### Sıradaki

1. M1 — pencere açılsın, native picker çalışsın, mevcut bir rapor tıklamayla açılsın.
2. M2 — worker + gerçek progress. Kabul kriteri: çıktılar v1 CLI ile bayt bayt aynı.
3. M5'in ilk maddesi (rcp revizyonu) M1/M2'den bağımsız, istenirse paralel yürür.

---

## 2026-08-28 (ek) — `docs-ref` `main`'den çıkarıldı, iki iddia düzeltildi

Bakım yapan kişinin notu üzerine: `docs-ref` sadece mapping yazmak için var, şirkete giden
ürünün parçası değil. `main`'den silindi, `v2`'de duruyor.

**Ölçülen sonuç:** `main`'de 8.529 → **34** dosya, en uzun yol 212 → **54** karakter. Windows
uzun-yol tuzağı bir workaround olarak belgelenmek yerine tamamen ortadan kalktı; `core.longpaths`
artık `main` için hiç gerekmiyor. Klasör yolu için boşluk 47 → ~205 karakter.

**Bu arada iki iddiam yanlış çıktı, ikisi de düzeltildi.** `main`'e dosya eklerken hangi
dosyanın gerçekten çalışma zamanında okunduğunu varsaymışım; grep'leyince:

| Dosya | Gerçek durum |
|---|---|
| `ohpm_registry_cache.json` | `ohpm_fetch.py`'yi **hiçbir şey import etmiyor** — standalone builder. Cache mapping zamanı işine yarıyor, analize değil. |
| `hmos_api.xlsx` | Sadece `api_index.py` okuyor, o da tek seferlik index üreteci. Mapping zamanı. |

İkisi de repoda kaldı (4.2 MB, mapping işini mümkün kılıyor) ama artık ne oldukları yazıyor.
Analiz sırasında gerçekten okunan tek referans dosyası `hmos_api_index.json`, batch'te bir de
`play_metadata_cache.json`.

**Merge uyarısı:** `v2`'de `docs-ref` takipli. `v2` ileride `main`'e merge edilirse dosyalar geri
gelir — `.gitignore` kazara eklemeyi engeller, merge'ü engellemez. O commit'te tekrar silinmeli.

**Geçmiş:** blob'lar pack'te duruyor (~15 MB), yani tam klon onları yine indiriyor; sadece
checkout yazmıyor. Temizlemek history rewrite ister ve `v2` o commit'lerden dallandığı için onu
bozar — değmez. İsteyen `git clone --depth 1` kullanır.

---

## 2026-08-29 (gece) — M1'den M4'e: uygulama çalışır durumda

`python -m app` artık pencere açıyor, dosya/klasör seçtiriyor, analiz ediyor, ilerlemeyi canlı
gösteriyor, sonuçları listeliyor ve paket adından APK indiriyor. Dört milestone, dört commit.

### M1 — kabuk
pywebview penceresi + arka planda uvicorn. Native picker'lar **ayrı bir süreçte** çalışıyor:
hem tkinter hem pywebview GUI ana thread'ini istiyor, bizimki zaten pencerede; kendi ana
thread'ine sahip bir süreç bu sorunu tamamen ortadan kaldırıyor ve tarayıcı fallback'inde de
çalışıyor. `/api/open` **korumalı** — yol çözümlenip `engine/result/` içinde olduğu doğrulanıyor
(dışarısı ve `result/../../../Windows/...` ikisi de 403).

### M2 — analiz + gerçek ilerleme
Worker motoru **import ediyor**, `analyzer.py`'yi kabuk üzerinden çağırmıyor. Böylece hem CLI'ın
kendi bootstrap'i (bağımlılık kurulumu, loguru susturma, UTF-8) çalışıyor, hem de sonuç dict'i
elimizde kalıyor. En önemlisi: `print_info` motor modülleri onu bağlamadan **önce** patch'lendiği
için aşamalar motorun kendi faz çağrılarından geliyor — renkli konsol metnini regex'lemiyoruz.

**Bir aşamanın içinde yüzde YOK, bilerek.** androguard ilerleme sinyali vermiyor; süreye dayalı
bir çubuk tam da uzun dosyalarda yanlış olurdu (bu korpus 1,8 sn ile 1039 sn arasında değişiyor).

**Kabul kriteri karşılandı:** çıktılar v1 CLI ile birebir. HTML ve agent JSON hash'i aynı; XLSX
yalnızca iki yerde farklı, ikisi de zaman damgası.

**Toplu workbook'lar da eklendi** — yoksa klasör koşusu `--batch` ile eşdeğer olmuyordu.
`app/aggregate.py` side-car'lardan aggregation'ı tekrarlayıp **gerçek** exporter'ları çağırıyor.
v1'in kendi `run_batch`'iyle hücre hücre karşılaştırıldı: **6 sheet + 2 sheet, hepsi aynı.**

### M3 — sonuç kütüphanesi
Koşuya göre gruplanmış liste, SQLite indeks. "DB'yi sil, yeniden tara, kütüphane aynı" iddiasını
gerçekten doğru kılmak iki şey gerektirdi: koşu gruplaması diskte hiçbir yerde yok, bu yüzden
biten koşu `engine/result/.runs/` altına manifest yazıyor; ve coverage kaybolacaktı, çünkü agent
JSON namespace sayılarını taşımıyor — raporun kendi gömülü `report_data`'sından okunup **motorun**
`coverage_status()`'una veriliyor. Şema değişikliği ALTER değil **yeniden inşa** (her sütun zaten
diskten türetilebilir).

### M4 — paket adıyla indirme
`d.apkpure.com` doğrudan uç noktası. HTML ayrıştırmıyoruz, olmayan paket temiz 404 veriyor.

**Test sırasında iki şey ortaya çıktı ve tasarımı değiştirdi:**

1. **`/b/APK/` her zaman tek APK vermiyor.** `com.foodgulu` o yoldan 143,9 MB'lık bir App Bundle
   döndü. App Bundle artık Play'in varsayılanı olduğu için bunu reddetmek modern uygulamaların
   büyük kısmında indirmeyi başarısız kılardı — bu yüzden bundle açılıp `base.apk` analiz
   ediliyor ve config split'lerinin düştüğü **söyleniyor**. Bu bir bozulma değil: korpusun
   43 uygulamasından 27'si zaten base split. Ama native kütüphaneler gerçekten eksik kalıyor.
2. **Doğrulama boş bir formalite değil.** İndirilen dosyanın manifest paket adı istenenle
   eşleşmek zorunda. v1 korpusundaki iki yanlış dosya (Aptoide, Uptodown) tam olarak bu hatanın
   sonucuydu ve otomatik indirme bu riski **artırır**, azaltmaz. Test edildi: gerçek bir APK
   başka bir paket adıyla doğrulatıldığında reddediliyor.

**İki hata bulundu ve düzeltildi:**
- `file_count` fazladan sayıyordu (indirilen paket `paths`'e ekleniyor ama `packages`'ta kalıyor).
- **Yarış koşulu:** `run.status = "done"` manifest yazımından ve `run_finished` olayından ÖNCE
  atanıyordu. SSE'deki `finished` bu duruma bakıyor, yani o birkaç yüz milisaniyelik pencerede
  uyanan okuyucu akışı `run_finished` hiç gitmeden kapatıyordu — arayüzdeki "Start" butonu
  sonsuza kadar kapalı kalırdı. Artık status **en son** atanıyor.

### Sıradaki
M5 — `docs-ref` ile mapping yeniden temellendirme. İlk maddesi hazır: v1'in kendi istediği
`@kit.RemoteCommunicationKit` revizyonu. **Mapping satırları senin onayın olmadan yazılmayacak**;
öneri dokümanı çıkarılıp sunulacak.

---

## 2026-08-29 (gece, devam) — M5 ilk geçiş: v1'in altı boşluğu yeniden test edildi

**`mapping.json`'a hiçbir şey yazılmadı.** Hâlâ v1.10.0 / 279 satır. Bulgular
`docs/MAPPING_CANDIDATES_2026-08-29.md` içinde, satır satır onayın için.

| v1'in boşluğu | Sonuç |
|---|---|
| `android.credentials` | **Karşılık bulundu** — `@kit.OnlineAuthenticationKit` (FIDO/FIDO2/IIFAA/SOTER passwordless). Passkey 47, FIDO 48 dosya. |
| `com.scottyab.rootbeer` | **Karşılık bulundu** — `@kit.DeviceSecurityKit` / SafetyDetect: *"cihaz jailbreak'li mi veya gerçek cihaz değil mi kontrol eder"*. v1'in "native attestation API yok" gerekçesi yanlıştı. |
| `org.reactnative.facedetector` | **Karşılık bulundu** — `@kit.CoreVisionKit` (`faceDetector` + `faceComparator`, 40 attestasyon). v1 `@kit.VisionKit`'e bakmıştı; kendi notunda "core-vision-kit farklı bir kittir" yazmasına rağmen. |
| `net.openid.appauth` | **Boşluk DOĞRULANDI** — OAuth/OIDC 51/55/30 dosyada geçiyor ama hepsi Huawei'nin kendi yetkilendirme sunucusu (Account Kit REST). Genel sağlayıcı desteği yok. |
| `org.altbeacon` | **Boşluk DOĞRULANDI** — beacon 5 dosya, iBeacon 1, **Eddystone 0**. |
| `com.google.android.odml` | Değişmedi — katman uyuşmazlığı, doküman bunu çözmez. |

### `rcp` sorusu: gerçek, ama **dokunmamayı öneriyorum**

v1 "rcp gerçekse bu satırlar gözden geçirilmeli" demişti. Gerçek:
`rcp.createSession()` / `session.get()` / `session.post()` doğrulandı. **13 satırı** ilgilendiriyor
(8 değil). Ama:

1. Huawei kendi dokümanında *"ihtiyacına en uygun kiti seçebilirsin"* diyor — mevcut satırlar
   **yanlış değil**. Bu projenin kuralı "yanlış satır boşluktan kötüdür", "savunulabilir bir satırı
   başka bir savunulabilir satırla değiştir" değil.
2. `mapping.json` **append-only**. 13 satırı bir tercih için yeniden yazmak, bu kuralın ilk
   istisnası olurdu.
3. Avantaj kısmi: `rcp` oturum tabanlı (OkHttp şekli), ama `NetworkKit`'te de
   `http.HttpInterceptorChain` var ve socket/websocket yarısı zaten NetworkKit'te.

**Alternatif öneri:** bulguyu mapping dosyasına 13 kez yazmak yerine rapora **bir kez** koymak —
`@kit.NetworkKit` satırının altına tek cümle. Bu bir renderer değişikliği, senin kararın.

### Yöntem açısından en önemli çıkarım

Yukarıda bulunan **üç kitin de `kits/` altında `.d.ts`'i YOK**. Yani ".d.ts'te yoksa yoktur"
kuralı, v1'in `hmos_api_index.json` hatasını yeni bir biçimde tekrarlardı. Doğru yöntem:
korpusta **yeteneğe göre** ara, sonra çıkan yolun hangi kite ait olduğunu oku.

---

## 2026-08-30 (gece) — dark mode, 156 test, mapping v1.11.0

### Dark / light mode
Üç durum: **system / light / dark**, `localStorage`'da hatırlanıyor. İki değil üç,
çünkü `data-theme` özniteliği tam da `prefers-color-scheme`'i devre dışı bırakan şey —
"system" seçeneği olmasaydı bir tık sonra uygulama işletim sistemi ayarını sonsuza kadar
yok sayardı. `theme.js` `<head>` içinde ve **senkron** çalışıyor; sonrasında çalışsaydı
her açılışta bir kare yanlış tema görünürdü.

### Test altyapısı — 156 test, ~2,5 dakika, ek bağımlılık yok
Düz `unittest`. Kilitli bir makinede `pip install` listesine bir şey daha eklemek
bu projenin sürekli kaçındığı sürtünme.

İzolasyon: `app/config.py` artık `MA_RESULT_DIR` / `MA_DB_PATH` / `MA_INPUT_DIR`
değişkenlerini dinliyor, testler üçünü de temp dizine yönlendiriyor. Motor, web ve
docs-ref yolları **bilerek** yönlendirilemez — onları başka yere göstermek, bu
uygulamadan başka bir şeyi test etmek olurdu.

**Testlerin ilk koşuda bulduğu üç gerçek hata:**

1. **Reap zaman aşımı, yazılma sebebi olan durumda erişilemezmiş.** `for line in
   proc.stdout` çocuk süreç stdout'u kapatana kadar bitmiyor; sonucunu yazıp asılı
   kalan bir worker — yani v1'de en ağır dosyanın 8-11 GB tutarak asılı kalması —
   okuyucuyu sonsuza kadar bekletiyordu ve alttaki zaman aşımı hiç çalışmıyordu.
   Artık terminal olay döngüyü kırıyor.
2. **Worker yapılandırılmış sonuç dizinini yok sayıyordu**, `_ENGINE / "result"`
   sabitini kullanıyordu; yani her yönlendirme bir yalandı ve test paketi gerçek
   çıktı klasörüne yazardı.
3. **Koşu başına dosya tanıtıcısı sızıntısı** — aggregate adımı iki pipe'ı da
   kapatmıyordu. `-W error::ResourceWarning` altında ortaya çıktı.

Ayrıca 19 senaryo testi: **CJK/Türkçe/Kiril dosya adları** (v1'de 26 uygulamanın
11'ini kaybettiren hata — v2'de stdout her zaman pipe olduğu için bu artık uç
durum değil, norm), dağınık klasörler, **eşzamanlı iki koşu**, kütüphane yaşam
döngüsü ve mapping dosyası bütünlüğü.

### Motor hatası: var olmayan izinler öneriliyordu

Korpusun 41 eşleşmemiş iznini incelerken çıktı. `_OHOS_PERM_CATALOGUE`'daki 47
girdinin **dördü HarmonyOS izni değil**:

| Motorda | Gerçek |
|---|---|
| `READ_MEDIA_IMAGES` / `_VIDEO` | **Android** adları; HarmonyOS: `READ_IMAGEVIDEO` |
| `READ_MEDIA_AUDIO` | HarmonyOS: `READ_AUDIO` |
| `USE_BIOMETRIC` | gerçek ad `ACCESS_BIOMETRIC` |
| `ACCESS_NFC` | gerçek ad `NFC_TAG` |

İlk üçü migratöre **`high` güvenle** öneriliyordu — anahtar kelime eşleştirici tam
kelime örtüşmesine en yüksek puanı verdiği için, rapor tam da en yanlış olduğu
yerde en emindi.

**Bir izin adı artık üç bağımsız kaynağa karşı doğrulanıyor** (aralarında 748 ad):
`engine/data/permissions/*.txt` (132 — v1 bunları "kullanılmayan, atıl referans"
diye işaretlemişti, oysa asıl katalog bu), doküman korpusu (82, kısmi) ve
**SDK'nın `.d.ts` `@permission` anotasyonları (655, açık ara en zengin)**.
Tek kaynağa bakmak iki yönde de yanlış negatif üretirdi.

### mapping.json v1.10.0 → v1.11.0

**namespace 279 → 311 (+32), izin 38 → 67 (+29, 3 düzeltildi).**

**Expo korpustaki en büyük boşluktu ve hiç maplenmemişti** — 22 modül ailesinde
223 namespace. React Native çekirdeği zaten tamamen kapsanıyordu
(`com.facebook.react` altındaki her şeyi yutuyor), yani asıl delik Expo'daydı.
Modül modül maplendi, blanket `expo.` öneki değil: blanket kural modül
**çalışma zamanını** da yutardı (`expo.modules.kotlin` 37 ns, `core`, `adapters`,
`interfaces`…), oysa onun karşılığı yok ve unmapped kalması doğru.

**HMS SDK** taşıyan altı uygulama için kit karşılığı olanlar birebir maplendi;
**SDK altyapısı bilerek maplenmedi** (7.144 metot) — HarmonyOS NEXT'te kitler
sisteme gömülü olduğu için o katman **tamamen ortadan kalkıyor**; gösterecek bir
kit yok ve uydurmak "bu iş yok oluyor" yerine "port et" demek olurdu.

**İzin tarafında en değerlisi, sezgiselin aktif olarak yanlış olduğu yerler:**
dokuz üretici launcher rozet izni (her biri 11 uygulamada, korpusun en sık
eşleşmeyen izni) `MANAGE_SECURE_SETTINGS` diye cevaplanıyordu; HarmonyOS'ta rozet
`setBadgeNumber`, yani **izin gerektirmeyen bir API çağrısı**.

`KIT_DOC_URLS` 58 → 60; **mapping.json'daki 60 kit token'ının hepsi artık bir
dokümana çözülüyor.** İki yeni URL `docs-ref` içinde **birebir** geçiyor — dizin
yolundan tahmin edilmiş slug değil, crawler'ın koruduğu gerçek bağlantılar.

### Emilim — tahmin
12.030 unmapped satır üzerinde gerçek eşleştirme döngüsü tekrar oynatıldı:
**160 farklı namespace, 249 uygulama-başı satır, 38'i ≥2 uygulamada, 0 gölgeleme,
0 ölü kural.** Gerçek 43 uygulamalık koşuyla doğrulaması aşağıda.

---

## 2026-08-30 (gündüz) — mapping denetimi ve dil desteği

### "Halüsinasyon var mı" sorusunun cevabı: vardı, dokuzu

Her mapping dosyasının **her satırı** dört bağımsız kaynağa karşı denetlendi
(47 kit barrel, api `.d.ts`, taranmış doküman, üretilmiş index — aralarında
**97 kit token'ı ve 748 izin adı**). Bir değer, kaynaklardan **herhangi birinde**
geçiyorsa gerçek sayıldı; birinde yok olması hiçbir şey kanıtlamaz.

**`@kit.AnalyticsKit` diye bir kit yok.** "AnalyticsKit" dizesi 110 MB'lık
korpusta **tek bir kez bile geçmiyor** — kit token'ı olarak da değil, kelime
olarak da değil. 13 satır kullanıyordu (3 mapping.json, 10 ios_mapping) ve
`KIT_DOC_URLS`'te bir **HMS ürün sayfasına** bağlıydı, yani başka bir platforma.

İki şey bunu daha önce yakalamalıydı: satırların *kendi notları* hedefin
"AGConnect Analytics" olduğunu yazıyordu — o bir **ohpm paketi**, `@kit.*` değil.
Ve v1'in doc URL yanındaki yorumu zaten "bunun için HarmonyOS sayfası
doğrulanamadı" diyordu; bağlantı yine de bırakılmıştı.

Hepsi artık `@kit.PerformanceAnalysisKit`'e (hiAppEvent) bakıyor — HarmonyOS'un
uygulama-olayı tesisi orada (19 doküman dosyası) ve bu dosya zaten
`com.google.firebase.analytics`'i tam bu sebeple oraya yönlendiriyordu.

**`@kit.RelationalStoreKit` de yok**: `relationalStore`, `@kit.ArkData`
barrel'ında. Realm / RealmSwift / FMDB düzeltildi.

**Beş iOS izni Android adı taşıyordu** (Haziran'dan beri hiç denetlenmemiş dosya):
`READ_MEDIA_IMAGES/VIDEO` → `READ_IMAGEVIDEO`, `READ_MEDIA_AUDIO` → `READ_AUDIO`,
`WRITE_MEDIA_IMAGES` → `WRITE_IMAGEVIDEO`. `WRITE_HEALTH_DATA` ayrı bir durum:
**yazmaya özel bir sağlık izni yok**, o yüzden satır uydurma bir ad yerine
attestasyonlu `HEALTH_DATA`'ya bakıyor.

### v1 ↔ v2 karşılaştırması: hiçbir kit kaybolmadı

Arşivlenmiş v1.10.0 koşusu ile yeni koşu, agent JSON'lardan uygulama uygulama:

| | |
|---|---|
| eklenen kit türü | 4 (DeviceSecurityKit 5 uyg, OnlineAuthenticationKit 4, AdsKit 1, CoreVisionKit 1) |
| **kaybolan kit türü** | **0** |
| güven değişen | 3 satır |
| OHPM / framework değişimi | 0 |
| kapanan izin boşluğu | 29 farklı izin |

**Hiçbir uygulamadan hiçbir kit kaybolmadı** — asıl önemli özellik bu: satır
eklemek bir sonucu asla silmemeli. Üç güven değişimi min-güven politikasının
tasarım gereği çalışması; her biri adı belli bir yeni `medium` katkıcıdan
kaynaklanıyor.

Fazladan görünen 44. uygulama (`com.app.auralaw`) bir tutarsızlık değil —
**kullanıcının kendi koşusu**; manifest 10:50'de tek dosyalık bir koşu diyor.

### Kalıcı koruma
`tests/test_scenarios.py::TestMappingDataIntegrity` içinde beş test artık bu
denetimi her koşuda yapıyor: var olmayan kit, var olmayan doc URL, registry'de
olmayan OHPM paketi, var olmayan izin hedefi, var olmayan öneri. `docs-ref`
yoksa temizce atlanıyor, yani `main` etkilenmiyor.

### Dil desteği: EN / TR / 中文

**Ne çevriliyor, ne çevrilmiyor** — asıl karar bu. Arayüz *kabuğu* çevriliyor;
**analiz çıktısı çevrilmiyor**. Kit token'ları, izin adları, paket adları,
framework etiketleri ve HTML/Excel raporları motorun ürettiği gibi kalıyor.
Bunlar tanımlayıcı ve teslimat, düzyazı değil: `@kit.ArkUI` bir cümle değil, ve
okuyana göre farklı okunan bir rapor karşılaştırılamaz, başkasına iletilemez.
Bir test hedef adlarının üç dilde de değişmediğini doğruluyor.

Yapı olarak: işaretleme kaynak (`data-i18n`), dosya sadece dizeleri taşıyor.
Çalışma anında üretilen metinler doğrudan `t()` çağırıyor ve `setLang()`
`onLanguageChanged()` ile onları yeniden çizdiriyor. Aşama etiketleri çizim
anında çözülüyor, yani koşu ortasında dil değiştirmek onları yerinde
etiketliyor. `t()` önce İngilizce'ye sonra anahtara düşüyor — eksik bir dize
asla "undefined" olarak görünemez.

Gerçek pencerede 7 test, üç dil için: her `data-i18n` anahtarı çözülüyor, dil
etiketleniyor, seçim hatırlanıyor, kabuk üç dilde de gerçekten farklı, çalışma
anı metinleri de değişiyor, tanımlayıcılar dokunulmamış, sıfır JS hatası.

---

## 2026-09-02 — taşınabilirlik denetimi ve gözetimsiz ilk kurulum

Soru şuydu: repo başka bir bilgisayarda, sıfırdan, çalışır durumda mı?
Tahmin etmedik — temiz bir klon açıp orada ölçtük.

### Ölçülenler

| | |
|---|---|
| `origin/v2` ile fark | 0 ileri / 0 geri, çalışma ağacı temiz |
| Temiz klonda test | **173/173 geçti**, 10 atlandı (corpus ikilileri repoda yok, beklenen) |
| Temiz klonda uygulama | açıldı; `/api/health` → `mappings:true`, arayüz HTTP 200 |
| Kodda mutlak yol | yok — `app/config.py` her şeyi kökten türetiyor |
| Çalışma anı veri dosyaları | 14'ünün hepsi takipte |
| Paket boyutu | 21.68 MiB, git-lfs yok |

### Bulunan üç engel

1. **`pip install -r requirements.txt` hiçbir yerde yazmıyordu.** Boş bir venv'de
   `run.bat` → `ModuleNotFoundError: No module named 'uvicorn'` ve ardından
   `pause`. Motor kendi dört paketini `_ensure_deps()` ile kuruyordu; v2
   kabuğunun `fastapi` / `uvicorn` / `pywebview`'i için hiçbir karşılığı yoktu.
   **Bu oturumda düzeltildi**, aşağıda.

2. **Uzun yol sorunu belgelendiğinden daha sinsi.** `core.longpaths` bu repoda
   *yerel* ayarlı, global değil. Derin bir yola (≈130 karakter önek) klonladığımızda
   checkout başarılı göründü, **dosya sayısı bile doğruydu (8495)** — ama Python'un
   `rglob`'u `docs-ref` klasörlerini sessizce atlayınca `TestMappingDataIntegrity`
   içindeki iki test kırıldı ve mesaj "7 kit token'ı kanıtlanmamış" dedi. Aynı klon
   `C:\v2t`'de tertemiz geçti. Yani hata mapping'lerde değil yolun uzunluğundaydı,
   **ama insanı mapping'lerin bozuk olduğuna inandırıyor.** Şirket makinesinde repo
   kısa bir yola konmalı.

3. **`requirements.txt`'te sürüm pinlenmemiş.** Boş venv'e androguard **4.1.4**
   geldi, oysa burada 4.1.3 var ve 43 uygulamalık corpus 4.1.3 ile analiz edildi.
   Donmuş bir motor için istenmeyen tek şey sessiz sürüm kayması. **Düzeltildi**,
   aşağıda.

### Yapılan: ilk açılışta gözetimsiz kurulum

`app/__main__.py::_ensure_deps()`. Motorun `_ensure_deps`'ini aynalıyor — aynı pip
çağrısı, aynı proxy temizliği, aynı "ne yaptığını söyle" kuralı — iki bilinçli farkla:

- **Motorun dört paketi de burada kuruluyor.** Bu süreç onları import etmiyor;
  analiz alt sürecinin ihtiyacı olacak, ve şimdi çekmek ilk analizin yarı yolda
  pip'e gitmesini engelliyor.
- **Sadece `_FATAL` başarısızlığı iptal ettiriyor.** Motor dördünün herhangi biri
  için `sys.exit(1)` yapabilir çünkü CLI koşusunda dördü de taşıyıcı; burada
  `fastapi` ve `uvicorn` dışındaki bir eksik uygulamayı açılmaktan alıkoymamalı —
  `pywebview` zaten tarayıcıya düşüyor.

`requirements.txt` neyin kurulacağının tek kaynağı olarak kaldı; `_IMPORT_NAME`
sadece "kurulu mu" sorusunu nasıl soracağımızı söylüyor (`pywebview` → `webview`).
`run.bat` artık yalnızca Python'un kendisi hakkında rapor veremeyeceği iki şeyi
kontrol ediyor: var mı, ve 3.10+ mı.

### Kalıcı koruma

`tests/test_bootstrap.py`, **19 test**. Ağa ve pip'e dokunmuyor; her kurulum taklit,
denetlenen şey kurulumun etrafındaki karar. Bunu test etmenin sebebi tam olarak
çalışan bir makinede hiç koşmayan bir kod yolu olması: sadece sıfırdan bir PC'de
çalışıyor, kimsenin bakmadığı yerde, ve orada bir hata "uygulama açılmıyor" gibi
görünüyor. Kapsananlar: yorum satırlarının ayrıştırılması (isteğe bağlı blok
kurulum listesine sızarsa çevrimdışı ilk açılış çalışan uygulamayı bloklanmışa
çevirir), `pywebview` → `webview` eşlemesi (yanlışsa her açılış pywebview'i sonsuza
kadar yeniden kurar), proxy temizliği, ölümcül/ölümcül-olmayan ayrımı, ve pip'in
hiç olmaması.

### Uçtan uca doğrulama

Boş bir venv (`pip==25.3`, başka hiçbir şey yok) → `python -m app --no-window` →
yedi paketin hepsi kendiliğinden kuruldu → sunucu açıldı, `mappings:true`, arayüz
HTTP 200. **Kullanıcıya düşen adım: sıfır.**

Sonrasında tam paket: 192 test.

### Ayrıca

- `docs/V2_YONETICI_OZETI.md` — v2'de ne yapıldığının yönetici düzeyinde, teknik
  olmayan Türkçe özeti. Bakımcının talebi.
### Sürüm pinleme

Motorun dördü **tam pinli** (`==`), kabuğun üçü doğrulanmış sürümden tabanlı ve bir
sonraki majör'ün altında tavanlı (`>=x,<y`). Ayrım kasıtlı: motorun çıktısı işin
teslimatı, dolayısıyla APK'yı ayrıştıran kütüphanenin sessizce minör atlaması
kimsenin karar vermediği bir çıktı değişikliği demek. Kabuğun üçü yerel bir sayfa
sunuyor, çıktıya dokunmuyor; orada bir güvenlik yamasını corpus'u yeniden
çalıştırmadan alabilmek bayt düzeyinde tekrarlanabilirlikten değerli. Taban
gerçekten test edilmiş sürüm, "herhalde buraya kadar çalışır" tahmini değil.

Pin eklemek **`_missing()`'i sessizce bozuyordu**: satır hem pip'e giden şey hem de
import edilecek ad olarak kullanılıyordu, yani `find_spec("androguard==4.1.3")`
hiçbir zaman bulunamayacak bir modül arıyor ve **her açılışta tüm listeyi yeniden
kuruyordu**. `_requirement_name()` ayrımı yapıyor; `_FATAL` karşılaştırması da çıplak
ada göre yapılıyor, yoksa pinli bir `uvicorn` ölümcül sayılmayı bırakıyordu. Her
ikisi de teste bağlandı — `tests/test_bootstrap.py` artık **29 test**.

Boş venv'de doğrulandı: androguard bu sefer 4.1.4 değil **4.1.3** geldi.

### `.gitattributes` ölü kural taşıyordu

`src/data/reference/*` diyordu, oysa yol v2'de `engine/data/reference/` oldu. Yani o
`-text` / `-diff` / `binary` kuralları **v2 boyunca hiçbir dosyaya uygulanmadı**.
Düzeltmeden önce ölçüldü: hasar yok — blob ile çalışma ağacı bayt bayt aynı (ikisinde
de 80.837 CR), yani dönüşüm zaten olmuyordu. Düzeltmeden sonra `git check-attr` kuralı
görüyor ve hiçbir dosya "değişmiş" görünmüyor. **Düzeltildi.**

## 2026-09-24 — coverage artık OHPM eşleşmelerini de sayıyor

İki uygulama (botim `im.thebot.messenger` 4.17.0, SHEIN `com.zzkko` 15.4.2)
indirilip batch olarak koşuldu; çıktı `24-9/` altında (git'e eklenmedi). İkisi de
APKPure'dan App Bundle olarak geldi, `base.apk` analiz edildi.

**Bakımcı kararı — çıktıyı değiştiren değişiklik.** Coverage eskiden
`kit'e eşlenen / (kit + eşlenmeyen + OHPM)` idi: OHPM paydadaydı ama payda değildi,
yani HarmonyOS portu olan bir kütüphane "karşılığı yok" ile aynı sayılıyordu.
Yeni formül `(kit + OHPM) / (kit + eşlenmeyen + OHPM)`. Payda değişmedi.

- Motor `total_ohpm_ns` alanını yazıyor (`apk_engine.py`); `coverage_status()` payına
  ekliyor. Alan beş besleme noktasına taşındı: `report_data`, `run_batch` satırı,
  worker side-car'ı, `aggregate.py`, index'in rapordan okuyan regex'i.
- Alanı taşımayan eski raporlar 0 kabul ediliyor → yayımlandıkları oran korunuyor,
  rescan onları sessizce yeniden puanlamıyor.
- Etki bu iki uygulamada küçük: botim %84,1 → %84,4, SHEIN %64,2 → %65,6.
- +3 test (store ×2, aggregate ×1): 207 → 210.
