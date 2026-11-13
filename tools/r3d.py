"""Frame Lab 3D: tarayıcıda (WebGL2, yazılım) ışın yürütme ile 3D sahne çizer.
kullanım: python3 r3d.py <sahne> <cikti.png> [gen yuk] [json parametre]"""
import asyncio, json, sys, base64
FS = r"""#version 300 es
precision highp float;
uniform vec2 R; uniform int SC; uniform float T; uniform int FACE;
uniform vec3 BG0, BG1, RIMA, RIMB, OBJ; uniform vec2 GC; uniform float GR; uniform float YAW, PITCH, ZOOM, OY;
out vec4 o;
int M; vec3 LP;
mat2 rot(float a){float c=cos(a),s=sin(a);return mat2(c,-s,s,c);}
float sdRB(vec3 p, vec3 b, float r){vec3 q=abs(p)-b+r;return length(max(q,0.))+min(max(q.x,max(q.y,q.z)),0.)-r;}
float sdCap(vec3 p, vec3 a, vec3 b, float r){vec3 pa=p-a,ba=b-a;float h=clamp(dot(pa,ba)/dot(ba,ba),0.,1.);return length(pa-ba*h)-r;}
float sdRCyl(vec3 p, float ra, float rb, float h){vec2 d=vec2(length(p.xz)-ra+rb,abs(p.y)-h+rb);return min(max(d.x,d.y),0.)+length(max(d,0.))-rb;}
float sdTorus(vec3 p, vec2 t){vec2 q=vec2(length(p.xy)-t.x,p.z);return length(q)-t.y;}
float sdTri(vec2 p, float r){const float k=1.7320508;p.x=abs(p.x)-r;p.y=p.y+r/k;if(p.x+k*p.y>0.)p=vec2(p.x-k*p.y,-k*p.x-p.y)/2.;p.x-=clamp(p.x,-2.*r,0.);return -length(p)*sign(p.y);}
float sdBox2(vec2 p, vec2 b, float r){vec2 q=abs(p)-b+r;return length(max(q,0.))+min(max(q.x,q.y),0.)-r;}
void U(float d, int m, inout float D){if(d<D){D=d;M=m;}}
float GY;
float map(vec3 p){
  float D=1e9; M=0;
  U(p.y-GY, 5, D);
  vec3 q=p; q.y-=OY; q.y-=0.03*sin(T*2.0); q.xz*=rot(YAW+0.12*sin(T*1.3)); q.yz*=rot(PITCH);
  if(SC==0){ // Kare
    float head=sdRB(q-vec3(0.,.15,0.), vec3(.62,.5,.34), .17);
    float cut=sdRB(q-vec3(0.,.15,.36), vec3(.49,.37,.05), .11);
    head=max(head,-cut);
    U(head,1,D);
    float scr=sdRB(q-vec3(0.,.15,.29), vec3(.485,.365,.03), .10);
    if(scr<D){D=scr;M=2;LP=q;}
    U(sdCap(q,vec3(0.,.62,0.),vec3(0.,.93,0.),.028),1,D);
    U(length(q-vec3(0.,1.0,0.))-.095,3,D);
    U(sdRCyl(q-vec3(0.,-.42,0.),.10,.02,.10),1,D);
    U(sdRB(q-vec3(0.,-.56,0.), vec3(.40,.05,.17), .05),4,D);
  } else if(SC==1){ // oynat düğmesi
    vec2 t2=vec2(q.y,q.x+.08);
    float d2=sdTri(t2,.40)-.20;
    vec2 w=vec2(d2,abs(q.z)-.13);
    U(min(max(w.x,w.y),0.)+length(max(w,0.))-.09,1,D);
    vec3 s=p; s.y-=OY;
    U(length(s-vec3(.98,.62,-.3))-.15,6,D);
    U(length(s-vec3(-.9,-.55,.35))-.09,7,D);
    U(length(s-vec3(-.82,.78,-.5))-.11,3,D);
  } else if(SC==2){ // madeni paralar
    for(int i=0;i<4;i++){
      float fi=float(i);
      vec3 c=q-vec3(.05*sin(fi*2.1)-.15,-.48+fi*.15,.04*cos(fi*1.7));
      float d=sdRCyl(c,.50,.035,.068);
      if(i==3){ float g=abs(sdBox2(c.xz,vec2(.22),.07))-.022; d=max(d,-max(g,.045-c.y)); }
      U(d,1,D);
    }
    vec3 c=q-vec3(.72,-.20,.12); c.xy*=rot(-1.18);
    float d=sdRCyl(c,.50,.035,.068);
    float g=abs(sdBox2(c.xz,vec2(.22),.07))-.022; d=max(d,-max(g,.045-c.y));
    U(d,1,D);
    vec3 s=p; s.y-=OY;
    U(length(s-vec3(-.95,.55,-.2))-.12,6,D);
    U(length(s-vec3(1.05,.75,-.5))-.08,3,D);
  }
  return D;
}
vec3 nrm(vec3 p){vec2 e=vec2(.0012,0.);int m=M;vec3 n=normalize(vec3(map(p+e.xyy)-map(p-e.xyy),map(p+e.yxy)-map(p-e.yxy),map(p+e.yyx)-map(p-e.yyx)));M=m;return n;}
float shadow(vec3 ro, vec3 rd){float r=1.,t=.03;for(int i=0;i<48;i++){float h=map(ro+rd*t);r=min(r,9.*h/t);t+=clamp(h,.02,.25);if(r<.01||t>6.)break;}return clamp(r,0.,1.);}
float ao(vec3 p, vec3 n){float a=0.,s=1.;for(int i=1;i<=5;i++){float h=.05*float(i);a+=(h-map(p+n*h))*s;s*=.72;}return clamp(1.-2.2*a,0.,1.);}
vec3 lin(vec3 c){return pow(c,vec3(2.2));}
vec3 bg(vec2 uv){float d=length((uv-GC)*vec2(1.,.85))/GR;return mix(lin(BG0),lin(BG1),smoothstep(0.,1.,d));}
vec3 env(vec3 d){float t=smoothstep(.35,.95,d.y);float box=smoothstep(.55,.75,d.y)*smoothstep(.9,.2,abs(d.x));return vec3(.10)+vec3(1.4)*box+vec3(.25)*t;}
vec3 face(vec3 q){
  vec2 p=q.xy-vec2(0.,.15); vec3 c=vec3(0.);
  float aa=.006;
  vec2 e=vec2(abs(p.x)-.19,p.y-.05);
  float eye;
  if(FACE==2){ eye=abs(length(e-vec2(0.,-.03))-.075)-.02; eye=max(eye,-(e.y+.03)); }
  else eye=length(e)-.075;
  c+=vec3(1.)*smoothstep(aa,-aa,eye);
  if(FACE==1){ c*=smoothstep(-aa,aa,length(e-vec2(-.02*sign(p.x)+.0,-.015))-.032); c+=vec3(1.)*smoothstep(aa,-aa,abs(length(p-vec2(0.,-.15))-.04)-.014); }
  else { float m=abs(length(p-vec2(0.,-.08))-.11)-.018; m=max(m,p.y+.11); c+=vec3(1.)*smoothstep(aa,-aa,m); }
  vec2 k=abs(p)-vec2(.40,.28);
  float tick=min(max(abs(k.x)-.008,abs(k.y+.035)-.04),max(abs(k.y)-.008,abs(k.x+.035)-.04));
  c+=lin(vec3(.776,.949,.306))*.9*smoothstep(aa,-aa,tick);
  return c;
}
vec3 shade(vec2 uv){
  vec3 ro=vec3(0.,.25,ZOOM), ta=vec3(0.,.12,0.);
  if(SC==2){ro=vec3(0.,1.25,ZOOM);ta=vec3(0.,-.1,0.);}
  vec3 f=normalize(ta-ro), r=normalize(cross(f,vec3(0.,1.,0.))), u=cross(r,f);
  vec3 rd=normalize(f*3.6+r*uv.x+u*uv.y);
  float t=0.; int m=0; bool hit=false;
  for(int i=0;i<140;i++){float h=map(ro+rd*t); if(h<.0008){hit=true;break;} t+=h; if(t>14.)break;}
  vec3 B=bg(uv);
  if(!hit) return B;
  m=M; vec3 lp=LP; vec3 p=ro+rd*t; vec3 n=nrm(p);
  vec3 L=normalize(vec3(-.45,.9,.55));
  float sh=shadow(p+n*.004,L), a=ao(p,n);
  if(m==5){ float k=mix(.42,1.,sh)*mix(.6,1.,a); return B*k; }
  vec3 alb; float rough=.35; vec3 em=vec3(0.);
  if(m==1) alb=lin(OBJ);
  else if(m==2){ alb=vec3(.012); rough=.08; em=face(lp)*1.25; }
  else if(m==3) alb=lin(vec3(.55,.38,.98));
  else if(m==4){ alb=vec3(.02); rough=.25; }
  else if(m==6) alb=lin(vec3(1.,.18,.56));
  else alb=vec3(.9);
  float nl=max(dot(n,L),0.), nv=max(dot(n,-rd),0.);
  vec3 col=alb*(nl*sh*1.15+ (0.22+.20*n.y)*a);
  col+=alb*.35*lin(RIMA)*max(dot(n,normalize(vec3(.9,.1,-.3))),0.)*a;
  col+=alb*.35*lin(RIMB)*max(dot(n,normalize(vec3(-.9,.2,-.2))),0.)*a;
  float fr=.04+.96*pow(1.-nv,5.);
  vec3 h=normalize(L-rd);
  col+=pow(max(dot(n,h),0.),mix(220.,40.,rough))*sh*(1.-rough)*1.2;
  col+=env(reflect(rd,n))*fr*a*(1.-rough*.5);
  col+=pow(1.-nv,2.5)*(lin(RIMA)*smoothstep(-.2,.9,n.x)+lin(RIMB)*smoothstep(-.2,.9,-n.x))*.55;
  if(m==4||m==2) return col*.0+alb*(nl*sh+.2*a)+env(reflect(rd,n))*fr*a+pow(max(dot(n,h),0.),200.)*sh+em;
  return col+em;
}
float hash(vec2 p){return fract(sin(dot(p,vec2(12.9898,78.233)))*43758.5453);}
void main(){
  GY=(SC==0?-.78:(SC==1?-1.05:-.55))+OY;
  vec3 c=vec3(0.);
  for(int i=0;i<2;i++)for(int j=0;j<2;j++){
    vec2 fc=gl_FragCoord.xy+vec2(float(i),float(j))*.5-.25;
    c+=shade((2.*fc-R)/R.y);
  }
  c/=4.;
  c=c*(2.51*c+.03)/(c*(2.43*c+.59)+.14);
  c=pow(clamp(c,0.,1.),vec3(1./2.2));
  c+=(hash(gl_FragCoord.xy)-.5)/255.*2.;
  o=vec4(c,1.);
}"""
HTML = """<canvas id=c></canvas><script>
window.draw=(W,H,P)=>{const c=document.getElementById('c');c.width=W;c.height=H;
const g=c.getContext('webgl2',{preserveDrawingBuffer:true});
const sh=(t,s)=>{const x=g.createShader(t);g.shaderSource(x,s);g.compileShader(x);if(!g.getShaderParameter(x,g.COMPILE_STATUS))throw g.getShaderInfoLog(x);return x};
const p=g.createProgram();g.attachShader(p,sh(g.VERTEX_SHADER,'#version 300 es\\nin vec2 a;void main(){gl_Position=vec4(a,0.,1.);}'));
g.attachShader(p,sh(g.FRAGMENT_SHADER,window.FS));g.linkProgram(p);if(!g.getProgramParameter(p,g.LINK_STATUS))throw g.getProgramInfoLog(p);g.useProgram(p);
const b=g.createBuffer();g.bindBuffer(g.ARRAY_BUFFER,b);g.bufferData(g.ARRAY_BUFFER,new Float32Array([-1,-1,3,-1,-1,3]),g.STATIC_DRAW);
const l=g.getAttribLocation(p,'a');g.enableVertexAttribArray(l);g.vertexAttribPointer(l,2,g.FLOAT,false,0,0);
g.viewport(0,0,W,H);g.uniform2f(g.getUniformLocation(p,'R'),W,H);
for(const k in P){const v=P[k],u=g.getUniformLocation(p,k);if(k=='SC'||k=='FACE')g.uniform1i(u,v);else if(v.length==3)g.uniform3fv(u,v);else if(v.length==2)g.uniform2fv(u,v);else g.uniform1f(u,v);}
g.drawArrays(g.TRIANGLES,0,3);g.finish();return c.toDataURL('image/png');}
</script>"""
def hexc(h): h=h.lstrip('#'); return [int(h[i:i+2],16)/255 for i in (0,2,4)]
DEF = dict(SC=0, FACE=0, T=0.0, BG0="#2a2a30", BG1="#0B0B0D", RIMA="#C6F24E", RIMB="#FF2E93", OBJ="#C6F24E", GC=[0.0,0.1], GR=1.5, YAW=-0.42, PITCH=0.06, ZOOM=7.6, OY=0.0)
async def render(jobs):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox","--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
        pg = await b.new_page()
        await pg.set_content(HTML); await pg.evaluate("s=>{window.FS=s}", FS)
        for out, W, H, P in jobs:
            q = dict(DEF); q.update(P)
            for k in ("BG0","BG1","RIMA","RIMB","OBJ"): q[k] = hexc(q[k])
            d = await pg.evaluate("([W,H,P])=>window.draw(W,H,P)", [W, H, q])
            open(out, "wb").write(base64.b64decode(d.split(",")[1])); print(out)
        await b.close()
if __name__ == "__main__":
    jobs = json.load(open(sys.argv[1]))
    asyncio.run(render([(j["out"], j.get("w",1080), j.get("h",1350), j.get("p",{})) for j in jobs]))
