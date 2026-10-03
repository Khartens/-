import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from render import *
from series_data import D
X=84; MAXW=1080-2*X
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','series')
os.makedirs(OUT,exist_ok=True)
def cover(path,lab,main,accent):
    W,H=1080,1920; im,d=canvas(W,H)
    logo(d,X,300,54)
    s=group_size([(main,accent)],MAXW,96); f,lines,s=two_lines(main,accent,s)
    th=len(lines)*s*1.18; labs=56; block=labs*1.45+60+th
    y0=960-block/2
    label(d,X,y0,lab,labs,color=NAVY,weight='Bold')
    draw_title(d,X,y0+labs*1.45+60,f,lines,s,lh=1.18)
    d.text((X,1560),'mashinarf.ru',font=font('Regular',38),fill=MUTED)
    arrow_btn(d,W-X-44,1560+24,44)
    im.save(path,'JPEG',quality=92,optimize=True,progressive=True)
    return s
ids=sys.argv[1:] or list(D)
sizes={k:cover(os.path.join(OUT,k+'.jpg'),*D[k]) for k in ids}
print('done',len(ids),'min size',min(sizes.values()),[k for k,v in sizes.items() if v<80])
