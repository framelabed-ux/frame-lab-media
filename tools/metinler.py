"""Yayın öncesi metin listesi: bir gönderideki TÜM ekran metinlerini ve açıklamayı tek listeye döker.
Kullanım: python3 tools/metinler.py posts/<klasör>
Sahne HTML'lerindeki (scene.html, story.html, cover.html) tırnak içindeki metinleri, render.py spec/cover JSON'larındaki
"text"/"label"/"title" alanlarını ve caption.txt'yi çıkarır. Satır bölmeleri (\\n) birleştirilir: her ifade TAM CÜMLE olarak okunur.
Çıktıyı satır satır oku: yazım, noktalama, ünlü uyumu, ek yazımı (de/da, ki, mi), eksik kelime, anlam. Bir hata bile varsa yayınlama.
"""
import sys, os, re, json, glob

SKIP = re.compile(r"^(#|rgba?\(|[0-9.\s,%-]+$|Inter|Lora|Poppins|DejaVu|TeX|center|left|right|middle|top|bottom|alphabetic|round|butt|square|"
                  r"pop2?|whoosh|ding|tick|alarm|light|dark|soft|webgl2?|image/|file:|https?:|[a-z_]+\.(png|jpe?g|mp4|mp3|json|html)$)")
def from_html(path):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)            # yorumlar
    s = re.sub(r"(?m)//[^\n]*$", "", s)
    out = []
    for q, body in re.findall(r"(['\"`])((?:\\.|(?!\1).)*?)\1", s):
        t = body.replace("\\n", " / ").strip()
        if re.search(r"\d+px|utf-8|^-?\d", t): continue
        if len(t) < 2 or SKIP.match(t) or not re.search(r"[A-Za-zÇĞİÖŞÜçğıöşüâÂ]", t): continue
        if re.search(r"[{}=<>]|\$\{|=>|\)\s*;", t): continue          # kod parçası
        if re.match(r"^[a-z_][A-Za-z0-9_]*$", t): continue                # değişken/anahtar adı
        if re.match(r"^[a-zA-Z_]+(\.[a-zA-Z_]+)+$", t): continue
        if t in ("tr-TR", "en-US"): continue
        out.append(t)
    return out
def from_json(path):
    out = []
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("text", "label", "title", "desc", "name") and isinstance(v, str): out.append(v.replace("\n", " / "))
                elif k in ("items", "rows", "chips", "steps", "blocks", "names") and isinstance(v, list):
                    for it in v:
                        if isinstance(it, str): out.append(it)
                        elif isinstance(it, list): out.extend(str(x) for x in it if isinstance(x, str))
                        else: walk(it)
                else: walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(json.load(open(path, encoding="utf-8")))
    return [re.sub(r"\[\[!?|\]\]|\{\{|\}\}|\*\*", "", t) for t in out]

d = sys.argv[1]
seen = set()
for f in sorted(glob.glob(os.path.join(d, "*"))):
    n = os.path.basename(f)
    items = from_html(f) if n.endswith(".html") else from_json(f) if n.endswith(".json") else None
    if items is None: continue
    print(f"\n== {n}")
    for t in items:
        if (n, t) in seen: continue
        seen.add((n, t)); print("  •", t)
cap = os.path.join(d, "caption.txt")
if os.path.exists(cap):
    print("\n== caption.txt"); print(open(cap, encoding="utf-8").read())
