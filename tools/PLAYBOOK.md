# Frame Lab üretim kılavuzu

Frame Lab, Ece Duru'nun yüzsüz Türkçe Instagram hesabı: **@frame.labo**. Konular yaratıcı dijital dünyanın tamamı: tasarım, marka ve reklam, sosyal medya ve platformlar, video ve görsel kültür, internet trendleri, içerik üreticiliği ve para kazanma, yapay zekâ. **Yapay zekâ bu konulardan yalnızca biri** (Ece, 13 Kasım: "sadece yapay zekâ paylaşıyoruz, çok dar bir yere sıkıştırma bizi"). Ton sıcak, net, hafif esprili ve pratik. Her içerik bir şey dener ya da öğretir: "Haber değil, deney."

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
- **İkinci vurgu rengi: Pembe #FF2E93** (Ece, 13 Kasım: "sarıya gerek yok, sadece pembe eklenebilir, mevcut çizgiden çok uzaklaşmak doğru olmaz"). Metinde `[[!kelime]]` pembe vurgu verir (koyu temada pembe yazı, açık temada pembe kutu + siyah yazı); `bars` öğesine `"color": "pink"` vurgulanan çubuğu pembe yapar. Ölçülü kullan: bir içerikte lime ana vurgu, pembe en fazla 2–3 yerde (ör. kapakta ana rakam, bir sahnede grafik, son soru). Sarı, turuncu, açık mavi ve mor zemin kullanılmaz.
- Arada (haftada en fazla 1–2 içerikte) 3D nesne, illüstrasyon ya da animasyon kullanılabilir; ama genel görünüm mevcut çizgiden uzaklaşmaz. 3D için `tools/r3d.py` (tarayıcıda yazılımla çizilen sahneler: `SC` 0 = 3D Kare, 1 = oynat düğmesi, 2 = madeni paralar; renkler `BG0/BG1/RIMA/RIMB/OBJ`; çıktıyı `hero` ya da `photo_bg` olarak kullan). Renkler yine lime + pembe + siyah/krem.
- Üretim için `python3 tools/render.py` (carousel, story, reel). Spec örnekleri `tools/examples/` içinde. Vurgu için metinde `[[kelime]]` yazılır.

## Konu dengesi (Ece, 13 Kasım; 14 Kasım'dan itibaren geçerli)
- Yapay zekâ içeriği **en fazla 3 gönderide 1** olur. Art arda iki yapay zekâ gönderisi yok (çok büyük bir model duyurusu istisna; o zaman sonraki iki gönderi kesinlikle başka alandan).
- Kalan gönderiler "Konu alanları" listesindeki alanlardan döner (marka ve reklam, para ve iş, dikkat ve psikoloji, internet kültürü ve trend, görsel kültür, perde arkası) ve platform/sosyal medya haberleri.
- Gündem payı (~%60) yalnızca yapay zekâ gündemi demek değil: yeni logo ve kimlik değişimleri, konuşulan reklam kampanyaları, Instagram/TikTok/YouTube güncellemeleri, viral akımlar, tasarım araçlarındaki yenilikler de gündemdir.
- Hafta sonu "Kare Açıklıyor" Reel'leri de bu dengeye uyar: tasarım, marka, sosyal medya, psikoloji ya da internet kültüründen bir kavram (ör. "kerning nedir", "neden kırmızı logo çok", "algoritma ne demek").
- Her sabah `grid` ve `queue` içindeki son 3 kaydın `topic_area` alanına bak; kayıt yazarken `"topic_area"` alanını doldur (`ai`, `marka`, `para`, `psikoloji`, `trend`, `gorsel-kultur`, `platform`, `tasarim`, `perde-arkasi`).

## Gündem kaynakları: kaçırılmaması gerekenler
Genel arama tek başına yetmez (10 Kasım'da Claude Fable 5.2 duyurusu sabah taramasında kaçtı). Her taramada şu kaynaklar **tek tek** kontrol edilir, son 48 saatte yeni bir duyuru var mı diye:
- **Yapay zekâ şirketleri:** Anthropic (anthropic.com/news, @claudeai), OpenAI (openai.com/news), Google (blog.google, deepmind.google), Meta AI (ai.meta.com/blog), xAI, Mistral, Microsoft (Copilot), Apple.
- **Görsel ve video yapay zekâsı:** Midjourney, Runway, Pika, Luma, Kling, ElevenLabs, Stability, Black Forest Labs (Flux), Ideogram.
- **Tasarım araçları:** Adobe (blog.adobe.com, Firefly), Canva (canva.com/newsroom), Figma (figma.com/blog), CapCut.
- **Platformlar:** Instagram (about.instagram.com, @mosseri), Meta newsroom, TikTok newsroom, YouTube blog / Creator Insider, Threads, LinkedIn.
- **Teknoloji medyası:** TechCrunch AI, The Verge AI, Engadget, Social Media Today (platform haberleri için).
- **Marka, reklam ve tasarım medyası:** Brand New (underconsideration.com/brandnew, logo/kimlik değişimleri), Creative Bloq, It's Nice That, Dezeen (grafik/ürün), Adweek, Ad Age, Campaign, The Drum, Marketing Türkiye, Kreatif, Webrazzi (Türkiye dijital gündemi).
- **Trend ve internet kültürü:** Know Your Meme (akımın kaynağını doğrulamak için), TikTok Creative Center trendleri, Instagram @creators.
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
- Renk ve tipografi dili (Ece, 13 Kasım): A/B/C yönleri ve sarılı yeni ızgara reddedildi. **Mevcut çizgi sürer, yalnızca pembe eklenir** (bkz. Marka). Izgara yeniden yapılmaz.

## Süs yok kuralı (Ece, 13 Kasım: "anlamsız şeyler koyma, gereksiz şeyler koyma tasarımlara")
Tasarımdaki her öğe ya bilgi taşır ya da konuyu gösterir. Şunlar **kullanılmaz**:
- Sıra/sayı numaraları ("№ 18" gibi), kod, tarih damgası gibi okura bir şey söylemeyen etiketler.
- Köşe çizgileri, kamera kadrajı, odak kutusu, REC, zaman kodu, pozlama cetveli gibi sahte arayüz öğeleri.
- Yalnızca boşluk doldurmak için konan artı işaretleri, ince çizgiler, rastgele şekiller.
- Düz turuncu ve düz açık mavi zemin/vurgu (Ece "çok kötü durmuş" dedi).
Üstteki küçük seri adı (Video, Tasarım, Kare Açıklıyor…) kalabilir; başka üst/alt etiket eklenmez.
- **Alt bilgi (Ece, 14 Kasım):** "@frame.labo" kullanıcı adı ve "FRAME/LAB" yazısı kullanılmaz (zaten o hesaptan paylaşılıyor). Sağ altta yalnızca küçük FL logosu durur; `render.py` bunu otomatik yapar. (28 Kasım: `tools/scenes/3d-kare.html`, `ui-telefon.html` ve `cartoon-kare.html` şablonlarına sol alta "@frame.labo" yazısı gömülüydü ve 18–25 Kasım Reel'lerinde görünüyordu; şablonlardan kaldırıldı. Eski bir `posts/*/scene.html` kopyalanarak yeni sahne yapılırsa `id="hand"` satırı ve `fillText('@frame.labo'…)` silinir. Logo kapanışındaki "Takip et" sahnesi aynen kalır.)
- Motor seçenekleri: `"frame": true` (köşe çizgileri) **kullanılmaz**. `"pattern"` (nokta/ızgara/halka deseni), `burst` (parıltı) ve `marquee` (kayan yazı) yalnızca bir anlam taşıyorsa kullanılır, süs olsun diye konmaz. Aşağıdaki eski bölümlerde bunlardan söz edilse de bu kural önceliklidir.

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

## Format sırası: sabah statik, akşam Reel (Ece, 16 Kasım; 17 Kasım'dan itibaren her gün, hafta sonu dahil)
Ece: "Sabahları statik post, akşamları video paylaş." Her gün **2 feed gönderisi** çıkar:
- **Sabah (~09:00–09:30): hareketli kare (Ece, 17 Kasım onayladı).** Statik gönderi tasarımı, 7–10 saniyelik tek sahnelik, müzikli bir Reel olarak yayınlanır. Neden: 5 takipçiyle gerçek statikler 2–7 kişiye ulaştı; Reel'ler takip etmeyenlere de gösteriliyor. Profilde yine tek kare gibi durur. Takipçi birkaç yüze çıkınca gerçek statiğe dönmeyi Ece'ye sor.
  - **17 Kasım güncellemesi:** Ece bu metin ağırlıklı kalıbı "sıkıcı" buldu. Sabah gönderisi de "Dikkat araştırması ve yeni görsel dil" kurallarına uyar: 7–10 sn'lik kısa bir çizgi film / oyun / 3D sahnesi (`tools/anim.py`). Aşağıdaki kare-reel.json yalnızca teknik ayarlar (tek sahne, outro yok) için referanstır.
  - Nasıl: `tools/examples/kare-reel.json` kalıbı. Tek sahne, `"outro": false`, `"progress": false`, 7–10 sn. Ana başlık ya da rakam `at` almaz, 0. karede tam görünür; yalnızca ikincil satırlar 1–2. saniyede girer. İçerik ortadaki 3:4 alanda kalır. Müzik stili akşam Reel'inden farklı.
  - Kapak: aynı sahnenin son hali, `render.py story` ile `"nofoot": true`.
  - Yayın: sabah görevi kalite kontrolünden sonra **hemen kendisi yayınlar** (`create_video_post`, `share_to_feed: true`). Kuyruğa girmez, doğrudan `grid`'e `kind: "kare-reel"` ile yazılır.
  - Statik seriler (aşağıdaki tablo) bu gönderide kullanılır. Format sırası hesaplarında `kare-reel` statik sayılır.
- **Önceden hazırlanmış sabah gönderisi:** `queue` içinde `publish_date` bugün ve `"slot": "sabah"` olan bir öğe varsa (Ece ile birlikte hazırlanmış), sabah görevi yeni sabah gönderisi üretmez; bu öğeyi kalite kontrolünden geçirip sabah yayınlar ve `grid`'e taşır. Akşam görevi `slot: "sabah"` öğelerini yayınlamaz.
- **Haftalık plan (Ece, 18 Kasım: "bu haftanın videoları için ses metinlerini ilet"):** `state.json` → `planned_reels` içinde bugünün tarihli bir kaydı varsa, akşam Reel'i o kayıttan üretilir: konu, tarz, `script` (seslendirme metni; ekrandaki yazılar bununla birebir uyumlu ve kısaltılmış olur), `visual_note` ve kaynaklar. Ece'nin sesi `posts/<slug>/voice.mp3` olarak repoda varsa `tools/anim.py --voice` ile eklenir ve sahneler cümle aralarına göre hizalanır (silencedetect + WARP_V); yoksa video müzikle çıkar. Plan, büyük bir gündem gelişmesinde bir gün kaydırılabilir; bu durumda raporda Ece'ye söylenir.
- **Akşam (19:10): Reel.** Sabah görevi üretip kuyruğa koyar, akşam görevi yayınlar. Hafta sonu Reel'leri "Kare Açıklıyor" serisinden olur.
- Carousel şimdilik rotasyonda yok. Çok iyi bir carousel fikri çıkarsa sabah statiğinin yerine kullanmak için Ece'ye sor.
- Aynı günün statiği ve Reel'i **farklı konu alanlarından** olur (bkz. Konu dengesi). Yapay zekâ yine en fazla 3 gönderide 1.
- Kapak tonu: sabah statiği `grid`'in son kaydının tersi, akşam Reel kapağı sabah statiğinin tersi (açık/koyu dama düzeni sürer). Izgara sütun döngüsü (`cover_type`) iki gönderide de devam eder.
- **Büyük gündem gelişmesi:** Sabah fark edilirse o günün akşam Reel'i bu konuda olur (planlanan Reel ertesi güne kayar). Öğle görevi fark ederse **üçüncü gönderi açmaz**: o konuda Reel üretir ve bugünün kuyruktaki akşam Reel'inin yerine koyar; yerinden çıkan Reel'in `publish_date`'i ertesi gün olur ve ertesi sabah yeni Reel üretilmez. Akşam Reel'i zaten büyük bir gelişme hakkındaysa dokunulmaz, yeni konu `hot_pending`'e yazılır.
- Günde ikiden fazla feed gönderisi yok. Story günde 1 kalır (sabah görevi, statik gönderiden farklı bir düzen ve tercihen farklı konu).
- Eski `"extra": true` işareti artık kullanılmaz (geçmiş kayıtlarda kalabilir).

Formata göre seriler:
| Format | Seriler |
| --- | --- |
| Reel | Sıcak Gelişme (gündemde büyük bir şey varsa), Kare Açıklıyor (bir kavramı 30–40 saniyede anlatır) |
| Carousel | Bu Hafta Dijitalde (haftanın ilk carousel'i, haftanın en önemli 3–4 gelişmesi), 1 Prompt 3 Sonuç (karşılaştırma), Mutfaktan (sosyal medya taktikleri), Kare'den Haberler (numaralı seri: 1–3 doğrulanmış gelişme, her biri için ne oldu, nasıl çalışır, sana ne faydası var; Ece 10 Kasım'da başlattı) |
| Statik (tek görsel, her sabah) | Günün Prompt'u (kopyalanacak hazır prompt), Tasarım Kuralı (tek kural, tek örnek), Bunu Bilmen Lazım (gündemden tek kare), Marka Önce/Sonra (logo ya da kimlik değişimi, görsel kural ve telif sınırları geçerli), Tek Rakam (doğrulanmış tek bir veri), Mini Test ("hangisi daha okunaklı?" gibi yoruma davet eden soru) |

**Konu alanları genişletildi (Ece, 13 Kasım: "içerik skalasını da genişletelim").** Gündem dışındaki içerikler yalnızca yapay zekâ/tasarım/sosyal medya ipuçlarıyla sınırlı değil; şu alanlar sırayla dönsün, aynı alan art arda iki kez gelmesin:
- **Marka ve reklam:** yeni logo/kimlik değişimleri, dikkat çeken kampanyalar, "bu reklam neden çalıştı" (Reklam Lab kuralları geçerli).
- **Para ve iş:** freelance fiyatlama, ilk müşteriyi bulma, içerik üreticilerin gelir yolları, teklif/brief hazırlama.
- **Dikkat ve psikoloji:** neden kaydırırız, kanca neden çalışır, renk ve yazı tipi algısı. İddia varsa kaynağı doğrulanır.
- **İnternet kültürü ve trend:** "bu format neden tuttu", viral bir akımın anatomisi.
- **Görsel kültür:** film jeneriği, klip, oyun ve afiş tasarımından tek bir fikir; tipografi ve tasarım tarihinden kısa hikâyeler.
- **Perde arkası:** bir içeriği (3D sahne, animasyon, kapak) nasıl yaptığımız.
Bu alanlardaki olgular da gündem haberleri gibi doğrulanır; doğrulanamayan rakam yazılmaz.

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
- **Görseli olmayan marka haberi yok (Ece, 14 Kasım: "Tomy story'sinde Tomy'ye dair hiçbir görsel yok").** Logo, kimlik, ambalaj ya da kampanya konusu işleniyorsa (story, carousel ya da Reel) konunun kendisi görünmeli: resmî basın görseli (`photo` / `photo_bg`, künyeli). Bulut ortamı basın sitelerinden görsel indiremiyor (proxy engeli); görsel alınamıyorsa o konu seçilmez, görselsiz anlatılabilen bir konu seçilir ya da Ece'den görsel istenir.

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
  - `{"type":"clock","size":600,"start":0.3,"secs":3}` kronometre: her saniye tıklayarak ilerler (tık sesi otomatik), sonunda alarm çalar ve saat sallanır. Hafıza/bekleme testleri için (Ece, 14 Kasım). Sahneye `"music_mute": [0, 4.0]` yazılırsa müzik o aralıkta kısılır; `"sfx_events": [[sn, "tick"|"alarm"|"pop"…]]` ile sahneye özel ses eklenir.
  - `bignum` öğesine `"count_at": 0.3` eklenirse rakam sıfırdan sayarak gelir ("1.140" gibi binlik ayraçlı sayılar da sayar).
- **Kare:** sahnelere öğe olarak eklenmez. Her sahneye `"kare": {"x":…, "y":…, "size":…, "face":…}` yazılır; Kare geçişlerde bir sonraki konuma zıplar (zoom ve wipe geçişlerinde takla atar), sahnede süzülür ve göz kırpar. Konumu metinle çakışmamalı; sahneden sahneye köşe, boyut ve ifade değişsin. `"kare": null` olursa o sahnede görünmez.
- **İlerleme çubuğu:** üstte sahne sayısı kadar parçalı ince çubuk otomatik gelir (izleyene videonun kısa olduğunu gösterir). Kapatmak için spec'e `"progress": false`. Üstteki ilk 100 pikselde öğe olmasın.
- **Müzik (Ece, 11 Kasım: "her videonun müziği aynı olmasın"):** Spec'e `"music": {"style": "...", "seed": <sayı>}` yaz. Stiller: `pop`, `lofi`, `house`, `synthwave`, `minimal`, `trap`, `funk`, `ambient`. Son 3 Reel'in stilini `grid` kayıtlarındaki `music` alanından oku ve onlardan farklı birini seç; tohumu da her seferinde değiştir (aynı stil + farklı tohum = farklı ton, tempo ve melodi). Konuya göre seç: haber/teknoloji → synthwave, house, minimal; sakin/iş → lofi, ambient; eğlenceli → funk, pop; dramatik → trap. Seslendirmeli videolarda lofi, ambient, minimal daha iyi oturur. Seçilen stili kuyruk kaydına `"music"` olarak yaz.
- **Ses efektleri:** geçişlerde hafif "whoosh", ana öğe girerken "pop", logoda "ding" otomatik eklenir ve müzikle karışır. Kapatmak için `"sfx": false`.
- Her Reel'in sonuna otomatik olarak 3,2 saniyelik logo outro'su eklenir. Kapatmak için `"outro": false`. Toplam süre hesaplanırken outro'yu da say.
- `"stills": [saniye, …]` ile kontrol kareleri üretilir. Her sahnenin dolu anından ve en az bir geçiş anından kare alıp Read ile bak; çakışma, taşma ya da Kare'nin yazıyı kapatması varsa düzelt. Kapak için ilk sahnenin dolu anındaki kare (`*_still_*.jpg`) kullanılabilir.
- **Reel kapağı:** ilk sahnenin öğelerini `at` olmadan, `"align": "center"` ve `"nofoot": true` ile `render.py story` modunda ayrı render et (örnek: `posts/2026-11-11-adobe-max-creative-agent/cover.json`). Başlık, ızgaradaki 3:4 kırpmaya (üstten 240, alttan 240 piksel kesilir) sığmalı.
- **İlk kare kancayı taşır (haftalık gelişim, 14 Kasım):** İlk sahnenin başlığına (h1) `"at"` **yazılmaz**; kanca cümlesi videonun 0. karesinde tam ve okunur durur (izleyicilerin çoğu sessiz izliyor, kaydırma kararı ~1,5 saniyede veriliyor). Hareketi sahnenin hafif yaklaşması, Kare, sticker ve sonradan gelen alt yazı (`"at"` en geç 0,8) verir. İlk sahnede başlığın üstüne ayrı bir küçük `lead` satırı ("X dün duyurdu") koyma; bu bilgi alt yazıya ya da ikinci sahneye gider. İlk sahne başlığı kalın (Inter Display 800) olur, `"light": true` ince editoryal başlık kapakta ve sonraki sahnelerde kullanılır. Kanıt: ince başlık + üstte küçük satırla açılan iki Reel (Claude Meetings, Adobe) ilk 3 saniyede %83–85 kaybetti; kalın başlıkla açılan Fable %61.
- **Açılış kancası:** Ortalama izleyici ilk 3 saniyede karar veriyor. İlk sahne rakamlı, sonucu önce gösteren ya da merak boşluğu açan tek bir cümleyle açılmalı ("Bu reklamda oyuncu hiç sete gelmedi.", "Aynı prompt, 3 sonuç: farkı tek kelime yaptı."). **"X artık Y" kalıbı kullanılmaz** (haftalık gelişim, 14 Kasım: bu kalıpla açılan 3 Reel'in ilk 3 saniye kaybı ortalama %81, diğerlerinin %69). Haberde ürünün adı + somut sonuç birlikte gelsin ("Claude Fable 5.2 çıktı: %30 daha hızlı."). Aynı kanca kalıbını art arda iki Reel'de kullanma. Logo, selamlaşma, "bugün sana … anlatacağım" ile açma.
- **Süre:** İdeal 20–35 saniye, outro dahil en fazla 45 saniye. Fable Reel'inde ortalama izlenme 12 saniyeydi, asıl bilgi ilk 10 saniyede verilmeli.

## Seslendirme
Otomatik çalışmada yapay ses aracı yok. Reel'ler ekran yazısı ve müzikle (`tools/music.py`, otomatik) üretilir. Ece ses dosyası gönderirse spec'e `voice_segments` eklenip `render.py reel spec out voice` ile kullanılır. Yazılar, sessiz izleyen biri de anlayacak kadar okunur süre ekranda kalmalı: kelime başına en az 0,35 saniye.

## Kalite kontrol (her içerikte, yayından önce)

**Anlam ve dil kontrolü (Ece, 18 Kasım: story'de "BEN DE MİYİM?" yazıyordu: "neden böyle yanlış ve anlamsız ifadeler kullanıyorsun").** Görsel ya da videodaki her metin yayından önce şu adımlardan geçer:
1. `python3 tools/metinler.py posts/<klasör>` ile tüm ekran metinlerini (balon, altyazı, başlık, piksel yazı, etiket, kapak) ve açıklamayı tek listeye çıkar. **Ece, 18 Kasım: "paylaşmadan önce mutlaka kontrol et, yazım hatası ya da gramer hatası asla olmamalı."** Bir tek hata bile varsa gönderi yayınlanmaz; düzeltilip yeniden üretilir. Satırlara bölünmüş ifadeleri birleştirip **tam cümle olarak** oku.
2. Her ifade, bağlamı bilmeyen birinin ilk okumada anlayacağı, dil bilgisi doğru, eksiksiz bir Türkçe cümle ya da öbek olmalı. Soru ekleri ünlü uyumuna ve yazımına uyar, eklendiği kelime eksik bırakılmaz ("Ben de insan mıyım?" doğru, "Ben de miyim?" yanlış).
3. Esprili ya da karakter replikleri için: "Bunu açıklamam gerekir mi?" Gerekirse replik atılır ya da açık hâle getirilir. Uydurma kelime oyunu, yarım bırakılmış soru, belirsiz zamir yok ("kişilerin" yerine "rehberindeki kişiler").
4. Piksel yazıda Türkçe harflerin (İ, I, Ş, Ğ, Ü, Ö, Ç) doğru göründüğünü karede kontrol et.
5. Raporda Ece'ye ekran metinlerinin tam listesini de ver.
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
- **Reel hedef çizgisi (haftalık gelişim, 14 Kasım, kendi verimiz):** ilk 3 saniye kaybı (skip rate) **%60'ın altı**, ortalama izlenme **8 saniye ve üstü**. İlk haftada skip'i %73–85 olan 6 Reel'in hepsi ~105–122 erişimde kaldı (Instagram'ın ilk deneme kitlesi); %61 olan Fable 1.400'e ulaştı. Yani asıl darboğaz kanca: bir Reel bu çizginin üstündeyse sonraki Reel'de yalnızca açılışı değiştir ve karşılaştır (tek değişken).
- Haftalık görev her cumartesi `state.json` içindeki `weekly_metrics` listesine o haftanın özetini (tarih, takipçi, toplam izlenme/erişim, en iyi/en kötü media_id) ekler; takipçi artışı bir önceki kayıtla karşılaştırılarak hesaplanır.
- Özgünlük: başkasının içeriğini yeniden paylaşmak yok; tasarım, metin ve müzik bize ait. (Instagram 17 Kasım 2026'da yeniden paylaşımları ve sesi kopyalanan yapay zekâ videolarını yakalayan "içerik koruma" aracını duyurdu ve bu tür hesapların erişimini sınırlamayı araştırıyor: techcrunch.com/2026/11/17/instagrams-new-tool-for-creators-targets-unauthorized-reposts-and-ai-modified-videos. Hesaba bildirim gelirse kayıt Ece'nin onayıyla yapılır.)
- **Takipçiye çevirme (haftalık gelişim, 21 Kasım):** 15–20 Kasım'da ~6.500 erişime karşı yalnızca +1 takipçi geldi; insanlar izliyor ama takip etmek için bir sebep görmüyor. Genel "takip et" yerine bir sonraki içeriği vaat eden CTA öneriliyor (imarkinfotech.com/why-your-reels-are-getting-views-but-zero-followers-fix-this-now; mandermarketing.com/blog/how-to-convert-instagram-views-into-followers) ve Instagram Reel'leri seri olarak bağlamaya izin veriyor (techcrunch.com/2025/08/21/instagram-now-lets-creators-link-multiple-reels-in-a-series). Kurallar: (1) Her Reel caption'ının son satırı ve seslendirme metninin son cümlesi, takip etmenin somut sebebini söyler: "Her akşam dijital dünyadan bir şeyi 30 saniyede çözüyoruz. Yarınki: <kısa konu>." (yarının konusu `planned_reels`/`queue`'dan; bilinmiyorsa yalnızca ilk cümle). Yorum/gönder CTA'sı bundan önce gelir, logo kapanışı aynen kalır. (2) Haftalık raporda takipçi/erişim oranı izlenir (10.000 erişimde 10+ takipçi ilk hedef).

**Para kazanma basamakları** (Ece'nin işi en az olacak şekilde; her adım Ece onayıyla başlar):
1. **Şimdi – 1.000 takipçi:** güven ve kitle. Ücretsiz prompt rehberi = kitle toplama aracı. Ürün satışı yok.
2. **1.000 – 5.000:** (a) Ortaklık (affiliate) linkleri: yalnızca gerçekten kullandığımız araçlar. İlk aday ElevenLabs (PartnerStack üzerinden, tekrarlayan komisyon); başvuruyu Ece bir kez yapar. Paylaşımda reklam/ortaklık olduğu açıkça yazılır. (b) Ücretli dijital ürün: rehberin genişletilmiş hâli (ör. 100 prompt + şablonlar), Türkiye'de Shopier ya da benzeri bir mağazadan, düşük fiyat.
3. **5.000 – 10.000:** marka iş birlikleri (yapay zekâ ve tasarım araçları, Türkiye pazarı); "Reklam Lab" ve Reel formatında sponsorlu içerik. Sponsorlu içerik her zaman "iş birliği" etiketiyle.
4. **10.000+:** Instagram'ın kendi gelir araçları (abonelik, hediyeler) ve daha büyük anlaşmalar.
- Frame Lab'i işletmelere içerik hizmeti satan bir vitrin olarak kullanma fikri: Ece 11 Kasım'da "1 ay sonra düşünelim" dedi; 11 Aralık'ta hatırlatılacak. O tarihe kadar görevler bunu önermez ve hizmet tanıtımı yapmaz.
- Ece'nin zamanı: isteğe bağlı seslendirme, yorum onayı, tek seferlik kayıt/ödeme kurulumları. Bunun dışındaki her şeyi görevler yapar.

## Dikkat araştırması ve yeni görsel dil (Ece, 17 Kasım: "sadece metinlerden oluşuyor, koca bir 66 yazısı kimsenin dikkatini çekmez … ikonlar, maskotlar, 3D, oyun, çizgi film olabilir")
Bulgular (kaynaklar aşağıda):
- Beyin ilk 100–250 ms'de yalnızca renk, yön, boyut ve **hareketi** tarar; hareket ve renk en güçlü ikisi. Düz zeminde duran metin bu taramada öne çıkmaz.
- **Yüz ve göz** en hızlı fark edilen şeydir; çizgi film gözleri ve yüze benzeyen şekiller de aynı önceliği alır. İzleyiciye bakan maskot güveni artırır.
- **Karakter** kullanan reklamlar (13.000 reklam analizi) yeni müşteri, pazar payı ve kârda daha iyi sonuç verdi. Duolingo: maskot logo değil, karakter; diziye dönüşen hikâyeler.
- İnsanlar az önce gördüklerinden **farklı** görünen şeyde durur. Düz akışta 3D hacim ve ışık fark yaratır; yapay zekâ içeriği arttıkça el yapımı/kil/çizgi film dokusu öne çıkıyor; Mosseri "kusursuz cilalı estetik bitti" diyor.
- Mizah ve merak durdurur (tüketicilerin %55'i komik an ya da güçlü kanca için duruyor). Başarılı yüzsüz kanallar sabit bir görsel dil ve tekrar eden karakterle tanınır (Kurzgesagt kuşları).
Kurallar (hemen geçerli):
1. **Sadece metin + rakam kompozisyonu yasak.** Her gönderinin ilk karesinde ya büyük ve izleyiciye bakan **Kare** (bir şey yaparken: şaşırıyor, kaçıyor, bir şeyi gösteriyor) ya da konuyu gösteren **bir nesne/sahne** (3D nesne, ikon, illüstrasyon, oyun sahnesi) olur. Metin ikinci planda, ekranda en fazla ~6 kelimelik başlık + altyazı.
2. **0. karede hareket:** ilk karede bir şey zaten hareket ediyor (düşüyor, dönüyor, koşuyor).
3. **Tarz dönüşümü:** tarzlar dönüşümlü kullanılır, aynı tarz art arda 2 kez gelmez: **çizgi film** (`tools/scenes/cartoon-kare.html`: kalın kontur, lastik hortum kollu Kare, 12 fps titreyen çizgi), **oyun** (`tools/scenes/game-kare.html`: 8-bit, HUD, görev/level dili, Türkçe piksel yazı), **3D** (`tools/scenes/3d-kare.html`: ışın yürütmeli 3D Kare ve nesneler), mevcut **editoryal** Reel motoru yalnızca veri/haber anlatımında ve mutlaka bir görsel öğeyle. Ortak bağ: Kare, lime + pembe, Inter.
4a. **Logo kapanışı (Ece, 18 Kasım: "sondaki logo motionları neden kaldırdın"):** Her Reel FL logo animasyonu + "Takip et" kapanışıyla biter. `tools/anim.py` bunu varsayılan olarak ekler (brand/outro.mp4, 3,2 sn); `--nooutro` kullanılmaz. Seslendirme varsa `--voice ses.mp3` ile eklenir.
4b. **Kapak (Ece, 18 Kasım: "kapakları garip, güzel durmuyor"):** Kapak videodan rastgele kare değil, ayrı tasarlanır (`cover.html`): profil ızgarası 1080x1920 kapağın ortadaki 1080x1440 alanını (y 240–1680) gösterir; başlık, karakter ve ana öğe tamamen bu alanın içinde, kenarlardan en az 60 px içeride olur. Kapakta kısa ve büyük bir başlık (en fazla ~6 kelime) + büyük Kare ya da konu nesnesi + videonun tarzı (çizgi film / oyun / 3D). Sadece yazıdan oluşan kapak yok. Yayından önce kapağı 1080x1440 kırpıp aç ve kontrol et (`convert cover.jpg -gravity center -crop 1080x1440+0+0 +repage kontrol.jpg`).
4. Sahneler `tools/anim.py` ile müzikli MP4'e çevrilir (`window.render(t)`, `window.DUR`, `window.SFX`). Yeni konu için uygun sahne dosyası kopyalanıp metinler, zamanlama ve olay örgüsü konuya göre yeniden yazılır; aynı sahne aynen tekrar kullanılmaz.
5. Her video bir **mini hikâye** taşır: Kare bir sorunla karşılaşır → konu çözüm olarak gösterilir → izleyiciye dönük kapanış. Mümkünse bir espri.
6. **Ece'nin tarz geri bildirimi (18 Kasım):** Instagram Direct'in çizgi film versiyonunu "hiç beğenmedim" dedi. Sebepler: renkler (büyük pembe/lime daireler + krem zemin), çocuksu görünüm (lastik kollar, kalın kontur), basit görseller. Aynı videonun **gerçekçi arayüz** versiyonunu kabul etti (`tools/scenes/ui-telefon.html`: koyu zemin, gerçekçi telefon, uygulama ekranlarının canlandırılması, Kare köşede küçük rehber). Buna göre:
   - **Gerçekçi arayüz** tarzı ana tarzlardan biri: uygulama, platform ve özellik haberleri için öncelikli (ekranlar uydurma marka logosu içermez; gerçek logoları kopyalama, genel ikon kullan).
   - **Çizgi film** tarzı bu haliyle kullanılmaz; kullanılacaksa daha olgun çizilir: ince kontur, dolgun ve detaylı çizimler, büyük renkli daire zeminler yok, koyu ya da nötr zemin. Ece onaylayana kadar çizgi film yerine arayüz, oyun ya da 3D tercih edilir.
   - 1,7 saniye çizgi film videosu iyi sonuç verdi (1.010 erişim) ama tarz Ece'nin beğenisine uymadığı için tekrarlanmaz; o videodan alınan ders izleyiciye bakan karakter + doğrudan hitap eden açılıştır, tarz değil.
Kaynaklar: pre-attentive tarama (oakgen.ai/blog/thumb-stopping-social-media-visuals; scitepress.org/Papers/2025/131287/131287.pdf), yüz/pareidolia (eurekalert.org/news-releases/1092222; par.nsf.gov/servlets/purl/10400737), maskot göz teması (livescience.com/44621-why-characters-on-cereal-boxes-stare-at-you.html), karakterli reklamlar (archive.researchworld.com/building-character-why-every-brand-needs-a-mascot), Duolingo (ads.tiktok.com/business/en/inspiration/ad-awards-duolingo-case-study), 3D fark (futuramo.com/blog/?p=19027), el yapımı animasyon (mediapost.com/publications/article/419160), Mosseri ve paylaşım ağırlığı (dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers), mizah/kanca (clutch.co/resources/attention-economy-2025), görsel kimlik (revid.ai/blog/best-faceless-youtube-channels).

## Veri dersleri (17 Kasım analizi, 15 gönderi, 5 takipçi)
Instagram her Reel'i önce ~100–120 takip etmeyen kişiye deniyor; sinyal iyiyse genişletiyor. Bizde 2 Reel bu eşiği geçti, 9'u ~105–125 erişimde kaldı. Statik ve carousel'ler 2–7 erişimde kaldı (yalnızca takipçiler görüyor).
| | Geçenler (Fable 5.2, YouTube–GTA VI) | Kalanlar (9 Reel) |
| --- | --- | --- |
| Erişim | 1.400 / 1.150 | 105–123 |
| 3 sn'de geçme | %61 / %53 | %57–85 (çoğu %73+) |
| Ort. izlenme | 11,2 / 11,3 sn | 2,7–8,6 sn |
| Paylaşım | 6 / 5 | 0–2 |
| Konu | Herkesin bildiği büyük isim, aynı gün sıcak haber | Niş kavram (60-30-10, hız eğrisi) ya da ikinci kez aynı marka (Gemini ×2) |
Kurallar:
1. **Geniş tanınırlık testi:** Reel'in ilk karesinde geniş kitlenin bildiği bir isim (oyun, uygulama, büyük marka, platform) ya da herkesin yaşadığı bir sorun olur. Niş tasarım kavramları ancak gündelik bir sonuca bağlanarak anlatılır ("Sunumun neden ucuz görünüyor?" gibi), kavram adıyla açılmaz.
2. **Sıcakken çık:** Büyük haber aynı gün çıkmalı; iki kazanan da haberin günü yayınlandı.
3. **Paylaşılabilirlik:** Her Reel "bunu bir arkadaşıma atar mıyım?" testinden geçer; kazananlarda paylaşım/erişim ~%0,4, kalanlarda ~%0–1 adet. CTA'larda ara sıra "bunu ... olan arkadaşına gönder" kullanılır.
4. **Tutma:** Hedef çizgisi sürer (3 sn'de geçme < %60, izlenme ≥ 8 sn). Von Restorff Reel'i %57 ve 8,6 sn'ye ulaştı ama paylaşım 0 olduğu için genişlemedi: tutma tek başına yetmiyor.
5. **Statik/carousel erişimi takipçiye bağlı:** Takipçi az iken statik gönderiler neredeyse kimseye ulaşmaz; bunu Ece'ye raporla, yeni takipçi kazanmak için Reel'e güven.
6. **Ses en güçlü kaldıraç (haftalık gelişim, 21 Kasım; 15–20 Kasım, 11 Reel):** Ece'nin seslendirdiği 5 Reel'in **5'i de** test havuzunu aştı (1.014–1.404 erişim, skip %45–54, izlenme 8,7–13 sn). Sessiz 6 Reel'in **6'sı da** ~105–118'de kaldı (skip %66–88, izlenme 2,6–4,4 sn) — akşam ya da sabah, uzun ya da kısa fark etmeden (seslendirmeli GPT-6.2 Reel'i 10:49'da çıkıp 1.028'e ulaştı, yani saat değil ses belirleyici). Dış kaynak: altyazılı Reel'lerde tamamlanma ~%65'e karşı ~%37 (Metricool, creatorlanehq.com/blog/instagram-algorithm-2026-mosseri-vs-measured); yüzsüz seslendirmeli liste Reel'leri yalnız yazılılardan fazla erişim alıyor (lilachbullock.com/instagram-reels-types-more-views). Kurallar:
   - `planned_reels` içinde bugünden sonraki 3 gün için kayıt kalmadıysa sabah görevi o günkü raporda Ece'ye önümüzdeki 3–5 akşam Reel'inin seslendirme metinlerini (her biri ~60–90 kelime, 20–35 sn'ye sığan) tek mesajda gönderir ve kayıtları `planned_reels`'e yazar; böylece Ece hepsini tek oturumda kaydedebilir. Ses gelmezse Reel her zamanki gibi müzikle çıkar.
   - Sessiz çıkan Reel'lerde ekran yazısı konuşma altyazısı gibi kurulur: ilk karede tam cümle kanca, ardından kısa satırlar sesli okunuyormuş gibi sırayla gelir (kelime başına ≥0,35 sn kuralı sürer).
7. **Gönderilme için Türkiye açısı (haftalık gelişim, 21 Kasım):** Haftanın en çok gönderilen Reel'i Direct (Türkiye'de test ediliyor): 132 paylaşım, erişim başına **%9,4**; diğer 10 Reel %0–2,7 (seslendirmeli olanlar bile %0,1–0,4). Dış ölçüt: erişim başına gönderim %1–2 "güçlü", %3+ "viral" (Influencer Marketing Hub, creatorlanehq.com üzerinden). Kurallar: Gündem haberinde Türkiye'yi doğrudan ilgilendiren bir taraf varsa (Türkiye'de açıldı/test ediliyor, Türk markası, TL fiyatı, Türkçe desteği) kanca bununla açılır ve CTA kişiyi etiketler ("…olan arkadaşına gönder"). Türkiye tarafı doğrulanamıyorsa uydurulmaz. Haftalık raporda hedef: en az bir Reel'de gönderim/erişim ≥ %1.
8. **Sessiz Reel arayüzle açılmaz (haftalık gelişim, 28 Kasım; 21–28 Kasım, 14 Reel):** Seslendirmesiz Reel'lerde gerçekçi arayüz (telefon ekranı) ile açılan 4 videonun ilk 3 saniye kaybı ortalama **%77** (İçerik koruma %60, Canva %83, Güvenli alan %74, Saatlik mi proje mi %91 / 1,6 sn); oyun ya da 3D sahneyle açılan 5 sessiz videonun ortalaması **%56** (Tidal %46, Doksan dokuz %50, WhatsApp %54, TikTok %57, İndirim sayacı %73). Seslendirmeli arayüz Reel'i (Sesli mi sessiz mi) %51'de kaldı, yani sorun tarz değil, sessiz açılışta beyaz telefon ekranının reklam gibi durması. Kurallar: Ses yoksa **ilk sahne** oyun ya da 3D sahne olur, 0. karede büyük ve izleyiciye bakan Kare + tam cümle kanca (izlenme süresi en yüksek Reel'imiz YouTube TV'nin açılışı gibi: piksel sahne, kocaman soru, hemen başlayan sayaç). Arayüz ekranı ikinci sahneden itibaren gelir. Seslendirmeli Reel'lerde arayüzle açılış serbest. Dış kaynak: yüzsüz anlatım videolarında kanca ilk 3 saniyede ekranda yazılı olmalı (Revid, 176.367 video, TikTok verisi: revid.ai/blog/how-to-get-more-views-on-instagram-reels).
9. **"Yarın kendi işinde kullanır mı?" testi (haftalık gelişim, 28 Kasım):** Bu hafta test havuzunu aşan 3 Reel'in üçü de izleyicinin kendi işine, parasına ya da hesabına dokunuyordu (İlk freelance müşteri 1.171 erişim + 13 kaydetme; YouTube TV izlenmesi 1.203; Sesli mi sessiz mi 513). Tutması iyi olan genel kültür Reel'leri ise (Turuncu-mavi afişler skip %53 / 8,9 sn, Doksan dokuz %50 / 7,6 sn) **0 paylaşım, 0 kaydetme** ile 145 ve 219'da kaldı. Kural: `planned_reels`'e yazılan her konu "izleyici bunu yarın kendi işinde, hesabında ya da cebinde kullanır mı?" sorusuna evet demeli. Psikoloji, görsel kültür ya da marka konuları da bu teste bağlanır: kanca kavramdan değil, izleyicinin yapacağı şeyden açılır ("Afişinde bir şeyi öne çıkarmak mı istiyorsun?" gibi), kavram ikinci cümlede gelir. Kapanışta kaydedilecek tek somut adım olur. Dış kaynak: yüzsüz "nasıl yapılır" videoları aynı nişteki diğer yüzsüz videolardan belirgin fazla izleniyor (Revid, aynı veri seti, TikTok) ve başvuru niteliğindeki eğitici Reel'ler kaydetme alıyor (flowshorts.app/blog/faceless-instagram-reels-guide).

## Gelişim günlüğü (haftalık gelişim görevi doldurur)
Her cumartesi görev; verilere ve global örneklere bakıp en fazla 3 kanıta dayalı değişiklik yapar, buraya tarihle yazar. Ece'nin koyduğu kurallar (onay kuralları, renkler, yüzsüz hesap, uzunluk sınırları) görev tarafından değiştirilmez; öneri olarak Ece'ye sorulur.
- 2026-11-11: Başlangıç. Reel ağırlıklı sıra, 3 saniye kancası, editoryal tasarım dili, 8 müzik stili, sends odaklı CTA kuralı eklendi.
- 2026-11-14 (1): "İlk kare kancayı taşır": ilk sahne başlığı animasyonsuz, kalın ve 0. karede tam görünür; üstte küçük "X duyurdu" satırı yok. Kanıt: Meetings/Adobe Reel'leri (ince başlık + üst satır) skip %85/%83, Fable (kalın) %61. Dış kaynak: ilk karede tam görünen kanca yazısı ve sessiz izleme payı (creatorlanehq.com/blog/first-three-seconds-instagram-hook-anatomy-2026; lilachbullock.com/what-is-a-good-skip-rate-on-instagram). `tools/examples/reel-editorial.json` ilk sahnesi buna göre güncellendi.
- 2026-11-14 (2): "X artık Y" kanca kalıbı bırakıldı; ürün adı + somut sonuç ya da sonucu önce gösteren kanca. Kanıt: "artık" ile açılan 3 Reel ortalama skip %81, diğer 3 Reel %69.
- 2026-11-17: Ece "son içerikler hiç etkileşim almadı" dedi; 15 gönderilik analiz yapıldı, "Veri dersleri" bölümü eklendi; sabah görevi her gün son 7 günün verisine bakacak.
- 2026-11-21 (1): "Veri dersleri" 6: ses en güçlü kaldıraç. Seslendirmeli 5/5 Reel 1.000+ erişim, sessiz 6/6 Reel ~110. `planned_reels` boşalmadan 3–5 metin Ece'ye toplu gönderilir; sessiz Reel'de altyazı gibi kurgu. Kaynak: kendi verimiz (15–20 Kasım), Metricool (Creator Lane üzerinden), Lilach Bullock.
- 2026-11-21 (2): "Veri dersleri" 7: Türkiye açısı + gönderim/erişim ≥ %1 hedefi. Kanıt: Direct Reel'i %9,4 (132 paylaşım), diğerleri %0–2,7; dış ölçüt %1–2 güçlü, %3+ viral.
- 2026-11-21 (3): "Büyüme ve gelir": takipçiye çevirme kuralı (sonraki içeriği vaat eden son satır) ve Instagram içerik koruma aracı notu. Kanıt: ~6.500 erişim → +1 takipçi; TechCrunch 17 Kasım 2026, seri bağlama (TechCrunch 2025), iMark ve Mander Marketing.
- 2026-11-28 (1): "Veri dersleri" 8: sessiz Reel arayüzle açılmaz; ilk sahne oyun/3D + izleyiciye bakan Kare. Kanıt: sessiz arayüz açılışları skip ort. %77 (4 Reel), sessiz oyun/3D açılışları %56 (5 Reel), 21–28 Kasım; Revid (yazılı kanca, TikTok verisi).
- 2026-11-28 (2): "Veri dersleri" 9: "yarın kendi işinde kullanır mı?" konu testi. Kanıt: test havuzunu aşan 3 Reel'in üçü de izleyicinin işi/hesabıyla ilgili (1.171 / 1.203 / 513); iyi tutan genel kültür Reel'leri 0 paylaşım, 0 kaydetme ile 145/219. Kaynak: kendi verimiz, Revid, FlowShorts.
- 2026-11-28 (3): Sahne şablonlarındaki "@frame.labo" yazısı kaldırıldı (Ece'nin 14 Kasım alt bilgi kuralına aykırıydı; 22 ve 25 Kasım Reel karelerinde görüldü). "Süs yok kuralı" → Alt bilgi maddesine not eklendi.
- 2026-11-14 (3): Reel hedef çizgisi (skip < %60, izlenme ≥ 8 sn) ve `state.json` → `weekly_metrics` haftalık özet kaydı. Kanıt: skip %73–85 olan 6 Reel ~110 erişimde kaldı, %61 olan 1.400'e çıktı. Mosseri'nin küçük hesap içeriğini takipçi olmayanlara deneme amaçlı gösterme ilkesi (socialmediatoday.com, 24 Eylül 2026).

### Günde 2 Reel etkileşimi düşürüyor mu? (23 Kasım kontrolü)
- Hayır, veride böyle bir iz yok. 18 Kasım'da 3 Reel çıktı; ikisi 1.000'i geçti (1.028 ve 1.404). Sabah Reel'i olan 19, 20 ve 22 Kasım akşamlarında seslendirmeli Reel'ler 1.133–1.365 erişime ulaştı.
- Erişimi belirleyen sıklık değil, içerik: seslendirmeli akşam Reel'lerinin 7'de 6'sı 1.000+; seslendirmesiz kısa sabah Reel'lerinin 7'de 7'si 120'nin altında (skip %60–87).
- Sabah Reel'i zarar vermiyor ama katkı da vermiyor. Sıklığı değiştirme kararı Ece'nin.
