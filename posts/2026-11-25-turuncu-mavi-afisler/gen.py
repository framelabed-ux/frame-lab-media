import sys; sys.path.insert(0,"/tmp/proto"); from kit import *
K=kare_imgs()
OR="#FF8A2A"; TL="#1FB5B0"
FLAME='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M12 2c1 3.5 5 6 5 11a5 5 0 0 1-10 0c0-2.2 1.2-3.6 2.3-4.8.3 1.8 1.2 2.8 2.2 3.1C11 8.7 11.2 5 12 2z" fill="{c}"/></svg>'
SUN='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><circle cx="12" cy="15" r="5" fill="{c}"/><path d="M2 20h20" stroke="{c}" stroke-width="2" stroke-linecap="round"/><path d="M12 5v3M5 8l2 2M19 8l-2 2" stroke="{c}" stroke-width="2" stroke-linecap="round"/></svg>'
MOON='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z" fill="{c}"/></svg>'
STAR='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M12 3l2.6 5.6 6.1.7-4.5 4.2 1.2 6L12 16.6 6.6 19.5l1.2-6L3.3 9.3l6.1-.7z" fill="{c}"/></svg>'
ic=lambda f,s,c: f.format(s=s,c=c)
poster=f'''<div class="el" id="po" style="left:230px;top:500px;width:620px;height:900px"><div style="position:absolute;inset:0;border-radius:24px;overflow:hidden;background:radial-gradient(70% 60% at 50% 45%,#2a8f8c,#0d3b3d 70%,#071d1f);box-shadow:0 50px 110px rgba(0,0,0,.65),0 0 0 3px #2a2a30">
 <div id="pglow" style="position:absolute;left:110px;top:170px;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,rgba(255,138,42,.55),rgba(255,138,42,0) 65%)"></div>
 <img src="{K['saskin_sag']}" style="position:absolute;left:110px;top:170px;width:400px;mix-blend-mode:screen;filter:sepia(1) saturate(7) hue-rotate(-38deg) brightness(1.1);-webkit-mask-image:radial-gradient(circle,#000 52%,transparent 70%)">
 <div style="position:absolute;left:0;right:0;top:640px;text-align:center;font-family:'Inter Display';font-weight:900;font-size:92px;letter-spacing:6px;color:#FFE2C4;text-shadow:0 0 30px rgba(255,138,42,.6)">SON KARE</div>
 <div style="position:absolute;left:0;right:0;top:770px;text-align:center;font-size:26px;font-weight:700;letter-spacing:8px;color:#9fd8d6">YAKINDA</div></div></div>'''
body=f'''
<div class="hd" id="h1"><h1>Film afişleri neden hep<br><em>turuncu ve mavi?</em></h1></div>
{poster}
<div class="el" id="sw1" style="left:70px;top:1440px;width:440px;height:130px"><div class="card" style="inset:0;flex-direction:row;gap:22px"><div style="width:64px;height:64px;border-radius:50%;background:{OR}"></div><div style="font-size:44px;font-weight:800">Turuncu</div></div></div>
<div class="el" id="sw2" style="left:570px;top:1440px;width:440px;height:130px"><div class="card" style="inset:0;flex-direction:row;gap:22px"><div style="width:64px;height:64px;border-radius:50%;background:{TL}"></div><div style="font-size:44px;font-weight:800">Mavi</div></div></div>
<div class="hd" id="h2"><p style="font-size:40px;color:#C9C9CF">Hollywood'un sevdiği ikili</p></div>
<div class="el" id="duo" style="left:0;right:0;top:640px;text-align:center"><div style="font-family:'Inter Display';font-weight:900;font-size:150px;line-height:1.02;letter-spacing:-3px"><span style="color:{TL};text-shadow:0 10px 0 #0e6e6b,0 20px 40px rgba(0,0,0,.6)">Turkuaz</span><br><span style="font-size:90px;color:#fff">ve</span><br><span style="color:{OR};text-shadow:0 10px 0 #a8520f,0 20px 40px rgba(0,0,0,.6)">turuncu</span></div></div>
<div class="hd" id="h3"><h1>Sebep:<br><em>insan teni.</em></h1></div>
<div class="el" id="wh" style="left:240px;top:560px;width:600px;height:600px"><div id="whr" style="position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 0deg,#ff3b30 0deg,{OR} 40deg,#ffd23f 80deg,#7cd34a 130deg,{TL} 220deg,#2f7bff 255deg,#8a4dff 290deg,#ff2e93 330deg,#ff3b30 360deg);box-shadow:0 40px 90px rgba(0,0,0,.6)"></div><div style="position:absolute;inset:150px;border-radius:50%;background:#0B0B0D"></div>
 <div id="ln" style="position:absolute;left:50%;top:50%;width:620px;height:8px;margin-left:-310px;margin-top:-4px;border-radius:4px;background:#fff;opacity:0"></div>
 <div id="mo" style="position:absolute;width:90px;height:90px;border-radius:50%;border:8px solid #fff;background:{OR};opacity:0"></div>
 <div id="mt" style="position:absolute;width:90px;height:90px;border-radius:50%;border:8px solid #fff;background:{TL};opacity:0"></div></div>
<div class="el" id="skin" style="left:390px;top:1220px;width:300px;height:110px"><div class="card" style="inset:0;flex-direction:row;gap:18px;border-radius:55px"><div style="width:56px;height:56px;border-radius:50%;background:#E0A27A"></div><div style="font-size:36px;font-weight:800">Ten rengi</div></div></div>
<div class="cap" id="c3a">Arka plan mavi-yeşil olunca <b>yüzler öne çıkıyor.</b></div>
<div class="cap" id="c3b">Renk çemberinde <b>birbirinin tam karşısında.</b></div>
<div class="el" id="f1" style="left:80px;top:560px;width:430px;height:640px"><div class="card" style="inset:0;background:linear-gradient(160deg,#3a2414,#1b120c)"><div style="display:flex;gap:10px">{ic(FLAME,120,OR)}{ic(SUN,120,OR)}</div><div style="margin-top:40px;font-size:38px;font-weight:800;text-align:center;line-height:1.3">Ateş, patlama,<br>gün batımı</div><div style="margin-top:16px;font-size:34px;font-weight:800;color:{OR}">turuncu</div></div></div>
<div class="el" id="f2" style="left:570px;top:560px;width:430px;height:640px"><div class="card" style="inset:0;background:linear-gradient(160deg,#0f2e33,#0a1719)"><div style="display:flex;gap:10px">{ic(MOON,120,TL)}{ic(STAR,120,TL)}</div><div style="margin-top:40px;font-size:38px;font-weight:800;text-align:center;line-height:1.3">Gece,<br>gökyüzü</div><div style="margin-top:16px;font-size:34px;font-weight:800;color:{TL}">mavi</div></div></div>
<div class="el" id="kh" style="left:0;right:0;top:1300px;text-align:center"><div class="x3d" style="font-size:130px">Kontrast hazır.</div></div>
<div class="hd" id="h5"><h1>Kapakta bir şeyi<br><em>öne çıkarmak mı istiyorsun?</em></h1></div>
<div class="el" id="cv" style="left:290px;top:600px;width:500px;height:720px"><div id="cvb" style="position:absolute;inset:0;border-radius:30px;background:#6b6b70;box-shadow:0 40px 90px rgba(0,0,0,.6);overflow:hidden">
 <img src="{K['mutlu_sol']}" style="position:absolute;left:50px;top:160px;width:400px;-webkit-mask-image:radial-gradient(circle,#000 52%,transparent 70%)"></div></div>
<div class="cap" id="c5">Karşıt rengini <b>arkaya koy.</b> Lime'ın karşıtı: pembe.</div>
<div class="hd" id="h6"><h1>Sen bu ikiliyi en son<br><em>hangi afişte gördün?</em></h1></div>
<div class="el" id="p6" style="left:0;right:0;top:1000px;text-align:center"><span class="pill">Yorumlara yaz</span></div>
<div class="hd" id="h7"><p style="font-size:40px">Her akşam dijital dünyadan bir şeyi</p><h1 style="margin-top:10px"><em>30 saniyede</em> çözüyoruz.</h1></div>
{kare_html("kr",K)}
'''
script=r'''
window.render=function(t){
  $('glow').style.transform=`scale(${1+0.08*Math.sin(t*2)})`;
  // A 0–8.8: afiş + ikili
  hd('h1',t,0,4.85);
  st('po',win(t,0,4.9,0.15,0.35),0,(1-E(t/0.6))*260,1,0,`perspective(1600px) rotateY(${-14+8*Math.sin(t*0.9)}deg) rotateX(${3*Math.sin(t*1.1)}deg)`);
  $('pglow').style.transform=`scale(${1+0.1*Math.sin(t*3)})`;
  st('sw1',win(t,2.3,4.85,0.2,0.3),0,0,Bk((t-2.3)/0.4)); st('sw2',win(t,3.4,4.85,0.2,0.3),0,0,Bk((t-3.4)/0.4));
  hd('h2',t,4.9,8.8); st('duo',win(t,5.1,8.8,0.25,0.3),0,0,0.7+0.3*Bk((t-5.1)/0.5),0,`perspective(1400px) rotateX(${6*Math.sin(t*1.4)}deg)`);
  // B 8.8–19.3: ten + çember
  hd('h3',t,8.85,19.3);
  st('wh',win(t,9.0,19.3,0.3,0.3),0,(1-E((t-9.0)/0.6))*200); $('whr').style.transform=`rotate(${720*(1-E((t-9.0)/6.8))}deg)`;
  st('skin',win(t,10.7,19.3,0.25,0.3),0,0,Bk((t-10.7)/0.4));
  // çember durunca turuncu (30°) ve turkuaz (~170°) işaretleri: işaretler sabit konumda
  const R=225, cx=300, cy=300, aO=(40-90)*Math.PI/180, aT=(220-90)*Math.PI/180;
  $('mo').style.left=(cx+R*Math.cos(aO)-45)+'px'; $('mo').style.top=(cy+R*Math.sin(aO)-45)+'px';
  $('mt').style.left=(cx+R*Math.cos(aT)-45)+'px'; $('mt').style.top=(cy+R*Math.sin(aT)-45)+'px';
  st('mo',cl((t-16.6)/0.25),0,0,Bk((t-16.6)/0.4)); st('mt',cl((t-17.2)/0.25),0,0,Bk((t-17.2)/0.4));
  $('ln').style.opacity=cl((t-17.8)/0.3); $('ln').style.transform=`rotate(${-50}deg) scaleX(${E((t-17.8)/0.5)})`;
  cap('c3a',t,12.4,15.6); cap('c3b',t,15.8,19.3);
  // C 19.3–25.9: ateş / gece
  st('f1',win(t,19.4,25.9,0.3,0.3),(1-E((t-19.4)/0.5))*-200,0,1,0,`perspective(1400px) rotateY(${(1-E((t-19.4)/0.6))*25}deg)`);
  st('f2',win(t,22.2,25.9,0.3,0.3),(1-E((t-22.2)/0.5))*200,0,1,0,`perspective(1400px) rotateY(${(1-E((t-22.2)/0.6))*-25}deg)`);
  st('kh',win(t,24.7,25.9,0.2,0.25),0,0,0.6+0.4*Bk((t-24.7)/0.4));
  // D 25.9–30.9: kapak ipucu
  hd('h5',t,25.95,30.9); st('cv',win(t,26.2,30.9,0.3,0.3),0,(1-E((t-26.2)/0.5))*150,1,0,`perspective(1400px) rotateY(${-8+5*Math.sin(t)}deg)`);
  const pk=E((t-29.2)/0.5); $('cvb').style.background=pk>0?`rgb(${107+(255-107)*pk},${107+(46-107)*pk},${112+(147-112)*pk})`:'#6b6b70';
  cap('c5',t,29.2,30.9);
  // E 30.9–35
  hd('h6',t,30.95,34.95); st('p6',win(t,33.85,34.95,0.2,0.25),0,0,Bk((t-33.85)/0.35));
  // F 35–39.4
  hd('h7',t,35.0,99);
  const face=t<8.8?'saskin':t<19.3?'goz':t<25.9?'mutlu':t<30.9?'goz':'mutlu';
  if(t>35.0) kare('kr',t,face,390,900,1.0); else kare('kr',t,face,800,1650,0.6);
  $('kr').style.opacity=cl(t/0.4)*((t>34.8&&t<35.2)?0:1);
};'''
sfx=[[0.1,'whoosh'],[2.3,'pop'],[3.4,'pop'],[4.95,'whoosh'],[5.1,'ding'],[9.0,'whoosh'],[10.7,'pop'],[16.6,'pop2'],[17.2,'pop2'],[17.8,'tick'],[19.4,'whoosh'],[22.2,'whoosh'],[24.7,'ding'],[26.2,'whoosh'],[29.2,'pop'],[31.0,'whoosh'],[33.85,'pop'],[35.05,'whoosh']]
open(sys.argv[1],"w").write(page(body,script,sfx,39.4))
