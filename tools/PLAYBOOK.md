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
  - **bars:** yatay çubuk karşılaştırması (iki–dört değer, biri vurgulu).
  - **ring:** yüzde halkası + kısa etiket (tek bir oran).
  - **editorial:** ortalı ince başlık + italik serif vurgu + kahraman görsel (aşağıdaki "Editoryal stil" bölümü; kapaklar için varsayılan).
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

## Izgara sütun sistemi (Ece onayladı, 13 Kasım)
Profil 3 sütun. Kapaklar şu 3'lü döngüyü sırayla izler: **görsel → tipografi → Kare → görsel → …** Her yeni gönderi ızgarayı bir kare kaydırsa da her sütun tek türde kalır; açık/koyu dama tahtası da (tonu her gönderide değiştirerek) korunur.
- **görsel:** kapağın çoğunu büyük bir nesne/fotoğraf kaplar (kronometre, cam halka, telefon, marka basın görseli…), üstünde en fazla 5 kelime.
- **tipografi:** tek bir dev rakam ya da 2–3 kelime; başka öğe yok ya da çok az.
- **Kare:** maskot büyük ve net görünür (en az kapağın üçte biri), yanında kısa soru/başlık.
- Bugünün kapak türü: `grid` ve `queue` içindeki son kaydın `cover_type` alanına bak, döngüde bir sonrakini seç. Kaydı yazarken `"cover_type"` alanını mutlaka doldur. (13 Kasım Gemini 4 Hydrogen = tipografi; sıradaki = Kare.)
- **Kapakta en fazla 5 kelime.** Ayrıntı içeride ve açıklama metninde.
- "YENİ" etiketi en fazla 9 gönderide bir. Aynı vurgu kalıbını (yeşil kutu) art arda iki kapakta kullanma.
- Renk ve tipografi dili Ece'nin seçeceği yöne göre güncellenecek (13 Kasım'da 3 yön sunuldu: A Deney Raporu, B Vizör, C Renk Blokları). Seçim gelene kadar mevcut editoryal stil sürer.

## Editoryal stil (Ece, 11 Kasım: "çok aynı tip gidiyoruz"; Behance'ten ajans işleri örnek gösterdi)
Kapaklarda ve tek görsellerde varsayılan görünüm budur: ortalı kurgu, ince başlık + italik serif vurgu, ışıklı zemin ve altta büyük bir "kahraman" görsel. Örnekler: `tools/examples/editorial.json` (4 gönderi) ve `tools/examples/reel-editorial.json`. Örnek gösterilen işler yalnızca yön içindir; hiçbirinin kurgusunu, nesnesini ya da metnini kopyalama.
- Slayt/sahne seçenekleri: `"bg": "glow"` (ışıklı degrade zemin), `"pattern": "rings"` (ince halkalar), `"logo": "center"` (üstte ortalı logo), `"align": "center top"`.
- Başlık: `{"type":"h1","light":true,"size":104,"text":"Videonun kaderi\n{{ilk 3 saniyede}}\nbelli olur."}`. `{{...}}` italik serif (koyu temada yeşil), `[[{{...}}]]` yeşil kutu içinde italik serif (açık temada), `**...**` kalın. Başlığın üstüne kısa bir `lead` (üst satır), altına tek cümlelik `lead` gelir.
- `{"type":"pill","outline":true,"text":"Açıklamayı oku"}` ince çerçeveli hap.
- `{"type":"hero","src":"brand/stock/x.jpg","x":200,"y":837,"w":900,"h":513,"blend":"lighten"}` kahraman görsel. Siyah zeminli görsel koyu temada `"blend":"lighten"` ile zemine karışır; beyaz zeminli görsel açık temada `"blend":"multiply"`. `"gray": true` renkleri alır, `"tint": true` yeşile boyar, `"cover": true` kutuyu doldurur, `"mask": "top"|"bottom"|"radial"` kenarı eritir. Görsel alt kenardan taşabilir; alttaki yazıyla çakışıyorsa slayta `"foot_right": ""`, Reel sahnesine `"nofoot": true` yaz.
- `{"type":"burst","x":700,"y":742,"size":310,"rot":12}` yeşil dört uçlu parıltı (`"shape":"sun"` ışınlı). Görselin arkasına ya da boşluğa, slayt başına en fazla iki tane.
- `{"type":"note","text":"**Rakamla** aç.\nMerak uyandır.","x":90,"y":900,"w":340,"rot":-6}` yırtık kâğıt notu; en fazla iki kısa satır, görselin kenarına biner ama yazıyı kapatmaz.
- `{"type":"phone","center":true,"title":"…","blocks":[…],"accent":3,"bottom":-470}` ortada alttan yükselen telefon (açık temada kahraman görsel yerine).
- Hazır görseller `brand/stock/` içinde: `kronometre.jpg` (zaman, hız), `cam-halka.jpg` (döngü, süreç), `dalga-koyu.jpg` (soyut zemin, `tint` ile). Aynı görseli iki hafta içinde ikinci kez kapakta kullanma.
- Yeni görsel gerekirse yalnızca masaüstü uygulamasındaki tarayıcı bağlıyken, Unsplash'in ücretsiz lisanslı fotoğraflarından ekran görüntüsüyle alınır (Unsplash+ değil). Marka logosu, tanınabilir ürün markası ve ünlü yüzü içeren görsel kullanılmaz; logolu kısım kadraj dışında bırakılır. Tarayıcı bağlı değilse hazır görseller ya da telefon/grafik öğeleri kullanılır.
- Bu stil eski düzen aileleriyle karışık kullanılır: carousel'de kapak editoryal, iç slaytlar steps/bars/ring/compare/chat olabilir. Izgarada açık/koyu sırası aynen geçerli.

## Izgara düzeni (puzzle)
- Profil ızgarası satranç tahtası gibi görünmeli: her feed gönderisinin kapağı bir öncekinin tersi olmalı. Açık (light veya soft) ve koyu (dark) sırayla gider.
- Son kapak tonu `posts/state.json` içindeki `grid` listesinin son öğesinde yazar. Yeni gönderinin kapak tonu bunun tersi seçilir.
- Reel kapağı `cover_url` ile ayrıca verilir. Kapak 1080x1920 olur, ama ızgarada ortadaki 3:4 alan görünür. Önemli metin dikeyde 300–1600 piksel arasında kalmalı.
- Carousel içinde kareler açık ve koyu sırayla gider, böylece kaydırırken ritim oluşur.

## Format sırası (feed, her hafta içi günü 1 gönderi, saat 19:30 civarı)
Format haftanın gününe bağlı değil, sırayla döner. **10 Kasım'dan itibaren Reel ağırlıklı (Ece onayladı):** **Reel → Reel → carousel ya da statik → Reel → Reel → carousel ya da statik …**
- Neden: Hesap küçükken carousel'ler 2–4 kişiye, Reel'ler takip etmeyenlere ulaşıyor (Fable 5.2 Reel'i 3 takipçiyle 1.140 hesaba ulaştı, 9 kaydetme aldı). Takipçi sayısı birkaç yüze çıkınca bu oranı yeniden değerlendirip Ece'ye sor.
- Bugünün formatı: `grid` listesinin son iki öğesine bak. Son iki öğe Reel ise carousel ya da statik yap (bir önceki carousel ise statik, statik ise carousel). Aksi hâlde Reel yap.
- Büyük gündem gelişmesi her zaman Reel olur. O gün carousel/statik sırasıysa bile Reel yapılabilir, carousel/statik ertesi güne kayar.
- **İlk ay sayıyı artırıyoruz (Ece 10 Kasım'da onayladı, ~10 Aralık'a kadar; sonra verilere bakıp Ece'ye sor):**
  - Hafta sonu da her gün 1 Reel paylaşılır: gündemden bağımsız "Kare Açıklıyor" serisi (bir yapay zekâ, tasarım ya da sosyal medya kavramı, 20–35 saniye). Sabah görevi üretir, akşam görevi yayınlar.
  - Büyük, doğrulanmış bir gündem gelişmesi olursa öğle görevi aynı gün ek bir Reel üretip hemen yayınlar. Akşamki planlı gönderi yine çıkar.
  - Hafta sonu Reel'leri ve öğle ek Reel'leri grid kaydında `"extra": true` ile işaretlenir ve hafta içi format sırası hesaplanırken atlanır. Izgaradaki açık/koyu kapak sırasına ise dahildir.
  - Günde ikiden fazla feed gönderisi yok. Story günde 1 kalır.

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

## Yorumlara yanıt (ONAYLI: Ece 10 Kasım'da "bana sormadan cevap verme" dedi)
- **Hiçbir yoruma Ece'nin onayı olmadan cevap verilmez, hiçbir yorum gizlenmez ya da silinmez.** Bu kural her görev için geçerlidir.
- Akşam görevi son 7 günün yanıtlanmamış yorumlarını Windsor'dan okur (`comment_id`, `comment_text`, `comment_username` varsa, `media_id`, `comment_timestamp`). Hesabın kendi yorumları ve `replied_comments` / `pending_replies` içindekiler atlanır.
- Her yorum için bir yanıt TASLAĞI yazılır: 1–2 cümle, kişisel, sıcak, yorumdaki ayrıntıya değinen, Türkçe, en fazla 1 emoji, link yok. Eleştiri ya da şikâyet içeren yorumlarda savunmaya geçme, abartılı övgüye de kayma; kısa, dürüst ve saygılı ol. Spam gibi görünenler için "gizleyelim mi?" diye sorulur.
- Taslaklar `state.json` içindeki `pending_replies` listesine yazılır (comment_id, media_id, yorum metni, taslak) ve Ece'ye numaralı liste olarak gönderilir: "1) Yorum: … → Taslak: …". Ece'den "1 onay", "2'yi şöyle değiştir", "3 cevap verme" gibi bir yanıt istenir.
- Ece aynı konuşmada onay verirse yalnızca onaylanan yanıtlar, Ece'nin son hâliyle birebir gönderilir (`reply_to_comment`). Onay gelmezse hiçbir şey gönderilmez, taslaklar bekler. Gönderilenler `pending_replies`'tan çıkarılıp `replied_comments`'e yazılır. Ece bir yoruma "cevap verme" derse comment_id `replied_comments`'e yazılır, böylece tekrar sorulmaz.
- **Anahtar kelimeli yorumlar (ör. REHBER):** DM'leri Ece elle atıyor. Görev sonunda DM atılacak kişileri (kullanıcı adı ya da yorum metni ve gönderi) Ece'ye listeler. Bu yorumlara da onaysız açık yanıt yazılmaz. 50 takipçiye ulaşılınca Ece'ye ReplyRush kurulumunu hatırlat.
- Yorumdan DM'e çağrı (CTA) yalnızca gerçekten gönderilecek bir kaynak varsa kullanılır (şimdilik prompt rehberi: https://framelabed-ux.github.io/frame-lab-media/rehber/). Haftada en fazla 2 gönderide.

## Story (her gün 1 tane, sabah yayınlanır)
Story o akşamki gönderinin merak uyandıran bir duyurusu, günün kısa bir ipucu ya da bir soru olabilir ("Yorumlara yaz" yerine "DM'den yaz"). 1080x1920 JPEG. Story'de saat yazma, "Bu akşam profilde" de.

Öne çıkanlar (Ece uygulamadan ekliyor, API desteklemiyor): Başla, Gündem, AI Lab, Tasarım, Mutfak. Sabah raporunda o günün story'sinin hangi öne çıkana eklenebileceğini öner. Kalıcı değeri olan story'ler (ipucu, formül, gündem özeti) öne çıkana uygundur, akşam duyuruları değildir.

## Hareketli Reel (varsayılan)
Ece Reel'lerin daha hareketli olmasını, Kare'nin sayfalar arasında gezmesini istedi. Tüm Reel'ler **motion modunda** üretilir. Örnekler: `tools/examples/reel-motion.json` (haber kurgusu) ve `tools/examples/reel-styles.json` (grafik öğeleri).
- Spec'e `"motion": true` eklenir. Her öğeye `"at"` (sahne başından saniye) yazılır; `at` olmayan öğe animasyonsuz, baştan görünür.
- **Sahne geçişleri:** Sahneye `"transition"` yazılabilir: `slide` (yana kayar), `up` (yukarı kayar), `stack` (yeni sayfa kart gibi üste biner), `zoom` (içinden geçer), `wipe` (yeşil renk perdesi). Yazılmazsa bu sırayla kendiliğinden döner, outro'ya renk perdesiyle geçilir. Aynı geçişi art arda kullanma.
- **Yazı ve öğe animasyonları otomatiktir:** h1/h2/quote kelime kelime gelir, `[[vurgu]]` sonradan süpürülerek boyanır, tag harf aralığı daralarak gelir, tiles/steps/rows/chips/chat/compare çocukları sırayla girer (chat için `"gap"` ile balon aralığı ayarlanır, varsayılan 0,6 sn), bignum ve pill yaylanarak büyür, sticker dönerek oturur. Zemin deseni yavaşça kayar, sahne çok hafif yaklaşır.
- **Grafik öğeleri (Reel'de animasyonlu, carousel/statikte sabit):**
  - `{"type":"bars","items":[["Reel",1140,"1.140"],["Carousel",4,"4"]],"accent":0,"at":0.7}` yatay çubuk karşılaştırması; çubuklar dolar, sayılar sayarak gelir. `"max"` ile tam genişlik değeri verilebilir.
  - `{"type":"ring","value":58,"text":"%58","size":600,"label":"ilk 3 saniyede [[geçti.]]","at":0.3}` yüzde halkası (value 0–100).
  - `{"type":"marquee","text":"REEL MI CAROUSEL MI","top":1420}` arka planda akan dev yazı şeridi; yalnızca Reel'de, sahne başına en fazla bir tane, metnin üstüne gelmesin.
  - `bignum` öğesine `"count_at": 0.3` eklenirse rakam sıfırdan sayarak gelir ("1.140" gibi binlik ayraçlı sayılar da sayar).
- **Kare:** sahnelere öğe olarak eklenmez. Her sahneye `"kare": {"x":…, "y":…, "size":…, "face":…}` yazılır; Kare geçişlerde bir sonraki konuma zıplar (zoom ve wipe geçişlerinde takla atar), sahnede süzülür ve göz kırpar. Konumu metinle çakışmamalı; sahneden sahneye köşe, boyut ve ifade değişsin. `"kare": null` olursa o sahnede görünmez.
- **İlerleme çubuğu:** üstte sahne sayısı kadar parçalı ince çubuk otomatik gelir (izleyene videonun kısa olduğunu gösterir). Kapatmak için spec'e `"progress": false`. Üstteki ilk 100 pikselde öğe olmasın.
- **Müzik (Ece, 11 Kasım: "her videonun müziği aynı olmasın"):** Spec'e `"music": {"style": "...", "seed": <sayı>}` yaz. Stiller: `pop`, `lofi`, `house`, `synthwave`, `minimal`, `trap`, `funk`, `ambient`. Son 3 Reel'in stilini `grid` kayıtlarındaki `music` alanından oku ve onlardan farklı birini seç; tohumu da her seferinde değiştir (aynı stil + farklı tohum = farklı ton, tempo ve melodi). Konuya göre seç: haber/teknoloji → synthwave, house, minimal; sakin/iş → lofi, ambient; eğlenceli → funk, pop; dramatik → trap. Seslendirmeli videolarda lofi, ambient, minimal daha iyi oturur. Seçilen stili kuyruk kaydına `"music"` olarak yaz.
- **Ses efektleri:** geçişlerde hafif "whoosh", ana öğe girerken "pop", logoda "ding" otomatik eklenir ve müzikle karışır. Kapatmak için `"sfx": false`.
- Her Reel'in sonuna otomatik olarak 3,2 saniyelik logo outro'su eklenir. Kapatmak için `"outro": false`. Toplam süre hesaplanırken outro'yu da say.
- `"stills": [saniye, …]` ile kontrol kareleri üretilir. Her sahnenin dolu anından ve en az bir geçiş anından kare alıp Read ile bak; çakışma, taşma ya da Kare'nin yazıyı kapatması varsa düzelt. Kapak için ilk sahnenin dolu anındaki kare (`*_still_*.jpg`) kullanılabilir.
- **Reel kapağı:** ilk sahnenin öğelerini `at` olmadan, `"align": "center"` ve `"nofoot": true` ile `render.py story` modunda ayrı render et (örnek: `posts/2026-11-11-adobe-max-creative-agent/cover.json`). Başlık, ızgaradaki 3:4 kırpmaya (üstten 240, alttan 240 piksel kesilir) sığmalı.
- **İlk sahne boş açılmasın:** ilk sahnede tag `"at": 0`, başlık `"at": 0.05` olsun; alt yazı en geç 0,8'de gelsin.
- **Açılış kancası:** Ortalama izleyici ilk 3 saniyede karar veriyor (Fable Reel'inde %58'i ilk 3 saniyede geçti). İlk sahne 0,5 saniye içinde dolu olmalı, rakamlı ya da merak uyandıran tek bir cümleyle açılmalı ("Claude artık %30 daha hızlı.", "Bu reklamda oyuncu hiç sete gelmedi."). Logo, selamlaşma, "bugün sana … anlatacağım" ile açma.
- **Süre:** İdeal 20–35 saniye, outro dahil en fazla 45 saniye. Fable Reel'inde ortalama izlenme 12 saniyeydi, asıl bilgi ilk 10 saniyede verilmeli.

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

## Büyüme ve gelir (Ece, 11 Kasım: "global örneklere bak, sürekli kendini güncelle, az enerji harcatmalı, çok iyi olmalı, etkileşim almalı, para kazandırmalı")
**Ölçtüğümüz şey:** Instagram'ın başı Adam Mosseri'nin 2026'da en önemli dediği sinyaller izlenme süresi, erişim başına DM ile gönderim (sends) ve erişim başına beğeni; kaydetme de beğeniden ağır sayılıyor. Takipçi olmayanlara ulaşmada en güçlü sinyal gönderimler. Bu yüzden:
- Her içerik "biri bunu bir arkadaşına gönderir mi?" testinden geçer. Gönderilme sebebi olsun: işe yarayan bir ipucu, ekibe iletilecek bir haber, "tam senlik" diyeceği bir durum.
- CTA'ları dönüşümlü kullan: yorum sorusu, "Bunu ekibine/ihtiyacı olan birine gönder", "Kaydet, lazım olur". Aynı CTA art arda iki gönderide olmasın.
- Haftalık rapordaki ana metrikler: izlenme, erişim, ortalama izlenme süresi, ilk 3 saniyede geçme oranı, kaydetme/erişim, paylaşım/erişim, takipçi artışı.
- Özgünlük: başkasının içeriğini yeniden paylaşmak yok; tasarım, metin ve müzik bize ait.

**Para kazanma basamakları** (Ece'nin işi en az olacak şekilde; her adım Ece onayıyla başlar):
1. **Şimdi – 1.000 takipçi:** güven ve kitle. Ücretsiz prompt rehberi = kitle toplama aracı. Ürün satışı yok.
2. **1.000 – 5.000:** (a) Ortaklık (affiliate) linkleri: yalnızca gerçekten kullandığımız araçlar. İlk aday ElevenLabs (PartnerStack üzerinden, tekrarlayan komisyon); başvuruyu Ece bir kez yapar. Paylaşımda reklam/ortaklık olduğu açıkça yazılır. (b) Ücretli dijital ürün: rehberin genişletilmiş hâli (ör. 100 prompt + şablonlar), Türkiye'de Shopier ya da benzeri bir mağazadan, düşük fiyat.
3. **5.000 – 10.000:** marka iş birlikleri (yapay zekâ ve tasarım araçları, Türkiye pazarı); "Reklam Lab" ve Reel formatında sponsorlu içerik. Sponsorlu içerik her zaman "iş birliği" etiketiyle.
4. **10.000+:** Instagram'ın kendi gelir araçları (abonelik, hediyeler) ve daha büyük anlaşmalar.
- Frame Lab'i işletmelere içerik hizmeti satan bir vitrin olarak kullanma fikri: Ece 11 Kasım'da "1 ay sonra düşünelim" dedi; 11 Aralık'ta hatırlatılacak. O tarihe kadar görevler bunu önermez ve hizmet tanıtımı yapmaz.
- Ece'nin zamanı: isteğe bağlı seslendirme, yorum onayı, tek seferlik kayıt/ödeme kurulumları. Bunun dışındaki her şeyi görevler yapar.

## Gelişim günlüğü (haftalık gelişim görevi doldurur)
Her cumartesi görev; verilere ve global örneklere bakıp en fazla 3 kanıta dayalı değişiklik yapar, buraya tarihle yazar. Ece'nin koyduğu kurallar (onay kuralları, renkler, yüzsüz hesap, uzunluk sınırları) görev tarafından değiştirilmez; öneri olarak Ece'ye sorulur.
- 2026-11-11: Başlangıç. Reel ağırlıklı sıra, 3 saniye kancası, editoryal tasarım dili, 8 müzik stili, sends odaklı CTA kuralı eklendi.
