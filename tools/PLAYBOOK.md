# Frame Lab üretim kılavuzu

Frame Lab, Ece Duru'nun yüzsüz Türkçe Instagram hesabı: **@frame.labo**. Konular yapay zekâ, tasarım, video ve sosyal medya. Ton sıcak, net, hafif esprili ve pratik. Her içerik bir şey dener ya da öğretir: "Haber değil, deney."

## Hesaplar ve yayın
- Instagram yayını Windsor MCP üzerinden yapılır: connector `instagram`, account `17841469889313843`.
- Medya bu depoda durur. Instagram'a **mutlaka raw adres** verilir: `https://raw.githubusercontent.com/framelabed-ux/frame-lab-media/main/<yol>`. GitHub Pages adresi görsellerde "media type" hatası verdi. Video raw adresiyle hata verirse bir kez `https://framelabed-ux.github.io/frame-lab-media/<yol>` denenir.
- Görseller JPEG olmalı. Carousel ve feed 1080x1350 (4:5), story ve Reel 1080x1920.
- Depoya push etmeden önce `git fetch origin main` ve rebase. Commit mesajı Türkçe ve kısa.

## Marka
- Renkler: Mürekkep #111114, Kâğıt #F5F4F0, Lab Yeşili #B8F24A (yalnızca vurgu ve Kare), yumuşak yeşil zemin #EEF6DE. **Mor zemin yok.** Ece istemedi. Morun tek kullanım yeri Kare'nin anten topu.
- Fontlar: başlık Inter Display (800), metin Inter.
- Maskot Kare'nin yüzleri: mutlu, goz (ipucu), saskin, dusunen, fikir (sonuç), calisiyor (AI üretirken).
- Tamamen fosforlu yeşil zemin kullanılmaz. Ece göz yorduğunu söyledi.
- Üretim için `python3 tools/render.py` (carousel, story, reel). Spec örnekleri `tools/examples/` içinde. Vurgu için metinde `[[kelime]]` yazılır.

## Gündem kaynakları: kaçırılmaması gerekenler
Genel arama tek başına yetmez (10 Kasım'da Claude Fable 5.2 duyurusu sabah taramasında kaçtı). Her taramada şu kaynaklar **tek tek** kontrol edilir, son 48 saatte yeni bir duyuru var mı diye:
- **Yapay zekâ şirketleri:** Anthropic (anthropic.com/news, @claudeai), OpenAI (openai.com/news), Google (blog.google, deepmind.google), Meta AI (ai.meta.com/blog), xAI, Mistral, Microsoft (Copilot), Apple.
- **Görsel ve video yapay zekâsı:** Midjourney, Runway, Pika, Luma, Kling, ElevenLabs, Stability, Black Forest Labs (Flux), Ideogram.
- **Tasarım araçları:** Adobe (blog.adobe.com, Firefly), Canva (canva.com/newsroom), Figma (figma.com/blog), CapCut.
- **Platformlar:** Instagram (about.instagram.com, @mosseri), Meta newsroom, TikTok newsroom, YouTube blog / Creator Insider, Threads, LinkedIn.
- **Teknoloji medyası:** TechCrunch AI, The Verge AI, Engadget, Social Media Today (platform haberleri için).
Arama ipucu: şirket adı + "announces", "launches", "introducing", "new model", "update" ve bugünün ya da dünün tarihi. "extended" modu kullan.

**Büyük gelişme ölçütü:** Yeni bir ana model sürümü (GPT, Claude, Gemini, Llama, Grok gibi), Instagram/TikTok/YouTube'da içerik üreticileri doğrudan etkileyen bir özellik, Adobe/Canva/Figma'da büyük bir yapay zekâ özelliği ya da viral bir dijital trend. Bunlar o günün feed konusu olur ve mümkünse aynı gün işlenir.

**Kapsanan konular:** İşlenen her gündem konusu `state.json` içindeki `covered_topics` listesine kısa bir anahtarla yazılır (ör. "claude-fable-5-2"). Aynı konu iki kez işlenmez, ama önemli bir devamı varsa "güncelleme" olarak işlenebilir.

## Tasarım çeşitliliği (Ece: "tasarımlar birbirine aşırı benziyor")
Marka aynı kalır (renkler, fontlar, Kare), ama düzen her seferinde değişir. Kalıp tekrarı yasak.
- Düzen aileleri (spec örnekleri `tools/examples/layout-*.json`):
  - **bignum:** dev rakam ya da istatistik + kısa etiket (sayı içeren her şey: "20 prompt", "3 adım", "%40").
  - **chat:** prompt ve sonuç sohbet balonu olarak (prompt içerikleri için ideal).
  - **phone:** kenardan giren telefon ekranı (uygulama, platform ve araç haberleri).
  - **compare:** iki sütun, kötü/iyi ya da önce/sonra.
  - **steps:** büyük, içi boş numaralı adımlar.
  - **quote:** ortalanmış büyük cümle, vizör çerçevesi (`"frame": true`) ve `"align": "center"` ile.
  - **tiles:** 2x2 kutular (4 madde, 4 araç).
  - **classic:** Kare + etiket + başlık + açıklama (eski kalıp, artık nadiren).
- Süsleme seçenekleri: `"pattern": "grid"` (laboratuvar kareli zemin) ya da `"dots"`, `sticker` (yuvarlak, eğik etiket: ÜCRETSİZ, YENİ, DENEDİK), `kare_peek` (kenardan bakan büyük Kare), başlıkta `"outline": true` (içi boş yazı), `"narrow": true` (yan tarafta telefon ya da Kare varken metni daraltır).
- Kurallar:
  1. Art arda iki feed gönderisinin kapağı aynı düzen ailesinden olamaz. Kullanılan düzen `grid` kaydına `layout` olarak yazılır.
  2. Bir carousel en az 3 farklı düzen ailesi içerir, ardışık iki slayt aynı düzende olamaz.
  3. Kare her slaytta olmaz: carousel başına en fazla 2 kez, farklı boyut ve konumda (büyük, kenardan bakan, küçük köşe).
  4. Kareli/noktalı zemin ve vizör çerçevesi gönderi başına en fazla bir iki slaytta, abartmadan.
  5. Başlık boyutu, hizalama (üst, orta, alt) ve metin yoğunluğu slayttan slayta değişir.
  6. **Kısa tut (Ece: "carouseller çok uzun olursa insanlar sıkılır").** Carousel ideal 5 slayt, en fazla 6 (kapak ve son slayt dahil). Her slaytta tek fikir. Teknik ayrıntıyı, künyeyi ve ek rakamları slayta değil caption'a koy. Son slayt hem dersi hem yorum sorusunu taşır, ayrı bir "soru slaytı" açma. Reel de kısa olsun: ideal 20–35 saniye, outro dahil en fazla 45 saniye.
  6. Story'ler de aynı ailelerden seçilir, aynı günün feed kapağıyla aynı düzende olmaz.

## Izgara düzeni (puzzle)
- Profil ızgarası satranç tahtası gibi görünmeli: her feed gönderisinin kapağı bir öncekinin tersi olmalı. Açık (light veya soft) ve koyu (dark) sırayla gider.
- Son kapak tonu `posts/state.json` içindeki `grid` listesinin son öğesinde yazar. Yeni gönderinin kapak tonu bunun tersi seçilir.
- Reel kapağı `cover_url` ile ayrıca verilir. Kapak 1080x1920 olur, ama ızgarada ortadaki 3:4 alan görünür. Önemli metin dikeyde 300–1600 piksel arasında kalmalı.
- Carousel içinde kareler açık ve koyu sırayla gider, böylece kaydırırken ritim oluşur.

## Format sırası (feed, her hafta içi günü 1 gönderi, saat 19:30 civarı)
Format haftanın gününe bağlı değil, sırayla döner: **Reel → statik → carousel → Reel → statik → carousel …**
- Bugünün formatı = `posts/state.json` içindeki `grid` listesinin son öğesinin `kind` değerinden bir sonraki format. (Son reel ise statik, son statik ise carousel, son carousel ise Reel.)
- Ece statik ile carousel'in yeri değişebilir dedi. Gündem gerektiriyorsa (ör. tek görsele sığmayan bir karşılaştırma) o gün statik yerine carousel, ertesi gün statik yapılabilir. Yeter ki üç format sırayla dönsün ve aynı format art arda gelmesin.
- Hafta sonu feed gönderisi yok, sadece story var. Sıra pazartesi kaldığı yerden devam eder.

Formata göre seriler:
| Format | Seriler |
| --- | --- |
| Reel | Sıcak Gelişme (gündemde büyük bir şey varsa), Kare Açıklıyor (bir kavramı 30–40 saniyede anlatır) |
| Carousel | Bu Hafta Dijitalde (haftanın ilk carousel'i, haftanın en önemli 3–4 gelişmesi), 1 Prompt 3 Sonuç (karşılaştırma), Mutfaktan (sosyal medya taktikleri), Kare'den Haberler (numaralı seri: 1–3 doğrulanmış gelişme, her biri için ne oldu, nasıl çalışır, sana ne faydası var; Ece 10 Kasım'da başlattı) |
| Statik (tek görsel) | Günün Prompt'u (kopyalanacak hazır prompt), Tasarım Kuralı (tek kural, tek örnek) |

İçeriklerin yaklaşık %60'ı gündemden gelir. Büyük bir gelişme o günün formatına uyarlanır: Reel günü kısa deneme videosu, carousel günü adım adım anlatım, statik günü tek karede "bunu bilmen lazım" kartı.

Statik gönderi: tek slaytlı carousel spec'iyle `render.py carousel` (1080x1350), yayın `create_image_post`. Metin tek bakışta okunmalı: bir başlık ve en fazla 3–4 kısa satır ya da bir prompt kartı.

## Önceden hazırlanmış gönderiler
`queue` içinde bugünün tarihli bir öğe zaten varsa (Ece ile birlikte önceden hazırlanmış), sabah görevi o gün yeni feed gönderisi üretmez. Sadece o gönderiyi duyuran story'yi yapar ve raporda bunu belirtir. Format sırası ve kapak tonu bu öğeye göre devam eder.

## Prompt rehberi ve link
- Ücretsiz rehber: https://framelabed-ux.github.io/frame-lab-media/rehber/ (kaynak: `rehber/index.html`). Biyografi linki ana sayfa: https://framelabed-ux.github.io/frame-lab-media/
- Uygun gönderilerde "Rehber ücretsiz, linki profilde" diye hatırlatılabilir, ama her gönderide değil (en fazla haftada 2 kez).

## Yorumlara yanıt (akşam görevi, her gün)
- Son 7 günün gönderilerindeki yanıtlanmamış yorumlar Windsor'dan okunur (`comment_id`, `comment_text`, `media_id`, `comment_timestamp`). Hesabın kendi yorumları atlanır.
- Gerçek yorumlara 1–2 cümlelik, kişisel, sıcak bir yanıt verilir (`reply_to_comment`). Yorumdaki ayrıntıya değinilir. Kopyala-yapıştır kalıp kullanılmaz. Soru varsa somut cevap verilir. "Caption / görsel / video" gibi bir ihtiyaç yazılmışsa rehberden uygun prompt'un adı ve tek cümlelik özeti önerilir.
- Emoji en fazla 1. Link yazılmaz, gerekirse "linki profilde" denir.
- Spam, reklam, hakaret ya da dolandırıcılık içeren yorumlar gizlenir (`hide_comment`), silinmez ve yanıtlanmaz.
- Tartışmalı ya da hassas bir yorumda (şikâyet, hukuki ya da kişisel konu) yanıt verilmez, Ece'ye bildirilir.
- Aynı yoruma iki kez yanıt verilmez. Yanıtlanan comment_id'ler `state.json` içindeki `replied_comments` listesine yazılır.

## Story (her gün 1 tane, sabah yayınlanır)
Story o akşamki gönderinin merak uyandıran bir duyurusu, günün kısa bir ipucu ya da bir soru olabilir ("Yorumlara yaz" yerine "DM'den yaz"). 1080x1920 JPEG. Story'de saat yazma, "Bu akşam profilde" de.

Öne çıkanlar (Ece uygulamadan ekliyor, API desteklemiyor): Başla, Gündem, AI Lab, Tasarım, Mutfak. Sabah raporunda o günün story'sinin hangi öne çıkana eklenebileceğini öner. Kalıcı değeri olan story'ler (ipucu, formül, gündem özeti) öne çıkana uygundur, akşam duyuruları değildir.

## Hareketli Reel (varsayılan)
Ece Reel'lerin daha hareketli olmasını, Kare'nin sayfalar arasında gezmesini istedi. Tüm Reel'ler **motion modunda** üretilir (örnek: `tools/examples/reel-motion.json`):
- Spec'e `"motion": true` eklenir. Sahneler yan yana bir şerit olur ve her geçişte sayfa sola kayar.
- Kare sahnelere öğe olarak eklenmez. Her sahneye `"kare": {"x":…, "y":…, "size":…, "face":…}` yazılır, Kare geçişlerde bir sonraki konuma zıplar, sahnede hafifçe süzülür ve göz kırpar.
- Kare'nin konumu metinle çakışmamalı: boş alanlara yerleştir, sahneden sahneye köşe, boyut ve ifade değişsin. `"kare": null` olursa Kare o sahnede görünmez.
- `bignum` öğesine `"count_at": 0.3` eklenirse rakam sıfırdan sayarak gelir.
- Her Reel'in sonuna otomatik olarak 3,2 saniyelik logo outro'su eklenir: FL çizilerek belirir, yeşil nokta oturur, FRAME/LAB, slogan, "Takip et" ve @frame.labo gelir. Kare son sahneden yukarı zıplayıp çıkar. Kapatmak için spec'e `"outro": false`. Toplam süre hesaplanırken outro'yu da say.
- `"stills": [saniye, …]` ile kontrol kareleri üretilir. Her sahnenin sonundan bir kare alıp Read ile bakılır, çakışma varsa konum düzeltilir. Kapak için ilk sahnenin dolu anındaki kare (`*_still_*.jpg`) kullanılabilir.

## Seslendirme
Otomatik çalışmada yapay ses aracı yok. Reel'ler ekran yazısı ve müzikle (`tools/music.py`, otomatik) üretilir. Ece ses dosyası gönderirse spec'e `voice_segments` eklenip `render.py reel spec out voice` ile kullanılır. Yazılar, sessiz izleyen biri de anlayacak kadar okunur süre ekranda kalmalı: kelime başına en az 0,35 saniye.

## Kalite kontrol (her içerikte, yayından önce)
1. **Doğruluk:** Her gündem iddiası birincil ya da saygın bir kaynakta açılıp doğrulanmış olmalı (resmî blog, büyük teknoloji medyası). Doğrulanamayan hiçbir şey yazılmaz. Sürüm, tarih, fiyat uydurulmaz. Emin olunmayan ifade çıkarılır.
2. **Mantık:** Başlık ile içerik, prompt ile sonuç, sayılar ile anlatım tutarlı mı? "3 deneme" diyorsa 3 tane mi? Kendini çürüten ya da abartılı vaat ("bedava, sınırsız") var mı?
3. **Yazım:** Türkçe imla (ı/i, ş, ğ, ç, ö, ü, şapkalı â), birleşik ve ayrı yazılanlar (de/da, ki, mi), noktalama, büyük harf. Görseldeki her metin ve caption satır satır tekrar okunur.
4. **Görsel kontrol:** Üretilen her JPEG ve Reel'den en dolu anın karesi Read ile açılıp bakılır. Taşma, kesilme, üst üste binme, okunaksız kontrast olmamalı.
5. **Etkileşim:** İlk satırda güçlü bir kanca olmalı. Kaydetmeye değer somut bir bilgi bulunmalı (formül, adım, karşılaştırma). Sonda yoruma çağıran net bir soru olmalı. 5–8 Türkçe hashtag. Caption en fazla 2200 karakter.
6. Herhangi bir adımda şüphe varsa içerik yayınlanmaz, Ece'ye sorulur.

## Durum dosyası: posts/state.json
- `grid`: yayınlanan feed gönderileri (tarih, tür, kapak tonu, slug, media_id).
- `queue`: sabah üretilip akşam yayınlanacaklar. Her öğe: slug, kind (carousel/reel/static), publish_date, files, cover, cover_tone, caption, sources.
- `stories`: yayınlanan story kayıtları.

## Reklam Lab serisi (Ece: "yapay zekâ sunucu olmasın, marka reklamlarına haber şeklinde yer verelim")
- Amaç: hesaba insan yüzü ve marka hikâyesi katmak. Konu: reklamcılıkta yapay zekâ, dikkat çeken yeni kampanyalar, ajans araçları, tartışmalı reklamlar. Haftada en fazla 1 kez, carousel ya da Reel olarak.
- Başlık haber dilinde ve kancalı olsun ("Ünlüler artık reklam çekimine bir kez gidecek."). Kapakta tag "REKLAM LAB · <bölüm no>".
- Son slaytlarda mutlaka "küçük marka / serbest çalışan ne öğrenir?" dersi ve yorum sorusu olsun.
- Görseller:
  - Ünlülerin ya da kamuya mal olmuş kişilerin fotoğraflarını tasarıma KOYMA. İsimleri metinde geçebilir.
  - Reklamdan kare gerekiyorsa yalnızca masaüstü uygulamasındaki tarayıcıyla (bağlıysa) ekran görüntüsü al. Az kare kullan (en fazla 2–3), ürünü, mekânı ya da tanınmış olmayan oyuncuları gösteren kareleri seç. Markayı ve ajansı künye olarak yaz, yorum ekle, reklamın tamamını ya da müziğini kullanma. Resmî basın görselleri önceliklidir.
  - Tarayıcı bağlı değilse görselsiz düzenlerle (bignum, steps, tiles, compare, chat) hazırla.
- Rakamları en az iki kaynaktan doğrula. Doğrulanamayan istatistiği kullanma.
- Görsel öğeleri (render.py):
  - `{"type":"photo_bg","src":"posts/<slug>/src/x.jpg","height":780,"pos":"center 0%","credit":"Görsel: Marka / Ajans"}` tam genişlik, alta doğru zemine erir. Slayta `"align":"bottom"` ver.
  - `{"type":"photo","src":...,"height":520,"credit":...}` yuvarlatılmış görsel kartı.
  - Sticker'ın yeri `"top"` ile ayarlanır; künyenin ve görseldeki önemli yerlerin üstüne gelmesin.
- Ekran görüntüsüyle yüksek çözünürlüklü görsel alma: tarayıcı ekran görüntüsü en fazla 800 px genişlikte geliyor. Görseli sayfada sabit bir katmanda büyütüp (ör. 2400 px) parça parça ekran görüntüsü al, sonra PIL ile birleştir. Görseller posts/<slug>/src/ altında dursun.
- Bölüm 1: Ogilvy ECHO (11 Kasım). Kapakta Ogilvy'nin resmî ECHO illüstrasyonu.
