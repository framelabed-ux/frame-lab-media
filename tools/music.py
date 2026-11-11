import numpy as np, wave, sys, json
sr=44100; T=float(sys.argv[1]) if len(sys.argv)>1 else 35.5; out_name=sys.argv[2] if len(sys.argv)>2 else "music2.wav"
N=int(sr*T); t=np.arange(N)/sr; mix=np.zeros(N)
bpm=120; beat=60/bpm; bar=4*beat
rng=np.random.default_rng(7)
def add(start, sig, gain):
    i=int(start*sr); j=min(N,i+len(sig))
    if i<N: mix[i:j]+=sig[:j-i]*gain
def kick():
    d=0.35; tt=np.arange(int(sr*d))/sr; f=50+90*np.exp(-tt*30)
    return np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-tt*9)
def hat(open_=False):
    d=0.12 if not open_ else 0.25; n=rng.standard_normal(int(sr*d)); n=n-np.convolve(n,np.ones(4)/4,'same')
    return n*np.exp(-np.arange(len(n))/sr*(40 if not open_ else 14))
def clap():
    d=0.2; n=rng.standard_normal(int(sr*d)); n=np.convolve(n,np.ones(3)/3,'same')
    e=np.exp(-np.arange(len(n))/sr*22); return n*e
def tone(f,d,dec,harm=(1,0.4,0.15)):
    tt=np.arange(int(sr*d))/sr; s=sum(a*np.sin(2*np.pi*f*(k+1)*tt) for k,a in enumerate(harm))
    return s*np.exp(-tt*dec)*np.minimum(tt/0.005,1)
prog=[(57,(69,72,76)),(53,(65,69,72)),(48,(64,67,72)),(55,(67,71,74))]  # Am F C G (midi)
mtf=lambda m:440*2**((m-69)/12)
nbars=int(np.ceil(T/bar))
for b in range(nbars):
    root,ch=prog[b%4]; s0=b*bar
    intro = b==0
    for q in range(4):
        st=s0+q*beat
        if not intro or q>=2: add(st,kick(),0.9)
        if q in (1,3) and not intro: add(st,clap(),0.35)
    for e in range(8):
        st=s0+e*beat/2
        add(st,hat(open_=(e%2==1)),0.10 if e%2 else 0.07)
        # bass: offbeat 8ths
        if e%2==1 or e==0: add(st,tone(mtf(root-12),beat/2*0.9,6,(1,0.5,0.2)),0.32)
    # chord stabs syncopated
    for pos in (0,1.5,3,3.5) if not intro else (0,):
        for m in ch: add(s0+pos*beat,tone(mtf(m),0.4,7,(1,0.3,0.1)),0.09)
    # arp lead 16ths in second half of each bar
    if b>=1:
        notes=[ch[0]+12,ch[1]+12,ch[2]+12,ch[1]+12]
        for k in range(8):
            add(s0+2*beat+k*beat/4,tone(mtf(notes[k%4]),0.18,14,(1,0.2)),0.05)
fade=np.minimum(np.minimum(t/0.3,1),np.minimum((T-t)/1.5,1)); mix*=fade
mix=np.tanh(mix*1.3); mix=mix/np.max(np.abs(mix))*0.8
# --- ses efektleri: python3 music.py <sn> <out.wav> [olaylar.json]  ->  [[zaman, "whoosh"|"pop"|"pop2"|"ding"], ...]
def whoosh():
    d=0.56; n=int(sr*d); x=rng.standard_normal(n); u=np.arange(n)/n
    fc=250+5200*np.sin(np.pi*u)**2; a=np.exp(-2*np.pi*fc/sr); y=np.zeros(n); z=0.0
    for k in range(n):
        z=a[k]*z+(1-a[k])*x[k]; y[k]=z
    y=y-np.convolve(y,np.ones(160)/160,'same')
    y=y*np.sin(np.pi*u)**2; return y/np.max(np.abs(y))
def pop(f0=520,f1=900):
    d=0.1; tt=np.arange(int(sr*d))/sr; f=f0+(f1-f0)*tt/d
    return np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-tt*36)
def ding():
    d=1.0; tt=np.arange(int(sr*d))/sr
    y=(np.sin(2*np.pi*1318.5*tt)+0.5*np.sin(2*np.pi*1975.5*tt)+0.25*np.sin(2*np.pi*2637*tt))*np.exp(-tt*5)*np.minimum(tt/0.003,1)
    return y/np.max(np.abs(y))
if len(sys.argv)>3:
    sfx=np.zeros(N); cache={}
    for at,kind in json.load(open(sys.argv[3])):
        if kind not in cache: cache[kind]={"whoosh":whoosh,"pop":pop,"pop2":lambda:pop(700,1150),"ding":ding}[kind]()
        sig=cache[kind]; g={"whoosh":0.5,"pop":0.3,"pop2":0.26,"ding":0.34}[kind]
        i=max(0,int(at*sr)); j=min(N,i+len(sig))
        if i<N: sfx[i:j]+=sig[:j-i]*g
    mix=mix+sfx; mix=mix/max(1.0,float(np.max(np.abs(mix))))
w=wave.open(out_name,"wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((mix*32767).astype(np.int16).tobytes()); w.close(); print("ok")
