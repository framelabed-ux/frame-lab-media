"""Yılbaşı Reel sahnesi. kullanım: python3 gen.py h|v çıktı.html"""
import sys
MODE=sys.argv[1]; OUT=sys.argv[2]
W,H=(1920,1080) if MODE=="h" else (1080,1920)
VW=W; VH=int(W*1080/1920); VT=0 if MODE=="h" else 600
SC=VW/1920
scenes=[  # id, start, end, frames, kb
 ("s1",0.0,5.6,["s1"]),
 ("s2",5.0,10.4,[f"s2_{k}" for k in range(6)]),
 ("s3",9.8,15.4,[f"s3_{k}" for k in range(6)]),
 ("s4",14.8,20.4,[f"s4_{k}" for k in range(6)]),
 ("s5",19.8,26.6,[f"s5_{k}" for k in range(6)]),
]
subs=[(2.3,5.3,"Bir yıl, aslında binlerce kareden oluşur."),
      (5.9,10.1,"Unuttuğumuz sabahlar, yağmurlu yollar,<br>ilk kez denediğimiz şeyler."),
      (10.6,15.1,"Çoğunu hiç paylaşmadık. Ama hepsi bizimdi."),
      (17.4,20.2,"Şimdi sıra yeni karelerde."),
      (21.0,26.1,"Yeni yılın her karesi güzel olsun.")]
sc_html="".join(f'<div class="sc" id="{i}">'+"".join(f'<img id="{i}f{k}" src="kareler/{fr}.jpg">' for k,fr in enumerate(frs))+
   ('<div id="off"></div>' if i=="s1" else '')+'</div>' for i,a,b,frs in scenes)
sub_html="".join(f'<div class="sub" id="sb{k}">{t}</div>' for k,(a,b,t) in enumerate(subs))
subtop = (VH-150) if MODE=="h" else (VT+VH+90)
fs = 46 if MODE=="h" else 50
title = '' if MODE=="h" else '<div id="ttl">Bu yılın<br><em>son karesi</em></div>'
html=f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:#0B0B0D;overflow:hidden;font-family:Inter,sans-serif;color:#fff}}
#vp{{position:absolute;left:0;top:{VT}px;width:{VW}px;height:{VH}px;overflow:hidden;background:#000}}
#stage{{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0;transform:scale({SC})}}
.sc{{position:absolute;inset:0;opacity:0;overflow:hidden}}
.sc img{{position:absolute;left:0;top:0;width:1920px;height:1080px;opacity:0}}
#off{{position:absolute;left:975px;top:548px;width:280px;height:130px;border-radius:50%;background:radial-gradient(ellipse at center,#0D0C07 55%,rgba(13,12,7,0) 72%)}}
#grain{{position:absolute;left:0;top:{VT}px;width:{VW}px;height:{VH}px;opacity:.09;mix-blend-mode:overlay;pointer-events:none}}
#vig{{position:absolute;left:0;top:{VT}px;width:{VW}px;height:{VH}px;background:radial-gradient(ellipse at center,transparent 55%,rgba(0,0,0,.45));pointer-events:none}}
.sub{{position:absolute;left:0;right:0;top:{subtop}px;text-align:center;font-size:{fs}px;font-weight:600;line-height:1.3;text-shadow:0 2px 18px rgba(0,0,0,.85),0 0 4px rgba(0,0,0,.6);opacity:0;padding:0 60px}}
#cd{{position:absolute;left:{int(330*SC)}px;top:{VT+int(330*SC)}px;width:{int(420*SC)}px;text-align:center;font-family:'Inter Display',Inter;font-weight:800;font-size:{int(300*SC)}px;line-height:1;color:#C6F24E;text-shadow:0 0 40px rgba(198,242,78,.55);opacity:0}}
#ttl{{position:absolute;left:0;right:0;top:300px;text-align:center;font-family:'Inter Display',Inter;font-weight:800;font-size:84px;line-height:1.05;letter-spacing:-1px;opacity:0}}
#ttl em{{font-style:normal;color:#C6F24E}}
#end{{position:absolute;inset:0;background:#0B0B0D;opacity:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 90px}}
#e1{{font-family:'Inter Display',Inter;font-weight:800;font-size:{64 if MODE=="h" else 70}px;line-height:1.15;letter-spacing:-.5px;opacity:0}}
#e1 em{{font-style:normal;color:#C6F24E}}
#e2{{margin-top:48px;font-size:{44 if MODE=="h" else 48}px;font-weight:600;color:#d8d8dc;opacity:0}}
#e3{{margin-top:36px;display:inline-block;background:#FF2E93;color:#fff;font-weight:800;font-size:{38 if MODE=="h" else 44}px;padding:18px 44px;border-radius:999px;opacity:0}}
#hd{{position:absolute;left:40px;bottom:36px;font-size:26px;font-weight:600;color:rgba(255,255,255,.6);opacity:{0 if MODE=="h" else 1}}}
</style></head><body>
{title}
<div id="vp"><div id="stage">{sc_html}</div></div>
<canvas id="grain" width="480" height="270"></canvas><div id="vig"></div>
<div id="cd"></div>
{sub_html}
<div id="hd">@frame.labo</div>
<div id="end"><div id="e1">Bu videoyu baştan sona<br><em>yapay zekâyla</em> biz ürettik.</div><div id="e2">Markan için de üretelim.</div><div id="e3">DM'den yaz</div></div>
<script>
const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)), E=x=>1-Math.pow(1-cl(x),3), S=x=>{{x=cl(x);return x*x*(3-2*x)}};
const win=(t,a,b,fi=.5,fo=.5)=>cl((t-a)/fi)*cl((b-t)/fo);
const SCN={[[i,a,b,len(frs)] for i,a,b,frs in scenes]};
const SUBS={[[a,b] for a,b,t in subs]};
const KB={{s1:[1.0,1.11,'62% 58%',0,0],s2:[1.03,1.12,'40% 50%',0,0],s3:[1.13,1.0,'50% 45%',0,0],s4:[1.02,1.06,'70% 60%',0,0],s5:[1.0,1.08,'50% 70%',30,-30]}};
// tane: önceden üretilmiş gürültü kareleri
const G=$('grain'), gx=G.getContext('2d'), NZ=[];
for(let n=0;n<6;n++){{const im=gx.createImageData(480,270);for(let i=0;i<im.data.length;i+=4){{const v=Math.random()*255;im.data[i]=im.data[i+1]=im.data[i+2]=v;im.data[i+3]=255;}}NZ.push(im);}}
window.DUR=31.0;
window.SFX=[[0.2,'whoosh'],[15.2,'tick'],[15.9,'tick'],[16.6,'tick'],[26.9,'ding']];
window.render=function(t){{
  gx.putImageData(NZ[Math.floor(t*30)%6],0,0);
  for(const [id,a,b,n] of SCN){{
    const el=$(id), o=win(t,a,b,id=='s1'?0.4:0.6,0.6); el.style.opacity=o;
    const k=KB[id], p=S((t-a)/(b-a)), s=k[0]+(k[1]-k[0])*p, ty=k[3]+(k[4]-k[3])*p;
    el.style.transformOrigin=k[2]; el.style.transform=`translateY(${{ty}}px) scale(${{s}})`;
    const q=cl((t-a)/(b-a))*(n-1), f0=Math.floor(q), fr=q-f0;
    for(let j=0;j<n;j++){{const im=$(id+'f'+j); im.style.opacity= j<f0?1 : j==f0?1 : j==f0+1?S(fr):0; im.style.zIndex=j;}}
  }}
  // ekran açılışı
  const ft=t; let off=1;
  if(ft>1.4) off=0.25; if(ft>1.5) off=0.9; if(ft>1.6) off=0.1; if(ft>1.68) off=0.55; if(ft>1.76) off=0;
  $('off').style.opacity=off;
  SUBS.forEach(([a,b],k)=>{{const v=win(t,a,b,.45,.4); const e=$('sb'+k); e.style.opacity=v; e.style.transform=`translateY(${{(1-E((t-a)/.6))*14}}px)`;}});
  // sayaç
  const cd=$('cd'); let num='', cv=0, cs=1;
  [[15.2,'3'],[15.9,'2'],[16.6,'1']].forEach(([a,s])=>{{if(t>=a&&t<a+0.7){{num=s; const u=(t-a)/0.7; cv=cl(u/0.12)*cl((1-u)/0.25); cs=1.25-0.25*E(u/0.4);}}}});
  cd.textContent=num; cd.style.opacity=cv; cd.style.transform=`scale(${{cs}})`;
  const tt=$('ttl'); if(tt){{tt.style.opacity=win(t,0.3,26.3,.6,.5);}}
  // kapanış kartı
  $('end').style.opacity=cl((t-26.3)/0.6);
  $('e1').style.opacity=cl((t-26.9)/0.5); $('e1').style.transform=`translateY(${{(1-E((t-26.9)/0.7))*24}}px)`;
  $('e2').style.opacity=cl((t-28.0)/0.5); $('e3').style.opacity=cl((t-28.6)/0.4); $('e3').style.transform=`scale(${{0.8+0.2*E((t-28.6)/0.4)}})`;
}};
</script></body></html>'''
open(OUT,"w").write(html)
