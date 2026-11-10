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
.a{{opacity:1}}
.main.center{{text-align:center;align-items:center}} .main.bottom{{justify-content:flex-end}}
.pat-grid{{background-image:linear-gradient({line} 2px,transparent 2px),linear-gradient(90deg,{line} 2px,transparent 2px);background-size:72px 72px;background-position:-2px -2px}}
.pat-dots{{background-image:radial-gradient({line} 3px,transparent 3.5px);background-size:44px 44px}}
.bignum{{font-family:'Inter Display';font-weight:800;line-height:.82;letter-spacing:-.06em;color:{lab if theme=='dark' else fg}}}
.bignum .u{{display:inline-block;border-bottom:{'0' if theme=='dark' else '28px solid '+LIME};line-height:.7}}
.blabel{{font-family:'Inter Display';font-weight:700;font-size:{44 if h<1500 else 52}px;margin-top:10px}}
.chat{{display:flex;flex-direction:column;gap:22px;width:100%}}
.bub{{max-width:86%;padding:26px 30px;border-radius:30px;font-size:{32 if h<1500 else 40}px;line-height:1.35;text-align:left}}
.bub.you{{align-self:flex-end;background:{fg};color:{bg};border-bottom-right-radius:8px}}
.bub.ai{{align-self:flex-start;background:{cardbg};color:{fg};border-bottom-left-radius:8px;{'' if theme=='dark' else 'box-shadow:0 2px 0 '+line}}}
.bub .who{{display:block;font-size:22px;font-weight:700;letter-spacing:.08em;opacity:.6;margin-bottom:8px}}
.cmp{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px;width:100%;text-align:left}}
.cmp .c{{border-radius:28px;padding:32px 30px;background:{cardbg}}}
.cmp .c.good{{background:{LIME};color:{INK}}}
.cmp .k{{font-family:'Inter Display';font-weight:800;font-size:28px;letter-spacing:.08em;margin-bottom:14px}}
.cmp .t{{white-space:pre-line;font-size:{30 if h<1500 else 36}px;line-height:1.38}}
.steps{{display:flex;flex-direction:column;gap:26px;width:100%;text-align:left}}
.step{{display:flex;gap:30px;align-items:flex-start}}
.step .n{{font-family:'Inter Display';font-weight:800;font-size:{110 if h<1500 else 130}px;line-height:.8;color:transparent;-webkit-text-stroke:3px {lab if theme=='dark' else fg};min-width:150px}}
.step .st{{font-family:'Inter Display';font-weight:700;font-size:{40 if h<1500 else 46}px;line-height:1.15}}
.step .sd{{font-size:{28 if h<1500 else 34}px;color:{grey};margin-top:6px;line-height:1.35}}
.quote{{font-family:'Inter Display';font-weight:800;font-size:{84 if h<1500 else 96}px;line-height:1.08;letter-spacing:-.025em}}
.qm{{font-family:'Inter Display';font-weight:800;font-size:260px;line-height:.6;color:{lab if theme=='dark' else LIME_DARK};height:120px}}
.tiles{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;width:100%;text-align:left}}
.tile{{background:{cardbg};border-radius:28px;padding:30px 28px;min-height:{220 if h<1500 else 280}px;display:flex;flex-direction:column;justify-content:space-between}}
.tile .ti{{font-family:'Inter Display';font-weight:800;font-size:52px;color:{lab if theme=='dark' else LIME_DARK}}}
.tile .tt{{font-family:'Inter Display';font-weight:700;font-size:{32 if h<1500 else 38}px;line-height:1.2}}
.sticker{{position:absolute;top:{150 if h<1500 else 190}px;right:{70 if h<1500 else 80}px;width:230px;height:230px;border-radius:50%;background:{LIME};color:{INK};display:flex;align-items:center;justify-content:center;text-align:center;font-family:'Inter Display';font-weight:800;font-size:38px;line-height:1.05;transform:rotate(12deg);z-index:3;padding:20px}}
.peek{{position:absolute;right:-80px;bottom:{110 if h<1500 else 200}px;z-index:1;transform:rotate(-10deg)}}
.frame i{{position:absolute;width:90px;height:90px;border-color:{lab if theme=='dark' else fg};border-style:solid;border-width:0;z-index:2}}
.frame .tl{{top:{150 if h<1500 else 120}px;left:56px;border-top-width:8px;border-left-width:8px}} .frame .tr{{top:{150 if h<1500 else 120}px;right:56px;border-top-width:8px;border-right-width:8px}}
.frame .bl{{bottom:{140 if h<1500 else 190}px;left:56px;border-bottom-width:8px;border-left-width:8px}} .frame .br{{bottom:{140 if h<1500 else 190}px;right:56px;border-bottom-width:8px;border-right-width:8px}}
.phone{{position:absolute;right:-30px;bottom:{-180 if h<1500 else -60}px;width:{430 if h<1500 else 500}px;height:{860 if h<1500 else 1000}px;border-radius:64px;background:{INK};border:14px solid {'#2A2A30' if theme=='dark' else INK};transform:rotate(-7deg);z-index:1;padding:70px 26px 26px;color:{PAPER};display:flex;flex-direction:column;gap:18px;box-shadow:0 30px 60px rgba(0,0,0,.25)}}
.phone:before{{content:'';position:absolute;top:22px;left:50%;width:120px;height:30px;border-radius:20px;background:#000;transform:translateX(-50%)}}
.phone .pt{{font-family:'Inter Display';font-weight:800;font-size:36px}}
.phone .pb{{border-radius:22px;background:#26262C;padding:20px;font-size:26px;line-height:1.3}}
.phone .pb.acc{{background:{LIME};color:{INK};font-weight:700}}
.narrow{{max-width:{560 if h<1500 else 600}px}}
.h1o{{color:transparent;-webkit-text-stroke:3px {fg}}}"""

def el(e, light):
    k = e["type"]; at = f' data-in="{e["at"]}"' if "at" in e else ""
    cls = ' class="a"' if "at" in e else ""
    if k == "kare":
        return f'<div{cls}{at} data-pop="1" style="margin-left:-30px">{kare(e.get("size",340), e.get("face","mutlu"), bg="none", light_bg=light)}</div>'
    if k in ("h1", "h2"):
        st = f' style="font-size:{e["size"]}px"' if "size" in e else ""
        oc = ' class="h1o"' if e.get("outline") else ""
        cl = (cls[:-1] + (" h1o" if e.get("outline") else "") + '"') if cls else oc
        nar = '<div class="narrow">' if e.get("narrow") else ""
        return f'{nar}<{k}{cl}{at}{st}>{hl(e["text"])}</{k}>' + ("</div>" if nar else "")
    if k == "tag":  return f'<div class="tag{" a" if at else ""}"{at}>{H.escape(e["text"])}</div>'
    if k == "lead": return f'<p class="lead{" a" if at else ""}{" narrow" if e.get("narrow") else ""}"{at}>{hl(e["text"])}</p>'
    if k == "chips": return f'<div{cls}{at}>' + "".join(f'<span class="chip">{H.escape(c)}</span>' for c in e["items"]) + "</div>"
    if k == "pill": return f'<div{cls}{at}><span class="pill{" muted" if e.get("muted") else ""}">{H.escape(e["text"])}</span></div>'
    if k == "rows": return f'<div{cls}{at} style="border-bottom:2px solid rgba(127,127,127,.3)">' + "".join(
        f'<div class="row"><div class="rk">{H.escape(r[0])}</div><div><div class="rt">{H.escape(r[1])}</div><div class="rd">{H.escape(r[2])}</div></div></div>' for r in e["items"]) + "</div>"
    if k == "card":
        inner = H.escape(e["text"]).replace('"', "&quot;")
        body = (f'<div class="ct{" strong" if e.get("strong") else ""}" style="{("font-size:%spx" % e["size"]) if "size" in e else ""}" data-type="{e["typed"][0]},{e["typed"][1]}" data-full="{inner}"></div>'
                if "typed" in e else f'<div class="ct{" strong" if e.get("strong") else ""}" style="{("font-size:%spx" % e["size"]) if "size" in e else ""}">{H.escape(e["text"])}</div>')
        return f'<div class="card{" out" if e.get("outline") else ""}{" a" if at else ""}"{at}><div class="lbl">{H.escape(e.get("label",""))}</div>{body}</div>'
    if k == "bignum":
        sz = e.get("size", 420 if True else 0)
        cnt = f' data-count="{e["count_at"]}" data-full="{H.escape(e["text"])}"' if "count_at" in e else ""
        return f'<div{cls}{at}><div class="bignum" style="font-size:{sz}px"><span class="u"{cnt}>{H.escape(e["text"])}</span></div>' + (f'<div class="blabel">{hl(e["label"])}</div>' if e.get("label") else "") + "</div>"
    if k == "chat":
        out = ""
        for who, txt in e["items"]:
            nm = e.get("names", {}).get(who, "SEN" if who == "you" else "YAPAY ZEKÂ")
            out += f'<div class="bub {who}"><span class="who">{H.escape(nm)}</span>{H.escape(txt)}</div>'
        return f'<div class="chat{" a" if at else ""}"{at}>{out}</div>'
    if k == "compare":
        L, R = e["left"], e["right"]
        ts = f' style="font-size:{e["size"]}px;font-family:\'Inter Display\';font-weight:800;line-height:1.1"' if "size" in e else ""
        return f'<div class="cmp{" a" if at else ""}"{at}><div class="c"><div class="k">{H.escape(L["label"])}</div><div class="t"{ts}>{H.escape(L["text"])}</div></div><div class="c good"><div class="k">{H.escape(R["label"])}</div><div class="t"{ts}>{H.escape(R["text"])}</div></div></div>'
    if k == "steps":
        return f'<div class="steps{" a" if at else ""}"{at}>' + "".join(f'<div class="step"><div class="n">{i+1:02d}</div><div><div class="st">{H.escape(t)}</div>' + (f'<div class="sd">{H.escape(d)}</div>' if d else "") + "</div></div>" for i, (t, d) in enumerate(e["items"])) + "</div>"
    if k == "quote":
        return f'<div{cls}{at}><div class="qm">“</div><div class="quote">{hl(e["text"])}</div></div>'
    if k == "tiles":
        return f'<div class="tiles{" a" if at else ""}"{at}>' + "".join(f'<div class="tile"><div class="ti">{H.escape(t[0])}</div><div class="tt">{H.escape(t[1])}</div></div>' for t in e["items"]) + "</div>"
    if k == "sticker":
        return f'<div class="sticker">{hl(e["text"])}</div>'
    if k == "kare_peek":
        return f'<div class="peek">{kare(e.get("size",620), e.get("face","goz"), bg="none", light_bg=light)}</div>'
    if k == "phone":
        blocks = "".join(f'<div class="pb{" acc" if i == e.get("accent", -1) else ""}">{H.escape(b)}</div>' for i, b in enumerate(e.get("blocks", [])))
        return f'<div class="phone"><div class="pt">{H.escape(e.get("title",""))}</div>{blocks}</div>'
    raise ValueError("bilinmeyen öğe: " + k)

JS = """<script>
function ease(x){return 1-Math.pow(1-Math.min(Math.max(x,0),1),3)}
window.render=function(t){
 document.querySelectorAll('[data-in]').forEach(e=>{const s=parseFloat(e.dataset.in);const p=ease((t-s)/0.45);
   e.style.opacity=p; e.style.transform='translateY('+(40*(1-p))+'px) scale('+(e.dataset.pop?0.85+0.15*p:1)+')';});
 document.querySelectorAll('[data-type]').forEach(e=>{const [s,d]=e.dataset.type.split(',').map(parseFloat);
   const full=e.dataset.full; const n=Math.round(full.length*Math.min(Math.max((t-s)/d,0),1));
   e.textContent=full.slice(0,n)+(t>=s && n<full.length && Math.floor(t*3)%2==0?'|':'');});
 document.querySelectorAll('[data-count]').forEach(e=>{const s=parseFloat(e.dataset.count);const full=e.dataset.full;const m=full.match(/[0-9]+/);if(!m)return;
   const p=ease((t-s)/0.9);const v=Math.round(parseInt(m[0])*p);e.textContent=full.replace(m[0],String(v));});
};
</script>"""

ABS = ("sticker", "kare_peek", "phone")
def page(theme, elements, w, h, top=None, foot_right=None, align="", pattern="", frame=False):
    light = theme in ("light", "soft")
    t = f'<div class="top"><div class="brand"><span class="dot"></span>FRAME/LAB</div><div>{top or ""}</div></div>' if h < 1500 else ""
    fr = foot_right if foot_right is not None else ("" if h >= 1500 else "Kaydır →")
    foot = f'<div class="foot"><span>@frame.labo</span><span class="sw">{H.escape(fr) if fr else ("FRAME/LAB" if h>=1500 else "")}</span></div>'
    body = "".join(el(e, light) for e in elements if e["type"] not in ABS)
    deco = "".join(el(e, light) for e in elements if e["type"] in ABS)
    fr = '<div class="frame"><i class="tl"></i><i class="tr"></i><i class="bl"></i><i class="br"></i></div>' if frame else ""
    pc = f" pat-{pattern}" if pattern else ""
    return f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{css(theme,w,h)}</style></head><body><div class="s{pc}">{fr}{deco}{t}<div class="main {align}" style="position:relative;z-index:2">{body}</div>{foot}</div>{JS}</body></html>'

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
    pages = [page(s["theme"], s["elements"], 1080, 1350, (f"{i+1}/{n}" if n > 1 else ""), s.get("foot_right", ("Takip et" if i == n-1 else None) if n > 1 else "Kaydet"), s.get("align",""), s.get("pattern",""), s.get("frame",False)) for i, s in enumerate(sl)]
    asyncio.run(_shots(pages, 1080, 1350, [f"{out_dir}/{i+1}.jpg" for i in range(n)]))

def story(spec, out):
    asyncio.run(_shots([page(spec["theme"], spec["elements"], 1080, 1920, foot_right=spec.get("foot_right", ""), align=spec.get("align",""), pattern=spec.get("pattern",""), frame=spec.get("frame",False))], 1080, 1920, [out]))

async def _reel_frames(spec, tmp):
    from playwright.async_api import async_playwright
    files = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        for i, sc in enumerate(spec["scenes"]):
            f = f"{tmp}/s{i}.html"; open(f, "w").write(page(sc["theme"], sc["elements"], 1080, 1920, align=sc.get("align",""), pattern=sc.get("pattern",""), frame=sc.get("frame",False)))
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

MOTION_JS = """<script>
const S=__SCENES__, K=__KARE__, TR=0.6;
function eio(x){x=Math.min(Math.max(x,0),1);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}
function lerp(a,b,p){return a+(b-a)*p}
function setFace(f){document.querySelectorAll('#kare .f').forEach(e=>e.style.display=(e.dataset.face==f?'block':'none'))}
window.render=function(t){
  let i=0; for(let k=0;k<S.length;k++){ if(t>=S[k].start) i=k; }
  let off=i*1080, sw=0;
  const end=S[i].start+S[i].dur;
  if(i<S.length-1 && t>end-TR){ sw=eio((t-(end-TR))/TR); off=(i+sw)*1080; }
  document.getElementById('strip').style.transform='translateX('+(-off)+'px)';
  document.querySelectorAll('iframe').forEach((f,k)=>{ try{ f.contentWindow.render(t-S[k].start) }catch(e){} });
  // Kare
  const a=K[i], b=(i<S.length-1?K[i+1]:K[i]); const el=document.getElementById('kare');
  if(!a && !b){ el.style.opacity=0; return; }
  const A=a||{x:b.x,y:-500,size:b.size,face:b.face}, B=b||{x:A.x,y:-500,size:A.size,face:A.face};
  let x=A.x,y=A.y,sz=A.size,rot=0,face=A.face;
  const local=t-S[i].start;
  const intro=(i==0)?eio(local/0.7):1;
  if(sw>0){ x=lerp(A.x,B.x,sw); y=lerp(A.y,B.y,sw)-Math.sin(Math.PI*sw)*260; sz=lerp(A.size,B.size,sw); rot=Math.sin(Math.PI*sw)*-18; face=sw<.5?A.face:B.face; }
  else { y+=Math.sin(t*2.6)*14; rot=Math.sin(t*1.7)*4; }
  if(i==0 && local<0.7){ y=lerp(A.y+500,A.y,intro); }
  const bl=(t%3.1); if(bl>2.95 && sw==0) face='blink';
  const land=(sw==0 && local<0.25 && i>0)?(1-local/0.25):0;
  const sq=1+land*0.12;
  el.style.opacity=1; setFace(face);
  el.style.transform='translate('+x+'px,'+y+'px) rotate('+rot+'deg) scale('+(sz/400)*sq+','+(sz/400)/sq+')';
};
</script>"""

def reel_motion(spec, out, voice=None):
    import tempfile
    sc = spec["scenes"]; t0 = 0.0; S = []; panels = ""
    for i, s_ in enumerate(sc):
        S.append({"start": round(t0, 3), "dur": s_["duration"]})
        htm = page(s_["theme"], s_["elements"], 1080, 1920, align=s_.get("align",""), pattern=s_.get("pattern",""), frame=s_.get("frame",False))
        panels += f'<iframe srcdoc="{H.escape(htm)}" style="width:1080px;height:1920px;border:0;flex:none" scrolling="no"></iframe>'
        t0 += s_["duration"]
    T = t0
    K = [s_.get("kare") for s_ in sc]
    faces = "".join(f'<div class="f" data-face="{f}" style="display:none">{kare(400, f, bg="none", light_bg=False).replace(chr(34)+"#F5F4F0"+chr(34)+"></rect>"+chr(10)+"</svg>", chr(34)+"#8A8A82"+chr(34)+"></rect>"+chr(10)+"</svg>")}</div>' for f in ["mutlu","goz","saskin","dusunen","fikir","calisiyor","blink"])
    js = MOTION_JS.replace("__SCENES__", json.dumps(S)).replace("__KARE__", json.dumps(K))
    doc = f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#111114}}#strip{{display:flex;width:{1080*len(sc)}px;height:1920px;will-change:transform}}#kare{{position:absolute;left:0;top:0;width:400px;height:400px;transform-origin:0 0;z-index:9;pointer-events:none}}</style></head><body><div id="strip">{panels}</div><div id="kare">{faces}</div>{js}</body></html>'
    tmp = tempfile.mkdtemp(); f = f"{tmp}/m.html"; open(f, "w").write(doc)
    async def go():
        from playwright.async_api import async_playwright
        async with async_playwright() as p:
            b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
            pg = await b.new_page(viewport={"width":1080,"height":1920})
            await pg.goto("file://"+f); await pg.wait_for_timeout(1200)
            n = int(round(T*30)); part = f"{tmp}/v.tmp.mp4"
            pr = subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate","30","-c:v","mjpeg","-i","-",
                "-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-r","30",part], stdin=subprocess.PIPE)
            for k in range(n):
                await pg.evaluate(f"render({k/30})"); pr.stdin.write(await pg.screenshot(type="jpeg", quality=92))
            pr.stdin.close()
            if pr.wait() != 0: raise RuntimeError("ffmpeg")
            os.replace(part, f"{tmp}/v.mp4")
            for ct in spec.get("stills", []):
                await pg.evaluate(f"render({ct})"); await pg.screenshot(path=f"{os.path.splitext(out)[0]}_still_{ct}.jpg", type="jpeg", quality=92)
            await b.close()
    asyncio.run(go())
    here = os.path.dirname(os.path.abspath(__file__))
    subprocess.run(["python3", f"{here}/music.py", str(T), f"{tmp}/m.wav"], check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"{tmp}/m.wav","-af","volume=0.8,loudnorm=I=-16:TP=-1.5","-ar","44100",f"{tmp}/a.wav"], check=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"{tmp}/v.mp4","-i",f"{tmp}/a.wav","-map","0:v","-map","1:a","-c:v","copy","-af","apad",
                    "-c:a","aac","-b:a","192k","-t",str(T),"-movflags","+faststart",out+".tmp.mp4"], check=True)
    os.replace(out + ".tmp.mp4", out)

if __name__ == "__main__":
    mode, spec_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
    spec = json.load(open(spec_path))
    {"carousel": lambda: carousel(spec, out), "story": lambda: story(spec, out),
     "reel": lambda: (reel_motion(spec, out) if spec.get("motion") else reel(spec, out, sys.argv[4] if len(sys.argv) > 4 else None))}[mode]()
    print("ok", out)
