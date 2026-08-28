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
