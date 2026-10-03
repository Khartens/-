# Minimal visual system taken from mashinarf.ru header & hero CSS
from PIL import Image, ImageDraw, ImageFont
import os
HERE=os.path.dirname(os.path.abspath(__file__))
B=os.path.join(HERE,'fonts')+'/'
F={w:B+f'Inter-{w}.ttf' for w in ['ExtraBold','Bold','Medium','Regular']}
_fc={}
def font(w,s):
    k=(w,int(s))
    if k not in _fc: _fc[k]=ImageFont.truetype(F[w],int(s))
    return _fc[k]
def hx(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
WHITE=hx('#ffffff'); INK=hx('#0f172a'); NAVY=hx('#102e7a'); MUTED=hx('#64748b'); LEAD=hx('#5b6678')
LINE=hx('#e6eaf2'); CIRCLE=hx('#e3e9f5'); DOT=hx('#d5def2'); SOFT=hx('#f1f5fd'); ICONBG=hx('#eef2fb'); GOLD=hx('#d4af37')
TRACK=-0.03  # letter-spacing -.03em (site logo and titles)

def tlen(text,f,track=TRACK):
    return f.getlength(text)+track*f.size*max(len(text)-1,0)
def ttext(d,xy,text,f,fill,track=TRACK):
    x,y=xy
    for i,ch in enumerate(text):
        d.text((x+f.getlength(text[:i])+track*f.size*i,y),ch,font=f,fill=fill)

def canvas(W,H,circle=True,dots=True,soft=False):
    im=Image.new('RGB',(W,H),WHITE); d=ImageDraw.Draw(im)
    s=W/1080
    if soft:  # tile:before — soft circle in the bottom-right corner
        r=int(520*s); d.ellipse([W-r*1.25,H-r*1.3,W+r*0.75,H+r*0.7],fill=SOFT)
    if circle:  # hero:before — thin outline circle, top-right
        r=int(780*s); cx,cy=W+int(120*s),-int(80*s)
        d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=CIRCLE,width=max(2,int(3*s)))
    if dots:  # hero:after — dot grid
        st=int(36*s); rr=max(2,int(3.4*s)); x0,y0=int(W*0.52),int(150*s)
        for i in range(9):
            for j in range(6):
                x=x0+i*st; y=y0+j*st
                d.ellipse([x-rr,y-rr,x+rr,y+rr],fill=DOT)
    return im,d

def logo(d,x,y,size,color=NAVY,center=False):
    """founder's logo: navy icon with the folded М + «Машина.РФ» (Montserrat)"""
    from logo import lockup, wordmark_len
    h=size*1.3
    if center: x=x-(h*1.28+wordmark_len(int(h*0.62)))/2
    return lockup(d._image,x,y-size*0.1,h,color)

def label(d,x,y,text,size):
    f=font('Medium',size); ttext(d,(x,y),text,f,MUTED,track=0)
    w=f.getlength(text); d.rounded_rectangle([x,y+size*1.45,x+w,y+size*1.45+max(4,size*0.12)],radius=3,fill=GOLD)

def wrap(f,text,maxw):
    words=text.replace(' — ','\u00a0— ').split(' ')
    out=[];carry=[]
    for w in words:
        if len(w)<=2 and w not in ('—',):  # bind short words / numbers to the next word
            carry.append(w); continue
        out.append('\u00a0'.join(carry+[w])); carry=[]
    if carry:
        if out: out[-1]=out[-1]+'\u00a0'+'\u00a0'.join(carry)
        else: out.append('\u00a0'.join(carry))
    res=[]
    for w in out:  # split over-long hyphenated words
        if tlen(w,f)>maxw and '-' in w:
            a,b=w.split('-',1); res+=[a+'-',b]
        else: res.append(w)
    lines=[];cur=''
    for w in res:
        t=(cur+('' if cur.endswith('-') else ' ')+w) if cur else w
        if tlen(t.replace('\u00a0',' '),f)<=maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return [l.replace('\u00a0',' ') for l in lines]

def title_block(main,accent,maxw,maxh,hi,lo,lh=1.08):
    """returns (font, [(line,color)], size) — main in INK, accent in NAVY (site hero__title-accent)"""
    for s in range(hi,lo-1,-2):
        f=font('ExtraBold',s)
        lines=[(l,INK) for l in wrap(f,main,maxw)]
        if accent: lines+=[(l,NAVY) for l in wrap(f,accent,maxw)]
        if len(lines)*s*lh<=maxh and all(tlen(l,f)<=maxw for l,_ in lines): return f,lines,s
    f=font('ExtraBold',lo)
    return f,[(l,INK) for l in wrap(f,main,maxw)]+([(l,NAVY) for l in wrap(f,accent,maxw)] if accent else []),lo

def draw_title(d,x,y,f,lines,s,lh=1.08,center_w=None):
    for i,(l,c) in enumerate(lines):
        xx=x if center_w is None else x+(center_w-tlen(l,f))/2
        ttext(d,(xx,y+i*s*lh),l,f,c)
    return y+len(lines)*s*lh

def arrow_btn(d,cx,cy,r,filled=True):
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=NAVY if filled else ICONBG)
    c=WHITE if filled else NAVY; w=max(3,int(r*0.13))
    d.line([(cx-r*0.38,cy),(cx+r*0.36,cy)],fill=c,width=w)
    d.line([(cx+r*0.05,cy-r*0.32),(cx+r*0.38,cy)],fill=c,width=w)
    d.line([(cx+r*0.05,cy+r*0.32),(cx+r*0.38,cy)],fill=c,width=w)

def check_icon(d,x,y,sz):
    d.rounded_rectangle([x,y,x+sz,y+sz],radius=int(sz*0.28),fill=ICONBG)
    w=max(3,int(sz*0.09))
    d.line([(x+sz*0.28,y+sz*0.52),(x+sz*0.44,y+sz*0.67),(x+sz*0.73,y+sz*0.35)],fill=NAVY,width=w,joint='curve')

def button(d,x,y,text,size,filled=True):
    f=font('Bold',size); w=f.getlength(text); ph,pv=size*1.3,size*0.85
    box=[x,y,x+w+ph*2,y+size+pv*2]
    if filled: d.rounded_rectangle(box,radius=int(size*0.8),fill=NAVY)
    else: d.rounded_rectangle(box,radius=int(size*0.8),outline=NAVY,width=3)
    d.text((x+ph,y+pv-size*0.1),text,font=f,fill=WHITE if filled else NAVY)
    return box

# ---- exactly two lines: line 1 = main (INK), line 2 = accent (NAVY), one size per group ----
def group_size(pairs,maxw,cap,lo=40):
    s=cap
    for m,a in pairs:
        while s>lo and any(tlen(t,font('ExtraBold',s))>maxw for t in (m,a) if t): s-=1
    return s
def two_lines(main,accent,size):
    return font('ExtraBold',size),[(main,INK)]+([(accent,NAVY)] if accent else []),size
