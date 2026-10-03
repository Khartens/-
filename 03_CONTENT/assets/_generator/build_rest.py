import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from render import *
A=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')+'/'
def save(im,p): im.save(A+p,'PNG',optimize=True)
X=96
def footer(d,W,y,text='mashinarf.ru',s=1):
    d.text((X*s,y),text,font=font('Regular',int(36*s)),fill=MUTED)
    arrow_btn(d,W-X*s-42*s,y+22*s,42*s)

# ---------- profile ----------
from logo import full_logo, mark, icon, lockup, wordmark, wordmark_len
import os
for size,name in [(1080,'avatar-1080.png'),(640,'avatar-640-telegram-max.png')]:
    save(full_logo(size,scale=0.86),'profile/'+name)   # 0.86: fits the round crop
for f in ['avatar-white-1080.png','avatar-white-640-telegram-max.png']:
    if os.path.exists(A+'profile/'+f): os.remove(A+'profile/'+f)
os.makedirs(A+'logo',exist_ok=True)
save(full_logo(1024),'logo/logo-1024.png')
m=mark(900); save(m,'logo/logo-mark-white.png')
save(icon(1024),'logo/logo-icon-1024.png')
for col,name in [(NAVY,'logo-horizontal-navy.png'),(WHITE,'logo-horizontal-white.png')]:
    h=200; w=int(h*1.28+wordmark_len(int(h*0.62)))+8
    im=Image.new('RGBA',(w,h),(0,0,0,0)); lockup(im,0,0,h,col); save(im,'logo/'+name)

def banner(W,H,safe_w,safe_h,name,s):
    im,d=canvas(W,H,circle=False,dots=False); 
    r=int(H*0.9); d.ellipse([W-r*0.9,-r*0.75,W+r*1.1,r*1.25],outline=CIRCLE,width=max(2,int(3*s)))
    st=int(36*s); rr=max(2,int(3.4*s))
    for i in range(8):
        for j in range(5):
            x=int(W*0.08)+i*st; y=int(H*0.12)+j*st; d.ellipse([x-rr,y-rr,x+rr,y+rr],fill=DOT)
    sz=group_size([('Аренда транспорта','напрямую у владельцев')],safe_w,96); f,lines,sz=two_lines('Аренда транспорта','напрямую у владельцев',sz)
    sub=font('Regular',int(sz*0.36)); subt='По всей России — даже в небольших городах'
    lh=sz*0.62; total=lh+sz*0.55+len(lines)*sz*1.08+sz*0.36*2.2
    y=(H-total)/2
    logo(d,W/2,y,lh/1.3,center=True); y+=lh+sz*0.55
    y=draw_title(d,(W-safe_w)/2,y,f,lines,sz,center_w=safe_w)
    d.text(((W-sub.getlength(subt))/2,y+sz*0.36*0.9),subt,font=sub,fill=LEAD)
    save(im,'profile/'+name)
banner(1920,768,1196,520,'vk-cover-1920x768.png',1.0)
banner(2560,1440,1500,400,'youtube-banner-2560x1440.png',1.0)

# ---------- stories ----------
ST=[('Сегодня','важный день',None,None),
    ('Мы','запустились',None,None),
    ('Аренда транспорта','напрямую у владельцев','Самогрузы, Газели, экскаваторы, такси',None),
    ('Есть техника?','Разместим бесплатно','Пришлите 3 фото и цену',None),
    ('Нужна техника?','Оставьте заявку','Владельцы предложат цену сами','mashinarf.ru')]
SS=group_size([(m,a) for m,a,_,_ in ST],1080-2*X,72)
for i,(m,a,sub,btn) in enumerate(ST,1):
    W,H=1080,1920; im,d=canvas(W,H); logo(d,X,300,54)
    f,lines,s=two_lines(m,a,group_size([(m,a)],1080-2*X,96))
    th=len(lines)*s*1.18; extra=(44*1.6+40 if sub else 0)+(140 if btn else 0)
    y=960-(th+extra)/2
    y=draw_title(d,X,y,f,lines,s,lh=1.18)
    if sub:
        sf=font('Regular',44); d.text((X,y+40),sub,font=sf,fill=LEAD); y+=40+44*1.6
    if btn: button(d,X,y+50,btn,40)
    d.text((X,1560),f'{i} / 5',font=font('Regular',36),fill=MUTED)
    save(im,f'stories/launch-{i}.png')

# ---------- category cards ----------
CAT=[('01','gazel','Газели','и грузовики'),('02','samogruz','Самогрузы','и манипуляторы'),('03','excavator','Экскаваторы','и погрузчики'),
     ('04','bus','Автобусы','и микроавтобусы'),('05','motorhome','Автодома','для путешествий'),('06','snowmobile','Снегоходы','и квадроциклы'),
     ('07','paramotor','Мотопарапланы',''),('08','helicopter','Вертолёты','тоже здесь')]
CS=group_size([(m,a) for _,_,m,a in CAT],1080-2*X,104)
for n,slug,m,a in CAT:
    W,H=1080,1350; im,d=canvas(W,H,circle=False,soft=True); logo(d,X,110,50)
    d.text((X,470),n,font=font('Medium',44),fill=GOLD)
    f,lines,s=two_lines(m,a,CS)
    draw_title(d,X,560,f,lines,s,lh=1.18)
    footer(d,W,1180,'Аренда у владельцев · mashinarf.ru')
    save(im,f'cards/category-{n}-{slug}.png')

# ---------- price cards ----------
ROWS=[('Самогруз 5 т','за час'),('Газель с грузчиками','за час'),('Экскаватор-погрузчик','за час'),('Автовышка','за смену'),('Манипулятор 10 т','за час')]
PS=group_size([('Аренда техники.','Цены владельцев')],1080-2*X,84)
for city,slug in [('Цены владельцев','russia')]:
    W,H=1080,1350; im,d=canvas(W,H); logo(d,X,110,50)
    label(d,X,230,'Вся Россия',36)
    f,lines,s=two_lines('Аренда техники.',city,PS)
    y=draw_title(d,X,310,f,lines,s,lh=1.18)+44
    rh=110; g=14
    for name,unit in ROWS:
        d.rounded_rectangle([X,y,W-X,y+rh],radius=24,fill=WHITE,outline=LINE,width=3)
        d.text((X+36,y+18),name,font=font('Bold',40),fill=INK)
        d.text((X+36,y+66),unit,font=font('Regular',28),fill=MUTED)
        pf=font('Bold',42); pt='от _____ ₽'
        d.text((W-X-36-pf.getlength(pt),y+32),pt,font=pf,fill=NAVY)
        y+=rh+g
    footer(d,W,1220,'Осень 2026 · mashinarf.ru')
    save(im,'cards/prices.png')

# ---------- posts ----------
def bullets(d,y,items,sz=44):
    for t in items:
        check_icon(d,X,y,64); d.text((X+96,y+8),t,font=font('Medium',sz),fill=INK); y+=100
    return y
OWN=[('owners','Вся Россия','Заказы напрямую','без процентов',['Размещение бесплатно','Разместим за вас по 3 фото','Заявки приходят в Telegram']),
     ('owners-small-towns','Владельцам техники','Любой город,','даже небольшой',['Заказчики рядом с вами','Без диспетчера и процентов','Размещение бесплатно']),
     ('rentals','Для прокатов','Ваш прокат','без комиссии',['Загрузим ваш парк сами','Клиенты пишут напрямую','Снимем ролик о технике'])]
for slug,lab,m,a,items in OWN:
    W,H=1080,1350; im,d=canvas(W,H); logo(d,X,110,50)
    label(d,X,330,lab,36)
    f,lines,s=two_lines(m,a,group_size([(m,a)],1080-2*X,92))
    y=draw_title(d,X,420,f,lines,s,lh=1.18)+70
    bullets(d,y,items)
    footer(d,W,1180)
    save(im,f'posts/{slug}.png')
# launch: like site hero with two action cards
W,H=1080,1350; im,d=canvas(W,H); logo(d,X,110,50)
label(d,X,300,'Мы запустились',36)
f,lines,s=two_lines('Аренда транспорта','напрямую у владельцев',group_size([('Аренда транспорта','напрямую у владельцев')],1080-2*X,92))
y=draw_title(d,X,390,f,lines,s,lh=1.18)+60
for i,(t1,t2) in enumerate([('Нужна техника','Оставьте заявку — владельцы ответят'),('Есть техника','Разместите бесплатно')]):
    acc=i==0
    d.rounded_rectangle([X,y,W-X,y+150],radius=30,fill=WHITE,outline=NAVY if acc else LINE,width=3)
    d.rounded_rectangle([X+28,y+35,X+108,y+115],radius=22,fill=ICONBG)
    check_icon(d,X+36,y+43,64)
    d.text((X+136,y+32),t1,font=font('Bold',42),fill=INK)
    d.text((X+136,y+86),t2,font=font('Regular',32),fill=MUTED)
    arrow_btn(d,W-X-64,y+75,32,filled=acc)
    y+=180
d.text((X,y+20),'По всей России — даже в небольших городах',font=font('Regular',32),fill=LEAD)
footer(d,W,1180)
save(im,'posts/launch.png')
print('ok')
