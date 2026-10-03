# Folded-ribbon «М» + «Машина.РФ» wordmark, redrawn from the founder's sample
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
HERE=os.path.dirname(os.path.abspath(__file__))
B=os.path.join(HERE,'fonts')+'/'
NAVY=(16,46,122)

# geometry in a 1024 space (from the sample)
LSTEM=[(245,268),(336,268),(336,650),(245,650)]
RSTEM=[(640,268),(735,268),(735,650),(640,650)]
RDIAG=[(490,478),(640,268),(733,268),(500,628)]
LDIAG=[(248,268),(345,268),(490,478),(500,628),(470,628)]
BOX=(245,268,735,650)

def _mask(poly,W,H,s,ox,oy):
    m=Image.new('L',(W,H),0)
    ImageDraw.Draw(m).polygon([((x-ox)*s,(y-oy)*s) for x,y in poly],fill=255)
    return np.asarray(m,dtype=np.float32)/255

def mark(height, ss=4):
    """white folded M on transparent background; returns RGBA of given height"""
    ox,oy=BOX[0]-4,BOX[1]-4; w0,h0=BOX[2]-BOX[0]+8,BOX[3]-BOX[1]+8
    s=height*ss/h0; W,H=int(w0*s),int(h0*s)
    yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
    X=xx/s+ox; Y=yy/s+oy
    out=np.zeros((H,W,4),np.float32)
    def layer(poly,shade):
        a=_mask(poly,W,H,s,ox,oy)
        col=np.stack([255-shade*(255-c) for c in (58,82,140)],-1)  # shade blends white -> ribbon blue
        out[...,:3]=out[...,:3]*(1-a[...,None])+col*a[...,None]
        out[...,3]=np.maximum(out[...,3],a)
    # stems: soft vertical falloff
    layer(LSTEM,0.10*np.clip((Y-268)/382,0,1)+0.06*np.clip((336-X)/91,0,1))
    layer(RSTEM,0.08*np.clip((Y-268)/382,0,1))
    # right diagonal: slight shade toward the V
    layer(RDIAG,0.18*np.clip((Y-420)/208,0,1)**1.5)
    # left diagonal = the fold: dark band along its lower-left edge, strongest mid-to-low
    # signed distance across the ribbon: 0 at lower-left edge (248,268)->(470,628), 1 at upper-right edge
    ax,ay=248,268; bx,by=470,628; nx,ny=by-ay,-(bx-ax); nl=(nx*nx+ny*ny)**.5; nx,ny=nx/nl,ny/nl
    d=-((X-ax)*nx+(Y-ay)*ny)  # positive inside the ribbon
    t=np.clip(d/58,0,1)
    u=np.clip((Y-268)/360,0,1)
    fold=(1-t)**1.6*np.clip((u-0.08)/0.55,0,1)*(1-0.35*np.clip((u-0.85)/0.15,0,1))
    layer(LDIAG,0.78*fold+0.10*(1-t)*np.clip(u/0.3,0,1)+0.04)
    # thin crease shadow where the left diagonal overlaps the left stem
    im=Image.fromarray(np.clip(out*[1,1,1,255],0,255).astype(np.uint8),'RGBA')
    return im.resize((int(W/ss),int(H/ss)),Image.LANCZOS)

def _f(sub,w,size): return ImageFont.truetype(B+f'Montserrat-{sub}-{w}.ttf',size)
def wordmark_len(size,w='700'):
    c=_f('cyrillic',w,size); l=_f('latin',w,size)
    return c.getlength('Машина')+l.getlength('.')+c.getlength('РФ')
def wordmark(d,x,y,size,fill,w='700'):
    c=_f('cyrillic',w,size); l=_f('latin',w,size)
    d.text((x,y),'Машина',font=c,fill=fill); x+=c.getlength('Машина')
    d.text((x,y),'.',font=l,fill=fill); x+=l.getlength('.')
    d.text((x,y),'РФ',font=c,fill=fill)

def full_logo(size,bg=NAVY,scale=1.0):
    """the sample composition: big M + wordmark below, on navy"""
    im=Image.new('RGB',(size,size),bg); k=size/1024*scale
    m=mark(int(382*k)); cx=size/2
    my=size/2-(512-268)*k
    im.paste(m,(int(cx-m.width/2),int(my)),m)
    d=ImageDraw.Draw(im); fs=int(118*k)
    wl=wordmark_len(fs); wordmark(d,cx-wl/2,size/2+(735-512)*k-fs*0.2,fs,(255,255,255))
    return im

def icon(size,radius=0.24):
    """navy rounded square with the M — used next to the wordmark on light backgrounds"""
    ss=4; S=size*ss
    im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,S-1,S-1],radius=int(S*radius),fill=NAVY+(255,))
    m=mark(int(S*0.5),ss=1)
    im.alpha_composite(m,(int((S-m.width)/2),int((S-m.height)/2)))
    return im.resize((size,size),Image.LANCZOS)

def lockup(d_im,x,y,h,color=NAVY):
    """icon + wordmark, height h; draws on RGB image, returns width"""
    ic=icon(int(h)); d_im.paste(ic,(int(x),int(y)),ic)
    d=ImageDraw.Draw(d_im); fs=int(h*0.62)
    wordmark(d,x+h*1.28,y+h*0.5-fs*0.62,fs,color)
    return h*1.28+wordmark_len(fs)
