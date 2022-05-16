import sys
import pygame as pg
from pygame.locals import KEYDOWN, K_q
import time
import random

gameDisplay = pg.display.set_mode((600, 600))
SCREENSIZE = WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255,255,255)
PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 70,70
SQUARE_LEN = 25
SQUARE_WID = 25
color = (220,220,220)
_VARS = {'surf': False}
STARTX = 250
step = 25
lilguy = pg.Rect(STARTX, 425, SQUARE_LEN, SQUARE_WID)

b1 = pg.Rect(5*25, 20*25,250,25)
b2 = pg.Rect(5*25, 4*25,250,25)
b3 = pg.Rect(4*25, 4*25,25,425)
b4 = pg.Rect(15*25, 4*25,25,425)
plist = [1, 2, 3 ,4,5]
randi = random.choice(plist)
if randi == 1: #square
    s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
    s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
    s3 = pg.Rect(STARTX, 125, SQUARE_LEN, SQUARE_WID)
    s4 = pg.Rect(STARTX + SQUARE_LEN, 125, SQUARE_LEN, SQUARE_WID)
    scolor = [255,255,0]
elif randi == 2:#line
    s1 = pg.Rect(STARTX-25, 100, SQUARE_LEN, SQUARE_WID)
    s2 = pg.Rect(STARTX + SQUARE_LEN-25, 100, SQUARE_LEN, SQUARE_WID)
    s3 = pg.Rect(STARTX- SQUARE_LEN-25, 100, SQUARE_LEN, SQUARE_WID)
    s4 = pg.Rect(STARTX+ SQUARE_LEN +SQUARE_LEN-25, 100, SQUARE_LEN, SQUARE_WID)
    scolor = [0,255,255]
elif randi == 3:#w
    s1 = pg.Rect(STARTX-50, 100, SQUARE_LEN, SQUARE_WID)
    s2 = pg.Rect(STARTX + SQUARE_LEN-50, 100, SQUARE_LEN, SQUARE_WID)
    s4 = pg.Rect(STARTX- SQUARE_LEN-50, 100, SQUARE_LEN, SQUARE_WID)
    s3 = pg.Rect(STARTX-50, 125, SQUARE_LEN, SQUARE_WID)
    scolor = [255,0,255]
elif randi == 4:
    s1 = pg.Rect(STARTX+50, 100, SQUARE_LEN, SQUARE_WID)
    s2 = pg.Rect(STARTX + SQUARE_LEN+50, 100, SQUARE_LEN, SQUARE_WID)
    s4 = pg.Rect(STARTX- SQUARE_LEN+50, 100, SQUARE_LEN, SQUARE_WID)
    s3 = pg.Rect(STARTX- SQUARE_LEN+50, 125, SQUARE_LEN, SQUARE_WID)
    scolor = [255, 128, 0]
elif randi == 5:
    s1 = pg.Rect(STARTX-75, 100, SQUARE_LEN, SQUARE_WID)
    s2 = pg.Rect(STARTX + SQUARE_LEN-75, 100, SQUARE_LEN, SQUARE_WID)
    s3 = pg.Rect(STARTX- SQUARE_LEN-75, 125, SQUARE_LEN, SQUARE_WID)
    s4 = pg.Rect(STARTX-75, 125, SQUARE_LEN, SQUARE_WID)
    scolor = [0,255,128]
canfall = True

alist = [1, 2, 3 ,4,5]
randa = random.choice(alist)
if randa == 1: #square
    a1 = pg.Rect(STARTX, 175, SQUARE_LEN, SQUARE_WID)
    a2 = pg.Rect(STARTX + SQUARE_LEN, 175, SQUARE_LEN, SQUARE_WID)
    a3 = pg.Rect(STARTX, 200, SQUARE_LEN, SQUARE_WID)
    a4 = pg.Rect(STARTX + SQUARE_LEN, 200, SQUARE_LEN, SQUARE_WID)
    acolor = [255,255,0]
elif randa == 2:#line
    a1 = pg.Rect(STARTX+25, 175, SQUARE_LEN, SQUARE_WID)
    a2 = pg.Rect(STARTX + SQUARE_LEN+25, 175, SQUARE_LEN, SQUARE_WID)
    a3 = pg.Rect(STARTX- SQUARE_LEN+25, 175, SQUARE_LEN, SQUARE_WID)
    a4 = pg.Rect(STARTX+ SQUARE_LEN +SQUARE_LEN+25, 175, SQUARE_LEN, SQUARE_WID)
    acolor = [0,255,255]
elif randa == 3:#w
    a1 = pg.Rect(STARTX+50, 175, SQUARE_LEN, SQUARE_WID)
    a2 = pg.Rect(STARTX + SQUARE_LEN+50, 175, SQUARE_LEN, SQUARE_WID)
    a4 = pg.Rect(STARTX- SQUARE_LEN+50, 175, SQUARE_LEN, SQUARE_WID)
    a3 = pg.Rect(STARTX+50, 200, SQUARE_LEN, SQUARE_WID)
    acolor = [255,0,255]
elif randa == 4:
    a1 = pg.Rect(STARTX-50, 175, SQUARE_LEN, SQUARE_WID)
    a2 = pg.Rect(STARTX + SQUARE_LEN-50, 175, SQUARE_LEN, SQUARE_WID)
    a4 = pg.Rect(STARTX- SQUARE_LEN-50, 175, SQUARE_LEN, SQUARE_WID)
    a3 = pg.Rect(STARTX- SQUARE_LEN-50, 200, SQUARE_LEN, SQUARE_WID)
    acolor = [255, 128, 0]
elif randa == 5:
    a1 = pg.Rect(STARTX+75, 175, SQUARE_LEN, SQUARE_WID)
    a2 = pg.Rect(STARTX + SQUARE_LEN+75, 175, SQUARE_LEN, SQUARE_WID)
    a3 = pg.Rect(STARTX- SQUARE_LEN+75, 200, SQUARE_LEN, SQUARE_WID)
    a4 = pg.Rect(STARTX+75, 200, SQUARE_LEN, SQUARE_WID)
    acolor = [0,255,128]
canfalla = True

current_score = 0

def main():
    global canfall, s1,s2,s3,s4,scolor
    global canfalla, a1,a2,a3,a4,acolor
    pg.init()
    _VARS['surf'] = pg.display.set_mode(SCREENSIZE)
    while True:
        checkEvents()
        _VARS['surf'].fill(BLACK)
        drawBounds()
        leftright()
        if canfall == True:
            drawGrid1()
            squareFall()
        elif canfall == False:
            drawGrid1()
            plist = [1, 2, 3 ,4,5]
            randi = random.choice(plist)
            if randi == 1: #square
                s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
                s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
                s3 = pg.Rect(STARTX, 125, SQUARE_LEN, SQUARE_WID)
                s4 = pg.Rect(STARTX + SQUARE_LEN, 125, SQUARE_LEN, SQUARE_WID)
                scolor = [255,255,0]
            elif randi == 2:#line
                s1 = pg.Rect(STARTX-25, 100, SQUARE_LEN, SQUARE_WID)
                s2 = pg.Rect(STARTX + SQUARE_LEN-25, 100, SQUARE_LEN, SQUARE_WID)
                s3 = pg.Rect(STARTX- SQUARE_LEN-25, 100, SQUARE_LEN, SQUARE_WID)
                s4 = pg.Rect(STARTX+ SQUARE_LEN +SQUARE_LEN-25, 100, SQUARE_LEN, SQUARE_WID)
                scolor = [0,255,255]
            elif randi == 3:#w
                s1 = pg.Rect(STARTX-50, 100, SQUARE_LEN, SQUARE_WID)
                s2 = pg.Rect(STARTX + SQUARE_LEN-50, 100, SQUARE_LEN, SQUARE_WID)
                s4 = pg.Rect(STARTX- SQUARE_LEN-50, 100, SQUARE_LEN, SQUARE_WID)
                s3 = pg.Rect(STARTX-50, 125, SQUARE_LEN, SQUARE_WID)
                scolor = [255,0,255]
            elif randi == 4:
                s1 = pg.Rect(STARTX+50, 100, SQUARE_LEN, SQUARE_WID)
                s2 = pg.Rect(STARTX + SQUARE_LEN+50, 100, SQUARE_LEN, SQUARE_WID)
                s4 = pg.Rect(STARTX- SQUARE_LEN+50, 100, SQUARE_LEN, SQUARE_WID)
                s3 = pg.Rect(STARTX- SQUARE_LEN+50, 125, SQUARE_LEN, SQUARE_WID)
                scolor = [255, 128, 0]
            elif randi == 5:
                s1 = pg.Rect(STARTX-75, 100, SQUARE_LEN, SQUARE_WID)
                s2 = pg.Rect(STARTX + SQUARE_LEN-75, 100, SQUARE_LEN, SQUARE_WID)
                s3 = pg.Rect(STARTX- SQUARE_LEN-75, 125, SQUARE_LEN, SQUARE_WID)
                s4 = pg.Rect(STARTX-75, 125, SQUARE_LEN, SQUARE_WID)
                scolor = [0,255,128]
            pg.draw.rect(_VARS['surf'], scolor, s1)
            pg.draw.rect(_VARS['surf'], scolor, s2)
            pg.draw.rect(_VARS['surf'], scolor, s3)
            pg.draw.rect(_VARS['surf'], scolor, s4)
            canfall = True
        if canfalla == True:
            drawGrid1()
            squareFalla()
        elif canfalla == False:
            drawGrid1()
            alist = [1, 2, 3 ,4,5]
            randa = random.choice(alist)
            if randa == 1: #square
                a1 = pg.Rect(STARTX, 175, SQUARE_LEN, SQUARE_WID)
                a2 = pg.Rect(STARTX + SQUARE_LEN, 175, SQUARE_LEN, SQUARE_WID)
                a3 = pg.Rect(STARTX, 200, SQUARE_LEN, SQUARE_WID)
                a4 = pg.Rect(STARTX + SQUARE_LEN, 200, SQUARE_LEN, SQUARE_WID)
                acolor = [255,255,0]
            elif randa == 2:#line
                a1 = pg.Rect(STARTX+25, 175, SQUARE_LEN, SQUARE_WID)
                a2 = pg.Rect(STARTX + SQUARE_LEN+25, 175, SQUARE_LEN, SQUARE_WID)
                a3 = pg.Rect(STARTX- SQUARE_LEN+25, 175, SQUARE_LEN, SQUARE_WID)
                a4 = pg.Rect(STARTX+ SQUARE_LEN +SQUARE_LEN+25, 175, SQUARE_LEN, SQUARE_WID)
                acolor = [0,255,255]
            elif randa == 3:#w
                a1 = pg.Rect(STARTX+50, 175, SQUARE_LEN, SQUARE_WID)
                a2 = pg.Rect(STARTX + SQUARE_LEN+50, 175, SQUARE_LEN, SQUARE_WID)
                a4 = pg.Rect(STARTX- SQUARE_LEN+50, 175, SQUARE_LEN, SQUARE_WID)
                a3 = pg.Rect(STARTX+50, 200, SQUARE_LEN, SQUARE_WID)
                acolor = [255,0,255]
            elif randa == 4:
                a1 = pg.Rect(STARTX-50, 175, SQUARE_LEN, SQUARE_WID)
                a2 = pg.Rect(STARTX + SQUARE_LEN-50, 175, SQUARE_LEN, SQUARE_WID)
                a4 = pg.Rect(STARTX- SQUARE_LEN-50, 175, SQUARE_LEN, SQUARE_WID)
                a3 = pg.Rect(STARTX- SQUARE_LEN-50, 200, SQUARE_LEN, SQUARE_WID)
                acolor = [255, 128, 0]
            elif randa == 5:
                a1 = pg.Rect(STARTX+75, 175, SQUARE_LEN, SQUARE_WID)
                a2 = pg.Rect(STARTX + SQUARE_LEN+75, 175, SQUARE_LEN, SQUARE_WID)
                a3 = pg.Rect(STARTX- SQUARE_LEN+75, 200, SQUARE_LEN, SQUARE_WID)
                a4 = pg.Rect(STARTX+75, 200, SQUARE_LEN, SQUARE_WID)
                acolor = [0,255,128]
            pg.draw.rect(_VARS['surf'], acolor, a1)
            pg.draw.rect(_VARS['surf'], acolor, a2)
            pg.draw.rect(_VARS['surf'], acolor, a3)
            pg.draw.rect(_VARS['surf'], acolor, a4)
            canfalla = True


        pg.display.update()
        gameover()
        time.sleep(1)


#def sets():

def drawGrid1():
    global current_score
    for i in range(5, 20):
        for j in range(5, 15):
            pg.draw.rect(_VARS['surf'], color, pg.Rect(j*25, i*25,25,25), 2)
    pg.draw.rect(_VARS['surf'], (255, 0, 0), pg.Rect(435, 210, 125, 100))
    pg.font.init()
    my_font1 = pg.font.SysFont('Comic Sans MS', 50)
    text_surface = my_font1.render(str(current_score), False, (0, 0, 0))
    gameDisplay.blit(text_surface, (485,245))
    my_font2 = pg.font.SysFont('Comic Sans MS', 30)
    text_surface2 = my_font2.render('Score:', False, (0, 0, 0))
    gameDisplay.blit(text_surface2, (445,215))

    pg.display.flip()

def drawBounds():

    pg.draw.rect(_VARS['surf'], [255,0,255], b1)
    pg.draw.rect(_VARS['surf'], [255,0,255], b2)
    pg.draw.rect(_VARS['surf'], [255,0,255], b3)
    pg.draw.rect(_VARS['surf'], [255,0,255], b4)
    pg.draw.rect(_VARS['surf'], [255,0,0], lilguy)


def squareFall():
    global canfall, s1,s2,s3,s4,scolor
    global current_score


    if s3.colliderect(b1) :
            pg.draw.rect(_VARS['surf'], scolor, s1)
            pg.draw.rect(_VARS['surf'], scolor, s2)
            pg.draw.rect(_VARS['surf'], scolor, s3)
            pg.draw.rect(_VARS['surf'], scolor, s4)
            canfall = False
            current_score +=1


    else:

        v = [0, 25]
        s1.move_ip(v)
        pg.draw.rect(_VARS['surf'], scolor, s1)
        s2.move_ip(v)
        pg.draw.rect(_VARS['surf'], scolor, s2)
        s3.move_ip(v)
        pg.draw.rect(_VARS['surf'], scolor, s3)
        s4.move_ip(v)
        pg.draw.rect(_VARS['surf'], scolor, s4)

def squareFalla():
    global canfalla, a1,a2,a3,a4,acolor
    global current_score
    if a3.colliderect(b1):
            pg.draw.rect(_VARS['surf'], scolor, a1)
            pg.draw.rect(_VARS['surf'], scolor, a2)
            pg.draw.rect(_VARS['surf'], scolor, a3)
            pg.draw.rect(_VARS['surf'], scolor, a4)
            canfalla = False
            current_score +=1
    else:
        d = [0, 25]
        a1.move_ip(d)
        pg.draw.rect(_VARS['surf'], acolor, a1)
        a2.move_ip(d)
        pg.draw.rect(_VARS['surf'], acolor, a2)
        a3.move_ip(d)
        pg.draw.rect(_VARS['surf'], acolor, a3)
        a4.move_ip(d)
        pg.draw.rect(_VARS['surf'], acolor, a4)


def leftright():
    key_input = pg.key.get_pressed()
    if key_input[pg.K_LEFT]:
        b = [-step, 0]
        lilguy.move_ip(b)
    if key_input[pg.K_RIGHT]:
        c = [step, 0]
        lilguy.move_ip(c)
    if key_input[pg.K_UP]:
        y = [0, -step]
        lilguy.move_ip(y)
    if key_input[pg.K_DOWN]:
        z = [0, step]
        lilguy.move_ip(z)

def gameover():
    global canfalla, a1,a2,a3,a4
    global canfall, s1,s2,s3,s4
    if lilguy.colliderect(a1) or lilguy.colliderect(a2) or lilguy.colliderect(a3) or lilguy.colliderect(a4)  or lilguy.colliderect(s1) or lilguy.colliderect(s2)  or lilguy.colliderect(s3)  or lilguy.colliderect(s4):
        sys.exit()




def checkEvents():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()



if __name__ == '__main__':
    main()
