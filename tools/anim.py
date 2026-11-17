"""Frame Lab serbest animasyon yakalayıcı: kendi çizdiğin HTML sahnesini müzikli MP4'e çevirir.
Kullanım:
  python3 tools/anim.py sahne.html out.mp4 [--dur 10] [--style funk] [--seed 3] [--fps 30] [--w 1080 --h 1920] [--stills 0,2.5,7]
Sahne sayfası şunları tanımlar:
  window.render(t)   -> t saniyesindeki kareyi çizer (canvas, SVG ya da DOM; deterministik olmalı)
  window.DUR         -> (isteğe bağlı) süre, --dur yoksa kullanılır
  window.SFX         -> (isteğe bağlı) [[sn, "pop"|"pop2"|"whoosh"|"ding"|"tick"|"alarm"], ...]
Çizgi film, oyun (piksel), ikonlu motion ve 3D kompozit sahneler için kullanılır; tools/scenes/ altındaki örneklere bak.
"""
import sys, os, json, asyncio, subprocess, tempfile, argparse

ap = argparse.ArgumentParser()
ap.add_argument("page"); ap.add_argument("out")
ap.add_argument("--dur", type=float); ap.add_argument("--style", default=None); ap.add_argument("--seed", type=int, default=7)
ap.add_argument("--fps", type=int, default=30); ap.add_argument("--w", type=int, default=1080); ap.add_argument("--h", type=int, default=1920)
ap.add_argument("--stills", default=""); ap.add_argument("--nomusic", action="store_true")
a = ap.parse_args()
here = os.path.dirname(os.path.abspath(__file__))
tmp = tempfile.mkdtemp()

async def go():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox", "--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
        pg = await b.new_page(viewport={"width": a.w, "height": a.h})
        await pg.goto("file://" + os.path.abspath(a.page)); await pg.wait_for_timeout(900)
        dur = a.dur or await pg.evaluate("window.DUR||10")
        sfx = await pg.evaluate("window.SFX||[]")
        n = int(round(dur * a.fps)); part = f"{tmp}/v.mp4"
        pr = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(a.fps), "-c:v", "mjpeg", "-i", "-",
                               "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(a.fps), part], stdin=subprocess.PIPE)
        for k in range(n):
            await pg.evaluate(f"window.render({k / a.fps})")
            pr.stdin.write(await pg.screenshot(type="jpeg", quality=92))
        pr.stdin.close()
        if pr.wait() != 0: raise RuntimeError("ffmpeg")
        for ct in [float(x) for x in a.stills.split(",") if x.strip()]:
            await pg.evaluate(f"window.render({ct})"); await pg.screenshot(path=f"{os.path.splitext(a.out)[0]}_still_{ct}.jpg", type="jpeg", quality=92)
        await b.close()
        return dur, sfx
dur, sfx = asyncio.run(go())
if a.nomusic:
    os.replace(f"{tmp}/v.mp4", a.out)
else:
    json.dump(sfx, open(f"{tmp}/sfx.json", "w"))
    cmd = ["python3", f"{here}/music.py", str(dur), f"{tmp}/m.wav", f"{tmp}/sfx.json"] + ([a.style] if a.style else ["-"]) + [str(a.seed)]
    if not a.style: cmd[5] = "x"  # geçersiz stil -> tohuma göre seçilir
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{tmp}/v.mp4", "-i", f"{tmp}/m.wav", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-shortest", "-movflags", "+faststart", a.out], check=True)
print("ok", a.out)
