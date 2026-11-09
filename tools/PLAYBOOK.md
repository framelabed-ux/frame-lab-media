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

## Izgara düzeni (puzzle)
- Profil ızgarası satranç tahtası gibi görünmeli: her feed gönderisinin kapağı bir öncekinin tersi olmalı. Açık (light veya soft) ve koyu (dark) sırayla gider.
- Son kapak tonu `posts/state.json` içindeki `grid` listesinin son öğesinde yazar. Yeni gönderinin kapak tonu bunun tersi seçilir.
- Reel kapağı `cover_url` ile ayrıca verilir. Kapak 1080x1920 olur, ama ızgarada ortadaki 3:4 alan görünür. Önemli metin dikeyde 300–1600 piksel arasında kalmalı.
- Carousel içinde kareler açık ve koyu sırayla gider, böylece kaydırırken ritim oluşur.

## Haftalık ritim (feed, saat 19:30 civarı)
Format dengesi: haftada 2 carousel, 2 Reel, 1 statik (tek görsel).
| Gün | Format | Seri |
| --- | --- | --- |
| Pzt | Carousel | Bu Hafta Dijitalde: haftanın 5 gelişmesi |
| Sal | Reel | Sıcak Gelişme |
| Çar | Statik (tek görsel) | Tasarım Kuralı / Günün Prompt'u: tek karede kaydedilecek bir kural, formül ya da hazır prompt |
| Per | Carousel | 1 Prompt 3 Sonuç: aynı prompt, farklı araçlar ya da yaklaşımlar, karşılaştırmalı |
| Cum | Reel | Kare Açıklıyor |
| Cmt | Sadece story | |
| Paz | Sadece story | |

Çok büyük bir gelişme olursa o günün planlı içeriğinin yerine "Sıcak Gelişme" girer, ama o günün formatı korunur (Reel günü Reel, carousel günü carousel, statik günü tek görsel). Böylece format dengesi bozulmaz. İçeriklerin yaklaşık %60'ı gündemden gelir. "Mutfaktan" (sosyal medya taktikleri) Çarşamba statiğinde ya da Pazartesi carousel'inde dönüşümlü kullanılabilir.

Statik gönderi: tek slaytlı carousel spec'iyle `render.py carousel` (1080x1350), yayın `create_image_post`. Metin tek bakışta okunmalı: bir başlık ve en fazla 3–4 kısa satır ya da bir prompt kartı.

## Story (her gün 1 tane, sabah yayınlanır)
Story o akşamki gönderinin merak uyandıran bir duyurusu, günün kısa bir ipucu ya da bir soru olabilir ("Yorumlara yaz" yerine "DM'den yaz"). 1080x1920 JPEG. Story'de saat yazma, "Bu akşam profilde" de.

Öne çıkanlar (Ece uygulamadan ekliyor, API desteklemiyor): Başla, Gündem, AI Lab, Tasarım, Mutfak. Sabah raporunda o günün story'sinin hangi öne çıkana eklenebileceğini öner. Kalıcı değeri olan story'ler (ipucu, formül, gündem özeti) öne çıkana uygundur, akşam duyuruları değildir.

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
