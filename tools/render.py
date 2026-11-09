"""Frame Lab içerik üretici.
Kullanım:
  python3 tools/render.py carousel spec.json out_dir   -> out_dir/1.jpg ... (1080x1350 JPEG)
  Statik gönderi: tek slaytlı carousel spec'i -> out_dir/1.jpg (sayfa sayacı olmadan)
  python3 tools/render.py story    spec.json out.jpg   -> 1080x1920 JPEG
  python3 tools/render.py reel     spec.json out.mp4 [voice_file]  -> 1080x1920 MP4, müzikli
Spec formatı için tools/PLAYBOOK.md'ye bak.
"""
import sys, os, json, asyncio, subprocess, tempfile, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import kare, INK, PAPER, LIME, SOFT, GREY, LIME_DARK

THEMES = {  # bg, fg, lead, grey, accent(dot), line, highlight(fg,bg,pad), card_bg
 "light": (PAPER, INK, "#3A3A36", "#6B6B65", LIME, "#D9D8D2", (INK, LIME, "0 12px"), "#FFFFFF"),
 "soft":  (SOFT, INK, "#33372B", "#5E6650", LIME_DARK, "#D3E3B5", (INK, LIME, "0 12px"), "#FFFFFF"),
 "dark":  (INK, PAPER, "#D9D8D2", GREY, LIME, "#26262C", (LIME, "transparent", "0"), "#1D1D22"),
}
def hl(text):  # [[...]] -> vurgu
    t = H.escape(text).replace("\n", "<br>")
    return t.replace("[[", '<span class="hl">').replace("]]", "</span>")

def css(theme, w, h):
    bg, fg, lead, grey, acc, line, (hf, hb, hp), cardbg = THEMES[theme]
    lab = LIME if theme == "dark" else LIME_DARK
    return f"""*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:{w}px;height:{h}px;background:{bg};color:{fg};font-family:'Inter',sans-serif;overflow:hidden}}
.s{{position:relative;width:{w}px;height:{h}px;padding:{'96px 88px' if h<1500 else '150px 90px 0'};display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center;font-size:26px;color:{grey};font-weight:500;letter-spacing:.04em}}
.brand{{display:flex;align-items:center;gap:14px;color:{fg};font-family:'Inter Display';font-weight:600;letter-spacing:.16em;font-size:24px}}
.dot{{width:14px;height:14px;border-radius:50%;background:{acc}}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:{40 if h<1500 else 48}px;padding-bottom:{40 if h<1500 else 300}px}}
.tag{{font-family:'Inter Display';font-weight:700;font-size:{30 if h<1500 else 36}px;letter-spacing:.12em;color:{lab}}}
h1{{font-family:'Inter Display';font-weight:800;font-size:{100 if h<1500 else 112}px;line-height:1.03;letter-spacing:-.03em}}
h2{{font-family:'Inter Display';font-weight:800;font-size:{76 if h<1500 else 88}px;line-height:1.06;letter-spacing:-.025em}}
.hl{{color:{hf};background:{hb};padding:{hp};border-radius:10px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.lead{{font-size:{38 if h<1500 else 44}px;line-height:1.4;color:{lead}}}
.card{{border-radius:32px;padding:40px 46px;background:{cardbg}}}
.card.out{{background:transparent;border:3px solid {lab}}}
.lbl{{font-size:26px;font-weight:600;letter-spacing:.08em;margin-bottom:16px;color:{grey}}}
.card.out .lbl{{color:{lab}}}
.ct{{font-size:{36 if h<1500 else 44}px;line-height:1.4}}
.ct.strong{{font-family:'Inter Display';font-weight:600}}
.pill{{display:inline-flex;font-family:'Inter Display';font-weight:700;font-size:40px;padding:18px 30px;border-radius:999px;background:{hb if hb!='transparent' else LIME};color:{INK}}}
.pill.muted{{background:{line};color:{fg}}}
.chip{{display:inline-block;padding:14px 26px;border:2px solid {fg if hb!='transparent' else acc};border-radius:999px;font-size:30px;font-weight:600;color:{fg if hb!='transparent' else acc};margin:0 14px 16px 0}}
.row{{display:flex;align-items:center;gap:28px;padding:18px 0;border-top:2px solid {line}}}
.rk{{width:150px;font-family:'Inter Display';font-weight:700;font-size:30px;color:{lab};letter-spacing:.06em}}
.rt{{font-family:'Inter Display';font-weight:700;font-size:38px}}
.rd{{font-size:27px;color:{grey};margin-top:6px}}
.foot{{position:absolute;left:{88 if h<1500 else 90}px;right:{88 if h<1500 else 90}px;bottom:{80 if h<1500 else 110}px;display:flex;justify-content:space-between;font-size:{26 if h<1500 else 30}px;color:{grey}}}
.sw{{color:{lab if theme=='dark' else fg};font-weight:600}}
.a{{opacity:1}}"""

def el(e, light):
    k = e["type"]; at = f' data-in="{e["at"]}"' if "at" in e else ""
    cls = ' class="a"' if "at" in e else ""
    if k == "kare":
        return f'<div{cls}{at} data-pop="1" style="margin-left:-30px">{kare(e.get("size",340), e.get("face","mutlu"), bg="none", light_bg=light)}</div>'
    if k in ("h1", "h2"):
        st = f' style="font-size:{e["size"]}px"' if "size" in e else ""
        return f'<{k}{cls}{at}{st}>{hl(e["text"])}</{k}>'
    if k == "tag":  return f'<div class="tag{" a" if at else ""}"{at}>{H.escape(e["text"])}</div>'
    if k == "lead": return f'<p class="lead{" a" if at else ""}"{at}>{hl(e["text"])}</p>'
    if k == "chips": return f'<div{cls}{at}>' + "".join(f'<span class="chip">{H.escape(c)}</span>' for c in e["items"]) + "</div>"
    if k == "pill": return f'<div{cls}{at}><span class="pill{" muted" if e.get("muted") else ""}">{H.escape(e["text"])}</span></div>'
    if k == "rows": return f'<div{cls}{at} style="border-bottom:2px solid rgba(127,127,127,.3)">' + "".join(
        f'<div class="row"><div class="rk">{H.escape(r[0])}</div><div><div class="rt">{H.escape(r[1])}</div><div class="rd">{H.escape(r[2])}</div></div></div>' for r in e["items"]) + "</div>"
    if k == "card":
        inner = H.escape(e["text"]).replace('"', "&quot;")
        body = (f'<div class="ct{" strong" if e.get("strong") else ""}" style="{("font-size:%spx" % e["size"]) if "size" in e else ""}" data-type="{e["typed"][0]},{e["typed"][1]}" data-full="{inner}"></div>'
                if "typed" in e else f'<div class="ct{" strong" if e.get("strong") else ""}" style="{("font-size:%spx" % e["size"]) if "size" in e else ""}">{H.escape(e["text"])}</div>')
        return f'<div class="card{" out" if e.get("outline") else ""}{" a" if at else ""}"{at}><div class="lbl">{H.escape(e.get("label",""))}</div>{body}</div>'
    raise ValueError("bilinmeyen öğe: " + k)

JS = """<script>
function ease(x){return 1-Math.pow(1-Math.min(Math.max(x,0),1),3)}
window.render=function(t){
 document.querySelectorAll('[data-in]').forEach(e=>{const s=parseFloat(e.dataset.in);const p=ease((t-s)/0.45);
   e.style.opacity=p; e.style.transform='translateY('+(40*(1-p))+'px) scale('+(e.dataset.pop?0.85+0.15*p:1)+')';});
 document.querySelectorAll('[data-type]').forEach(e=>{const [s,d]=e.dataset.type.split(',').map(parseFloat);
   const full=e.dataset.full; const n=Math.round(full.length*Math.min(Math.max((t-s)/d,0),1));
   e.textContent=full.slice(0,n)+(t>=s && n<full.length && Math.floor(t*3)%2==0?'|':'');});
};
</script>"""

def page(theme, elements, w, h, top=None, foot_right=None):
    light = theme in ("light", "soft")
    t = f'<div class="top"><div class="brand"><span class="dot"></span>FRAME/LAB</div><div>{top or ""}</div></div>' if h < 1500 else ""
    fr = foot_right if foot_right is not None else ("" if h >= 1500 else "Kaydır →")
    foot = f'<div class="foot"><span>@frame.labo</span><span class="sw">{H.escape(fr) if fr else ("FRAME/LAB" if h>=1500 else "")}</span></div>'
    body = "".join(el(e, light) for e in elements)
    return f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{css(theme,w,h)}</style></head><body><div class="s">{t}<div class="main">{body}</div>{foot}</div>{JS}</body></html>'

async def _shots(pages, w, h, paths, t_final=True):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": w, "height": h})
        tmp = tempfile.mkdtemp()
        for i, (htm, out) in enumerate(zip(pages, paths)):
            f = f"{tmp}/p{i}.html"; open(f, "w").write(htm)
            await pg.goto("file://" + f); await pg.wait_for_timeout(250)
            await pg.evaluate("render(999)")
            await pg.screenshot(path=out, type="jpeg", quality=92)
        await b.close()

def carousel(spec, out_dir):
    os.makedirs(out_dir, exist_ok=True); sl = spec["slides"]; n = len(sl)
    pages = [page(s["theme"], s["elements"], 1080, 1350, (f"{i+1}/{n}" if n > 1 else ""), ("Takip et" if i == n-1 else None) if n > 1 else "Kaydet") for i, s in enumerate(sl)]
    asyncio.run(_shots(pages, 1080, 1350, [f"{out_dir}/{i+1}.jpg" for i in range(n)]))

def story(spec, out):
    asyncio.run(_shots([page(spec["theme"], spec["elements"], 1080, 1920, foot_right=spec.get("foot_right", ""))], 1080, 1920, [out]))

async def _reel_frames(spec, tmp):
    from playwright.async_api import async_playwright
    files = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        for i, sc in enumerate(spec["scenes"]):
            f = f"{tmp}/s{i}.html"; open(f, "w").write(page(sc["theme"], sc["elements"], 1080, 1920))
            await pg.goto("file://" + f); await pg.wait_for_timeout(250)
            n = int(round(sc["duration"] * 30)); part = f"{tmp}/s{i}.tmp.mp4"
            pr = subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate","30","-c:v","mjpeg","-i","-",
                "-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-r","30",part], stdin=subprocess.PIPE)
            for k in range(n):
                await pg.evaluate(f"render({k/30})"); pr.stdin.write(await pg.screenshot(type="jpeg", quality=92))
            pr.stdin.close()
            if pr.wait() != 0: raise RuntimeError("ffmpeg sahne hatası")
            os.replace(part, f"{tmp}/s{i}.mp4"); files.append(f"{tmp}/s{i}.mp4")
        await b.close()
    return files

def reel(spec, out, voice=None):
    tmp = tempfile.mkdtemp(); files = asyncio.run(_reel_frames(spec, tmp))
    open(f"{tmp}/l.txt", "w").write("".join(f"file '{f}'\n" for f in files))
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{tmp}/l.txt","-c","copy",f"{tmp}/v.mp4"], check=True)
    T = sum(s["duration"] for s in spec["scenes"]); here = os.path.dirname(os.path.abspath(__file__))
    subprocess.run(["python3", f"{here}/music.py", str(T), f"{tmp}/m.wav"], check=True, stdout=subprocess.DEVNULL)
    if voice:  # spec["voice_segments"]: [[src_start, src_end, place_at], ...]
        segs = spec["voice_segments"]; parts = []; fc = f"[1:a]aresample=44100,highpass=f=80,acompressor=threshold=-18dB:ratio=2.5:attack=5:release=120,volume=1.6,asplit={len(segs)}" + "".join(f"[s{i}]" for i in range(len(segs))) + ";"
        for i, (a, b2, at) in enumerate(segs):
            fc += f"[s{i}]atrim={a}:{b2},asetpts=PTS-STARTPTS,adelay={int(at*1000)}|{int(at*1000)}[v{i}];"; parts.append(f"[v{i}]")
        fc += "".join(parts) + f"amix=inputs={len(segs)}:normalize=0,apad=whole_dur={T},atrim=0:{T}[vo];[0:a]volume=0.45[m];[vo]asplit=2[vk][vm];[m][vk]sidechaincompress=threshold=0.025:ratio=10:attack=15:release=350[md];[md][vm]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5[out]"
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"{tmp}/m.wav","-i",voice,"-filter_complex",fc,"-map","[out]","-ar","44100",f"{tmp}/a.wav"], check=True)
    else:
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"{tmp}/m.wav","-af","volume=0.8,loudnorm=I=-16:TP=-1.5","-ar","44100",f"{tmp}/a.wav"], check=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"{tmp}/v.mp4","-i",f"{tmp}/a.wav","-map","0:v","-map","1:a","-c:v","copy","-af","apad",
                    "-c:a","aac","-b:a","192k","-t",str(T),"-movflags","+faststart",out+".tmp.mp4"], check=True)
    os.replace(out + ".tmp.mp4", out)

if __name__ == "__main__":
    mode, spec_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
    spec = json.load(open(spec_path))
    {"carousel": lambda: carousel(spec, out), "story": lambda: story(spec, out),
     "reel": lambda: reel(spec, out, sys.argv[4] if len(sys.argv) > 4 else None)}[mode]()
    print("ok", out)
