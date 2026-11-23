import sys; sys.path.insert(0,"/tmp/proto"); from kit import *
K=kare_imgs()
SPK='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M3 9h4l5-4v14l-5-4H3z" fill="{c}"/><path d="M15.5 8.5a5 5 0 0 1 0 7M18.5 5.5a9 9 0 0 1 0 13" stroke="{c}" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'
MUTE='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M3 9h4l5-4v14l-5-4H3z" fill="{c}"/><path d="M16 9l5 6M21 9l-5 6" stroke="{c}" stroke-width="2.2" stroke-linecap="round"/></svg>'
ic=lambda f,s,c: f.format(s=s,c=c)
phone_css="position:absolute;left:250px;top:470px;width:580px;height:1140px;border-radius:84px;background:#121214;box-shadow:0 50px 110px rgba(0,0,0,.65),0 0 0 3px #2a2a30;padding:18px"
SES=[1015,1028,1404,1365,1133,136,1155]; SIZ=[107,110,115,5,108,110,105]
def rows(vals,pre,col):
    return "".join(f'<div style="display:flex;align-items:center;gap:14px;height:46px"><div style="flex:1;height:26px;border-radius:13px;background:#EFEFF4;position:relative"><div id="{pre}{i}" style="position:absolute;left:0;top:0;bottom:0;width:0;border-radius:13px;background:{col}"></div></div><div id="{pre}n{i}" style="width:96px;text-align:right;font-weight:800;font-size:26px;font-variant-numeric:tabular-nums">0</div></div>' for i,v in enumerate(vals))
tiles="".join(f'<div class="el" id="tl{i}" style="left:0;top:0;width:118px;height:200px"><div class="card" style="inset:0;border-radius:26px;{"box-shadow:0 0 0 4px #C6F24E,0 20px 40px rgba(0,0,0,.5)" if i<7 else ""}">{ic(SPK if i<7 else MUTE,58,"#C6F24E" if i<7 else "#8a8a92")}</div></div>' for i in range(14))
body=f'''
<div class="hd" id="h1"><h1>Sesli video mu,<br><em>sessiz video mu?</em></h1><p>Kendi 14 Reel'imizden</p></div>
{tiles}
<div class="el" id="g1" style="left:0;right:0;top:1290px;text-align:center"><div class="x3d" style="font-size:150px">ses.</div></div>
<div class="hd" id="h2"><h1>Erişim</h1><p>17–23 Kasım</p></div>
<div class="el" id="ph2" style="{phone_css}"><div style="position:absolute;inset:18px;border-radius:68px;overflow:hidden;background:#fff;color:#111;padding:90px 40px 0">
 <div style="display:flex;align-items:center;gap:14px;font-family:'Inter Display';font-weight:800;font-size:38px">{ic(SPK,46,'#5E9E00')}Seslendirmeli</div>
 <div style="margin-top:14px;position:relative">{rows(SES,'a','#C6F24E')}</div>
 <div id="t1" style="margin-top:10px;font-size:24px;font-weight:700;color:#5E9E00;opacity:0">7 videonun 6'sı 1.000 kişiyi geçti</div>
 <div style="margin-top:34px;display:flex;align-items:center;gap:14px;font-family:'Inter Display';font-weight:800;font-size:38px">{ic(MUTE,46,'#FF2E93')}Sadece yazı ve müzik</div>
 <div style="margin-top:14px">{rows(SIZ,'b','#FF2E93')}</div>
 <div id="t2" style="margin-top:10px;font-size:24px;font-weight:700;color:#FF2E93;opacity:0">7 videonun 7'si 120 kişinin altında</div>
</div></div>
<div class="hd" id="h3"><h1>İlk 3 saniyede<br><em>kaydırıp geçenler</em></h1></div>
<div class="el" id="r1" style="left:80px;top:700px;width:440px;height:600px"><div class="card" style="inset:0">
 <svg width="300" height="300" viewBox="0 0 120 120"><circle cx="60" cy="60" r="50" stroke="#2a2a30" stroke-width="14" fill="none"/><circle id="rc1" cx="60" cy="60" r="50" stroke="#C6F24E" stroke-width="14" fill="none" stroke-linecap="round" stroke-dasharray="314.16" stroke-dashoffset="314.16" transform="rotate(-90 60 60)"/></svg>
 <div id="rv1" style="position:absolute;top:190px;left:0;right:0;text-align:center;font-family:'Inter Display';font-weight:800;font-size:72px">%0</div>
 <div style="margin-top:34px;display:flex;align-items:center;gap:12px;font-size:38px;font-weight:800">{ic(SPK,46,'#C6F24E')}Sesli</div>
 <div id="rw1" style="margin-top:10px;font-size:32px;color:#C9C9CF;opacity:0">yarısı</div></div></div>
<div class="el" id="r2" style="left:560px;top:700px;width:440px;height:600px"><div class="card" style="inset:0">
 <svg width="300" height="300" viewBox="0 0 120 120"><circle cx="60" cy="60" r="50" stroke="#2a2a30" stroke-width="14" fill="none"/><circle id="rc2" cx="60" cy="60" r="50" stroke="#FF2E93" stroke-width="14" fill="none" stroke-linecap="round" stroke-dasharray="314.16" stroke-dashoffset="314.16" transform="rotate(-90 60 60)"/></svg>
 <div id="rv2" style="position:absolute;top:190px;left:0;right:0;text-align:center;font-family:'Inter Display';font-weight:800;font-size:72px">%0</div>
 <div style="margin-top:34px;display:flex;align-items:center;gap:12px;font-size:38px;font-weight:800">{ic(MUTE,46,'#FF2E93')}Sessiz</div>
 <div id="rw2" style="margin-top:10px;font-size:32px;color:#C9C9CF;opacity:0">dörtte üçü</div></div></div>
<div class="hd" id="h4"><h1>Dürüst olalım:</h1><p>Video süreleri farklıydı</p></div>
<div class="el" id="d1" style="left:110px;top:660px;width:860px"><div style="font-size:36px;font-weight:800;margin-bottom:16px">Sessiz videolar</div><div style="height:90px;border-radius:45px;background:#24242b;position:relative"><div id="db1" style="position:absolute;left:0;top:0;bottom:0;width:0;border-radius:45px;background:#FF2E93"></div></div><div style="margin-top:12px;font-size:30px;color:#C9C9CF">7–10 saniye</div></div>
<div class="el" id="d2" style="left:110px;top:920px;width:860px"><div style="font-size:36px;font-weight:800;margin-bottom:16px">Sesli videolar</div><div style="height:90px;border-radius:45px;background:#24242b;position:relative"><div id="db2" style="position:absolute;left:0;top:0;bottom:0;width:0;border-radius:45px;background:#C6F24E"></div></div><div style="margin-top:12px;font-size:30px;color:#C9C9CF">25 saniyeden uzun</div></div>
<div class="el" id="d3" style="left:0;right:0;top:1180px;text-align:center"><div style="font-size:44px;font-weight:700;color:#C9C9CF">Ama erişim farkı</div><div class="x3d x3p" style="font-size:190px;line-height:1.05">10 kat</div></div>
<div class="hd" id="h5"><h1>Yüzünü göstermek<br>zorunda değilsin.</h1><p style="font-size:64px;color:#C6F24E;font-weight:800;font-family:'Inter Display';margin-top:20px">Sesini kullan.</p></div>
__WAVES__
<div class="cap" id="c5">Bir ses sana konuşunca<br><b>durup dinliyorsun.</b></div>
<div class="hd" id="h6"><h1>Sen videolarını<br><em>seslendiriyor musun?</em></h1></div>
<div class="el" id="p6a" style="left:0;right:0;top:1450px;text-align:center"><span class="pill">Yorumlara yaz</span></div>
<div class="el" id="p6b" style="left:0;right:0;top:1580px;text-align:center"><span class="pill" style="background:#C6F24E;color:#0B0B0D">Video çeken arkadaşına gönder</span></div>
<div class="hd" id="h7"><p style="font-size:40px">Her akşam dijital dünyadan bir şeyi</p><h1 style="margin-top:10px"><em>30 saniyede</em> çözüyoruz.</h1></div>
<div class="el" id="y7" style="left:110px;top:1020px;width:860px;height:330px"><div class="card" style="inset:0;padding:0 50px"><div style="font-size:34px;font-weight:800;color:#FF2E93;letter-spacing:2px">YARIN</div><div style="margin-top:18px;font-family:'Inter Display';font-weight:800;font-size:56px;line-height:1.1;text-align:center">Film afişleri neden hep<br>turuncu ve mavi?</div></div></div>
{kare_html("kr",K)}
'''
waves="".join(f'<div class="el" id="wv{i}" style="left:540px;top:1060px;width:0;height:0"><div style="position:absolute;left:-200px;top:-200px;width:400px;height:400px;border-radius:50%;border:6px solid {"#C6F24E" if i%2==0 else "#FF2E93"}"></div></div>' for i in range(4))
body=body.replace("__WAVES__",waves)
script=r'''
const SES=%s, SIZ=%s;
window.render=function(t){
  $('glow').style.transform=`scale(${1+0.08*Math.sin(t*2)})`;
  const tilt=`perspective(1600px) rotateY(${-8+6*Math.sin(t*0.7)}deg) rotateX(${2*Math.sin(t*0.9)}deg)`;
  // A 0–6.1: 14 video, ayrışma, "ses."
  hd('h1',t,0,6.1);
  for(let i=0;i<14;i++){
    const mix=[3,10,5,12,0,8,6,13,1,9,4,11,2,7].indexOf(i); // karışık başlangıç sırası
    const mx=72+(mix%%7)*136, my=640+Math.floor(mix/7)*250;
    const g=i<7?0:1, k=i%%7, sx=72+k*136, sy=g?930:640;
    const a=0.15+mix*0.12, f=E((t-3.4)/0.8);
    const x=mx+(sx-mx)*f, y=my+(sy-my)*f+(g?f*60:0);
    st('tl'+i,win(t,a,6.1,0.25,0.3),x,y+(1-E((t-a)/0.4))*120,(i>=7&&t>5.2?0.92:1)*(0.85+0.15*Bk((t-a)/0.4)),0,`perspective(1200px) rotateY(${6*Math.sin(t*1.3+i)}deg)`);
    $('tl'+i).style.filter=(i>=7&&t>5.2)?'grayscale(1) brightness(.6)':'none';
  }
  st('g1',win(t,5.15,6.1,0.15,0.3),0,0,0.6+0.4*Bk((t-5.15)/0.4));
  // B 6.1–16.3: erişim çubukları
  hd('h2',t,6.1,16.3); st('ph2',win(t,6.2,16.3,0.35,0.3),0,(1-E((t-6.2)/0.6))*300,1,0,tilt);
  SES.forEach((v,i)=>{const p=E((t-(6.6+i*0.45))/0.7); $('a'+i).style.width=(Math.min(v,1404)/1404*100*p)+'%%'; $('an'+i).textContent=Math.round(v*p).toLocaleString('tr-TR');});
  SIZ.forEach((v,i)=>{const p=E((t-(11.0+i*0.4))/0.7); $('b'+i).style.width=(v/1404*100*p)+'%%'; $('bn'+i).textContent=Math.round(v*p).toLocaleString('tr-TR');});
  $('t1').style.opacity=cl((t-9.9)/0.3); $('t2').style.opacity=cl((t-14.4)/0.3);
  // C 16.3–23.4: halkalar
  hd('h3',t,16.3,23.4); st('r1',win(t,16.6,23.4,0.3,0.3),0,(1-E((t-16.6)/0.5))*120); st('r2',win(t,17.0,23.4,0.3,0.3),0,(1-E((t-17.0)/0.5))*120);
  const p1=E((t-18.6)/1.2)*0.50, p2=E((t-21.5)/1.1)*0.74;
  $('rc1').setAttribute('stroke-dashoffset',314.16*(1-p1)); $('rv1').textContent='%%'+Math.round(p1*100);
  $('rc2').setAttribute('stroke-dashoffset',314.16*(1-p2)); $('rv2').textContent='%%'+Math.round(p2*100);
  $('rw1').style.opacity=cl((t-19.8)/0.3); $('rw2').style.opacity=cl((t-22.4)/0.3);
  // D 23.4–28.1: dürüstlük + 10 kat
  hd('h4',t,23.4,28.1); st('d1',win(t,23.6,28.1,0.3,0.3),(1-E((t-23.6)/0.5))*-200,0); st('d2',win(t,24.3,28.1,0.3,0.3),(1-E((t-24.3)/0.5))*-200,0);
  $('db1').style.width=(E((t-24.6)/0.7)*18)+'%%'; $('db2').style.width=(E((t-25.0)/0.9)*92)+'%%';
  st('d3',win(t,26.4,28.1,0.2,0.3),0,0,0.6+0.4*Bk((t-26.4)/0.45),0,`perspective(1400px) rotateX(${6*Math.sin(t*1.5)}deg)`);
  // E 28.1–35.2: ses dalgaları
  hd('h5',t,28.1,35.2); const inE=t>28.1&&t<35.2;
  for(let i=0;i<4;i++){const ph=((t-28.4)*0.7+i/4)%%1; st('wv'+i,inE&&t>28.4?(1-ph)*cl((35.2-t)/0.3):0,0,0,0.4+ph*1.6);}
  cap('c5',t,32.2,35.2);
  // F 35.2–40.6
  hd('h6',t,35.2,40.6); st('p6a',win(t,37.5,40.6,0.2,0.3),0,0,Bk((t-37.5)/0.35)); st('p6b',win(t,38.6,40.6,0.2,0.3),0,0,Bk((t-38.6)/0.35));
  // G 40.6–48.6
  hd('h7',t,40.6,99); st('y7',cl((t-44.7)/0.3),0,(1-E((t-44.7)/0.5))*80,0.9+0.1*Bk((t-44.7)/0.4),0,`perspective(1400px) rotateX(${4*Math.sin(t*1.2)}deg)`);
  // Kare
  const face=t<6.1?'saskin':t<16.3?'mutlu':t<23.4?'saskin':t<28.1?'goz':t<35.2?'mutlu':'goz';
  if(inE){kare('kr',t,face,390,910,1.0);} else if(t>40.6){kare('kr',t,face,390,1390,0.9);} else {kare('kr',t,face,800,1650,0.6);}
  $('kr').style.opacity=cl(t/0.4)*(t>27.9&&t<28.3||t>35.0&&t<35.4||t>40.4&&t<40.8?0:1);
};''' % (SES,SIZ)
sfx=[[0.1,'whoosh'],[0.2,'pop'],[1.0,'pop'],[1.8,'pop'],[3.4,'whoosh'],[5.15,'ding'],[6.2,'whoosh'],[6.6,'tick'],[11.0,'tick'],[9.9,'pop2'],[14.4,'pop2'],[16.4,'whoosh'],[18.6,'tick'],[21.5,'tick'],[23.5,'whoosh'],[26.4,'ding'],[28.2,'whoosh'],[35.3,'whoosh'],[37.5,'pop'],[38.6,'pop'],[40.7,'whoosh'],[44.7,'ding']]
open(sys.argv[1],"w").write(page(body,script,sfx,48.6))
