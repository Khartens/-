import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from render import *
from covers_data import C,SERIES
X=84; MAXW=1080-2*X
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','covers')+'/'
def cover(path,series,main,accent):
    W,H=1080,1920; im,d=canvas(W,H)
    logo(d,X,300,54)
    s=group_size([(main,accent)],MAXW,96); f,lines,s=two_lines(main,accent,s); SZ[path[-7:-4]]=s
    th=len(lines)*s*1.18
    lab=40; block=lab*1.45+60+th
    y0=960-block/2
    label(d,X,y0,SERIES[series],lab)
    draw_title(d,X,y0+lab*1.45+60,f,lines,s,lh=1.18)
    fm=font('Regular',38); d.text((X,1560),'mashinarf.ru',font=fm,fill=MUTED)
    arrow_btn(d,W-X-44,1560+24,44)
    im.save(path,'JPEG',quality=92,optimize=True,progressive=True)
SZ={}
ids=sys.argv[1:] or list(C)
for k in ids:
    cover(OUT+k+'.jpg',*C[k])
print('done',len(ids)); import collections; print(sorted(collections.Counter(SZ.values()).items())); print([k for k,v in SZ.items() if v<80])
