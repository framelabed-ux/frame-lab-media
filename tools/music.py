"""Frame Lab müzik üreticisi (telifsiz, tamamen sentez).
Kullanım: python3 music.py <saniye> <out.wav> [olaylar.json|-] [stil] [tohum]
  olaylar.json: ses efektleri [[zaman, "whoosh"|"pop"|"pop2"|"ding"|"tick"|"alarm"], ...], müziği kısmak için [zaman, "mute", süre]  ("-" = yok)
  stil: pop | lofi | house | synthwave | minimal | trap | funk | ambient  (yoksa tohuma göre seçilir)
  tohum: tamsayı; aynı stil + tohum aynı müziği verir, farklı tohum farklı ton/melodi/ritim verir.
"""
import numpy as np, wave, sys, json, zlib

sr = 44100
T = float(sys.argv[1]) if len(sys.argv) > 1 else 30.0
out_name = sys.argv[2] if len(sys.argv) > 2 else "music.wav"
ev_path = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] != "-" else None
STYLES = ["pop", "lofi", "house", "synthwave", "minimal", "trap", "funk", "ambient"]
seed = int(sys.argv[5]) if len(sys.argv) > 5 else 7
style = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] in STYLES else STYLES[seed % len(STYLES)]
rng = np.random.default_rng(seed)
N = int(sr * T); t = np.arange(N) / sr
mix = np.zeros(N)

def add(start, sig, gain):
    i = int(start * sr); j = min(N, i + len(sig))
    if 0 <= i < N: mix[i:j] += sig[:j - i] * gain
mtf = lambda m: 440 * 2 ** ((m - 69) / 12)
def env(n, a=0.005, dec=6.0):
    tt = np.arange(n) / sr
    return np.minimum(tt / max(a, 1e-4), 1) * np.exp(-tt * dec)
def lp(x, k):  # basit alçak geçiren
    return np.convolve(x, np.ones(k) / k, "same") if k > 1 else x

# ---------- çalgılar ----------
def kick(punch=1.0, d=0.35):
    tt = np.arange(int(sr * d)) / sr; f = 45 + 95 * punch * np.exp(-tt * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-tt * 9)
def k808(f0, d):
    tt = np.arange(int(sr * d)) / sr; f = f0 * (1 + 1.5 * np.exp(-tt * 40))
    return np.tanh(1.6 * np.sin(2 * np.pi * np.cumsum(f) / sr)) * np.exp(-tt * 2.2)
def hat(open_=False, bright=1.0):
    d = 0.25 if open_ else 0.08; n = rng.standard_normal(int(sr * d))
    n = n - lp(n, max(2, int(4 / bright)))
    return n * np.exp(-np.arange(len(n)) / sr * (14 if open_ else 45))
def snare(tone=200, d=0.22):
    n = rng.standard_normal(int(sr * d)); tt = np.arange(len(n)) / sr
    return (0.7 * lp(n, 2) + 0.4 * np.sin(2 * np.pi * tone * tt)) * np.exp(-tt * 18)
def clap():
    n = rng.standard_normal(int(sr * 0.2)); e = np.zeros(len(n))
    for o in (0, 0.012, 0.024):
        i = int(o * sr); e[i:] += np.exp(-np.arange(len(n) - i) / sr * 25)
    return lp(n, 3) * e / 3
def shaker():
    n = rng.standard_normal(int(sr * 0.06)); n = n - lp(n, 3)
    return n * np.sin(np.linspace(0, np.pi, len(n)))
def tone(f, d, dec=6, harm=(1, .4, .15), a=0.005):
    n = int(sr * d); tt = np.arange(n) / sr
    s = sum(h * np.sin(2 * np.pi * f * (k + 1) * tt) for k, h in enumerate(harm))
    return s * env(n, a, dec)
def saw(f, d, dec=3, det=0.006, a=0.01):
    n = int(sr * d); tt = np.arange(n) / sr; s = 0
    for dd in (-det, 0, det):
        ph = (f * (1 + dd) * tt) % 1.0; s = s + (2 * ph - 1)
    return lp(s / 3, 6) * env(n, a, dec)
def rhodes(f, d):
    n = int(sr * d); tt = np.arange(n) / sr
    s = np.sin(2 * np.pi * f * tt + 1.2 * np.exp(-tt * 4) * np.sin(2 * np.pi * f * 2 * tt))
    return s * env(n, 0.006, 2.2) * (1 + 0.15 * np.sin(2 * np.pi * 4.5 * tt))
def pluck(f, d):
    n = int(sr * d); p = max(2, int(sr / f)); buf = rng.uniform(-1, 1, p); y = np.zeros(n)
    for i in range(n):
        y[i] = buf[i % p]; buf[i % p] = 0.5 * (buf[i % p] + buf[(i + 1) % p]) * 0.996
    return y
def pad(f, d):
    n = int(sr * d); tt = np.arange(n) / sr
    s = sum(np.sin(2 * np.pi * f * m * tt + rng.uniform(0, 6)) for m in (1, 1.003, 0.997, 2.001))
    a = np.minimum(tt / 0.6, 1) * np.minimum((d - tt) / 0.6, 1)
    return s / 4 * np.clip(a, 0, 1)

# ---------- stiller ----------
MAJ, MIN = [0, 2, 4, 5, 7, 9, 11], [0, 2, 3, 5, 7, 8, 10]
PROGS = {
    "minor": [[0, 3, 7], [-4, 0, 3], [-9, -5, 0], [-2, 2, 5]],          # i VI III VII
    "minor2": [[0, 3, 7], [5, 8, 12], [-2, 2, 5], [3, 7, 10]],           # i iv VII III
    "major": [[0, 4, 7], [-5, -1, 2], [-3, 0, 4], [-7, -3, 0]],          # I V vi IV
    "jazz": [[2, 5, 9, 12], [7, 11, 14, 17], [0, 4, 7, 11], [9, 12, 16, 19]],  # ii7 V7 Imaj7 vi7
}
P = {  # bpm aralığı, ilerleme, perde aralığı
    "pop": ((116, 124), "minor", (55, 60)), "lofi": ((76, 86), "jazz", (52, 57)),
    "house": ((122, 126), "minor2", (53, 58)), "synthwave": ((96, 104), "minor", (50, 55)),
    "minimal": ((106, 114), "major", (57, 62)), "trap": ((136, 144), "minor2", (50, 54)),
    "funk": ((104, 112), "minor", (52, 56)), "ambient": ((70, 80), "major", (55, 60)),
}[style]
bpm = float(rng.integers(P[0][0], P[0][1] + 1)); beat = 60 / bpm; bar = 4 * beat
root = int(rng.integers(P[2][0], P[2][1] + 1)); prog = PROGS[P[1]]
if rng.random() < 0.5: prog = prog[2:] + prog[:2]
nbars = int(np.ceil(T / bar)) + 1
scale = MIN if P[1] in ("minor", "minor2") else MAJ
motif = [int(x) for x in rng.choice([0, 2, 4, 1, 3, 4, 2, 0], 8)]  # melodi motifi (dizi basamakları)
def sdeg(d, oct=0): return root + 12 * oct + scale[d % 7] + 12 * (d // 7)

for b in range(nbars):
    s0 = b * bar; ch = prog[b % len(prog)]; r = root + ch[0]; intro = b == 0
    if style == "pop":
        for q in range(4):
            if not intro or q >= 2: add(s0 + q * beat, kick(), 0.9)
            if q in (1, 3) and not intro: add(s0 + q * beat, clap(), 0.35)
        for e in range(8):
            add(s0 + e * beat / 2, hat(e % 2 == 1), 0.09)
            if e % 2 == 1 or e == 0: add(s0 + e * beat / 2, tone(mtf(r - 12), beat / 2 * .9, 6, (1, .5, .2)), 0.3)
        for pos in ((0, 1.5, 3, 3.5) if not intro else (0,)):
            for m in ch: add(s0 + pos * beat, tone(mtf(root + m + 12), 0.4, 7, (1, .3, .1)), 0.08)
        if b >= 1:
            for k in range(8): add(s0 + 2 * beat + k * beat / 4, tone(mtf(sdeg(motif[k], 2)), .18, 14, (1, .2)), 0.05)
    elif style == "lofi":
        sw = beat / 2 * 0.62
        for q in (0, 2.5): add(s0 + q * beat, lp(kick(0.6), 4), 0.75)
        for q in (1, 3): add(s0 + q * beat, lp(snare(180), 6), 0.3)
        for e in range(4):
            add(s0 + e * beat, lp(hat(), 3), 0.06); add(s0 + e * beat + sw, lp(hat(), 3), 0.045)
        for m in ch: add(s0, lp(rhodes(mtf(root + m + 12), bar * .95), 3), 0.07)
        add(s0, tone(mtf(r - 12), beat * 1.6, 2.5, (1, .3)), 0.28); add(s0 + 2.5 * beat, tone(mtf(r - 12 + 7), beat, 3, (1, .3)), 0.22)
        if b % 2 == 1:
            for k, d_ in enumerate(motif[:4]): add(s0 + k * beat + 0.04, lp(rhodes(mtf(sdeg(d_, 2)), beat), 2), 0.045)
    elif style == "house":
        for q in range(4):
            add(s0 + q * beat, kick(1.1), 0.95); add(s0 + q * beat + beat / 2, hat(True, 1.2), 0.1)
            if q in (1, 3) and not intro: add(s0 + q * beat, clap(), 0.33)
        for e in range(16): add(s0 + e * beat / 4, shaker(), 0.035)
        for e in range(8):
            if e % 2 == 1: add(s0 + e * beat / 2, saw(mtf(r - 12), beat / 2 * .8, 8, 0.002), 0.22)
        if not intro:
            for pos in (0.5, 1.75, 3.0):
                for m in ch: add(s0 + pos * beat, lp(tone(mtf(root + m + 12), .22, 12, (1, .6, .4, .2)), 2), 0.07)
    elif style == "synthwave":
        for q in range(4):
            add(s0 + q * beat, kick(0.9), 0.85)
            if q in (1, 3): add(s0 + q * beat, snare(220, 0.35), 0.32)
        for e in range(8): add(s0 + e * beat / 2, hat(), 0.06)
        for m in ch: add(s0, saw(mtf(root + m + 12), bar, 0.6, 0.008, 0.25), 0.07)
        for e in range(8): add(s0 + e * beat / 2, saw(mtf(r - 12), beat / 2 * .9, 7, 0.003), 0.2)
        if b >= 1:
            arp = [root + ch[k % len(ch)] + 24 for k in range(16)]
            for k in range(16): add(s0 + k * beat / 4, tone(mtf(arp[k]), .12, 16, (1, .5, .3)), 0.04)
    elif style == "minimal":
        for q in range(4):
            add(s0 + q * beat, lp(kick(0.8), 2), 0.7)
            if q == 2 and not intro: add(s0 + q * beat, snare(260, 0.12), 0.18)
        for e in range(16):
            if e % 4 == 2: add(s0 + e * beat / 4, hat(), 0.07)
            elif e % 2 == 1: add(s0 + e * beat / 4, shaker(), 0.03)
        add(s0, tone(mtf(r - 12), beat * 1.8, 2, (1, .2)), 0.25)
        for k in range(8):
            if (k + b) % 3 != 2: add(s0 + k * beat / 2, pluck(mtf(sdeg(motif[k], 1)), beat), 0.11)
    elif style == "trap":
        h = beat  # yarım tempo hissi: trampet 3. vuruşta
        add(s0, kick(1.0), 0.8); add(s0 + 2.5 * h, kick(1.0), 0.6)
        if not intro: add(s0 + 2 * h, clap(), 0.36)
        roll = int(rng.integers(0, 4))
        for e in range(16):
            add(s0 + e * h / 4, hat(bright=1.4), 0.05)
            if e // 4 == roll and e % 2 == 1: add(s0 + e * h / 4 + h / 8, hat(bright=1.4), 0.04)
        add(s0, k808(mtf(r - 24), bar * 0.55), 0.45); add(s0 + 2.75 * h, k808(mtf(r - 24 + ch[1] - ch[0]), bar * 0.3), 0.35)
        for m in ch: add(s0, pad(mtf(root + m + 12), bar), 0.05)
        if b % 2 == 1:
            for k in range(4): add(s0 + k * h, pluck(mtf(sdeg(motif[k], 2)), h), 0.06)
    elif style == "funk":
        for q in (0, 1.75, 2.5): add(s0 + q * beat, kick(0.9), 0.8)
        for q in (1, 3): add(s0 + q * beat, snare(210), 0.3)
        for e in range(16): add(s0 + e * beat / 4, hat(bright=1.2), 0.05 if e % 2 else 0.07)
        for pos, iv in ((0, 0), (0.75, 12), (1.5, 7), (2.25, 10), (3.0, 0), (3.5, 12)):
            add(s0 + pos * beat, tone(mtf(r - 12 + iv), beat * .35, 9, (1, .6, .3)), 0.26)
        if not intro:
            for pos in (0.5, 1.5, 2.75):
                for m in ch: add(s0 + pos * beat, lp(tone(mtf(root + m + 12), .12, 20, (1, .7, .5, .3)), 2), 0.07)
    elif style == "ambient":
        for m in ch: add(s0, pad(mtf(root + m), bar * 1.02), 0.1)
        add(s0, pad(mtf(r - 12), bar), 0.08)
        for k in range(4):
            if (k + b) % 2 == 0: add(s0 + k * beat, pluck(mtf(sdeg(motif[k], 2)), beat * 2), 0.08)
        if not intro:
            add(s0, lp(kick(0.5), 6), 0.4); add(s0 + 2 * beat, lp(kick(0.5), 6), 0.3)
            for e in range(8): add(s0 + e * beat / 2, lp(hat(), 4), 0.03)

if style == "lofi":  # plak cızırtısı
    cr = rng.standard_normal(N) * 0.004; cr[rng.random(N) < 0.0004] += rng.uniform(-0.15, 0.15, int((rng.random(N) < 0.0004).sum()) or 1)[0]
    mix += lp(cr, 2)
fade = np.minimum(np.minimum(t / 0.3, 1), np.minimum((T - t) / 1.5, 1)); mix *= fade
mix = np.tanh(mix * 1.3); mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.8

# --- ses efektleri ---
def whoosh():
    d = 0.56; n = int(sr * d); x = rng.standard_normal(n); u = np.arange(n) / n
    fc = 250 + 5200 * np.sin(np.pi * u) ** 2; a = np.exp(-2 * np.pi * fc / sr); y = np.zeros(n); z = 0.0
    for k in range(n):
        z = a[k] * z + (1 - a[k]) * x[k]; y[k] = z
    y = y - np.convolve(y, np.ones(160) / 160, "same")
    y = y * np.sin(np.pi * u) ** 2; return y / np.max(np.abs(y))
def pop(f0=520, f1=900):
    d = 0.1; tt = np.arange(int(sr * d)) / sr; f = f0 + (f1 - f0) * tt / d
    return np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-tt * 36)
def ding():
    d = 1.0; tt = np.arange(int(sr * d)) / sr
    y = (np.sin(2 * np.pi * 1318.5 * tt) + 0.5 * np.sin(2 * np.pi * 1975.5 * tt) + 0.25 * np.sin(2 * np.pi * 2637 * tt)) * np.exp(-tt * 5) * np.minimum(tt / 0.003, 1)
    return y / np.max(np.abs(y))
def tick():  # saat tıkırtısı
    d = 0.05; tt = np.arange(int(sr * d)) / sr
    y = (np.sin(2 * np.pi * 3200 * tt) * 0.6 + rng.standard_normal(len(tt)) * 0.4) * np.exp(-tt * 140)
    return y / np.max(np.abs(y))
def alarm():  # dijital çalar saat: 4'lü bip, iki kez
    out = np.zeros(int(sr * 1.0)); b = int(sr * 0.07); tt = np.arange(b) / sr
    bip = np.sign(np.sin(2 * np.pi * 2730 * tt)) * 0.5 + np.sin(2 * np.pi * 2730 * tt) * 0.5
    bip *= np.minimum(np.minimum(tt / 0.004, 1), np.minimum((0.07 - tt) / 0.004, 1))
    for g0 in (0.0, 0.5):
        for k in range(4):
            i = int(sr * (g0 + k * 0.1)); out[i:i + b] += bip
    return lp(out, 2) / 1.0
if ev_path:
    evs = json.load(open(ev_path))
    for e_ in evs:  # [başlangıç, "mute", süre]: müziği o aralıkta neredeyse sustur
        if e_[1] == "mute":
            a0, d0 = e_[0], e_[2]; g = np.ones(N)
            ramp = 0.25; x0 = (t - a0) / ramp; x1 = (a0 + d0 - t) / ramp
            g = 1 - 0.88 * np.clip(np.minimum(x0, x1), 0, 1); mix *= g
    sfx = np.zeros(N); cache = {}
    for e_ in evs:
        at, kind = e_[0], e_[1]
        if kind == "mute": continue
        if kind not in cache: cache[kind] = {"whoosh": whoosh, "pop": pop, "pop2": lambda: pop(700, 1150), "ding": ding, "tick": tick, "alarm": alarm}[kind]()
        sig = cache[kind]; g = {"whoosh": 0.5, "pop": 0.3, "pop2": 0.26, "ding": 0.34, "tick": 0.45, "alarm": 0.42}[kind]
        i = max(0, int(at * sr)); j = min(N, i + len(sig))
        if i < N: sfx[i:j] += sig[:j - i] * g
    mix = mix + sfx; mix = mix / max(1.0, float(np.max(np.abs(mix))))
w = wave.open(out_name, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
w.writeframes((mix * 32767).astype(np.int16).tobytes()); w.close()
print("ok", style, int(bpm), "bpm", "root", root)
