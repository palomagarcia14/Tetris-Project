import sys
import pygame as pg
from pygame.locals import KEYDOWN, K_q
import time

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
rect = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
s3 = pg.Rect(STARTX, 125, SQUARE_LEN, SQUARE_WID)
s4 = pg.Rect(STARTX + SQUARE_LEN, 125, SQUARE_LEN, SQUARE_WID)
b1 = pg.Rect(5*25, 20*25,250,25)
b2 = pg.Rect(5*25, 4*25,250,25)
b3 = pg.Rect(4*25, 4*25,25,425)
b4 = pg.Rect(15*25, 4*25,25,425)

def main():
    pg.init()
    _VARS['surf'] = pg.display.set_mode(SCREENSIZE)
    while True:
        checkEvents()
        _VARS['surf'].fill(BLACK)
        drawGrid1()
        drawBounds()
        leftright()
        squareFall()
        pg.display.update()
        time.sleep(1)




def drawGrid1():
    for i in range(5, 20):
        for j in range(5, 15):
            pg.draw.rect(_VARS['surf'], color, pg.Rect(j*25, i*25,25,25), 2)

    pg.display.flip()

def drawBounds():

    pg.draw.rect(_VARS['surf'], [255,0,255], b1)
    pg.draw.rect(_VARS['surf'], [255,0,255], b2)
    pg.draw.rect(_VARS['surf'], [255,0,255], b3)
    pg.draw.rect(_VARS['surf'], [255,0,255], b4)
    #pg.display.flip()




def squareFall():
    if s3.colliderect(b1):
            pg.draw.rect(_VARS['surf'], [255,0,0], s1)
            pg.draw.rect(_VARS['surf'], [255,0,0], s2)
            pg.draw.rect(_VARS['surf'], [255,0,0], s3)
            pg.draw.rect(_VARS['surf'], [255,0,0], s4)

    else:
        v = [0, 25]
        s1.move_ip(v)
        pg.draw.rect(_VARS['surf'], [255,0,0], s1)
        s2.move_ip(v)
        pg.draw.rect(_VARS['surf'], [255,0,0], s2)
        s3.move_ip(v)
        pg.draw.rect(_VARS['surf'], [255,0,0], s3)
        s4.move_ip(v)
        pg.draw.rect(_VARS['surf'], [255,0,0], s4)

def leftright():
    key_input = pg.key.get_pressed()
    if key_input[pg.K_LEFT]:
        b = [-step, 0]
        s1.move_ip(b)
        s2.move_ip(b)
        s3.move_ip(b)
        s4.move_ip(b)
    if key_input[pg.K_RIGHT]:
        c = [step, 0]
        s1.move_ip(c)
        s2.move_ip(c)
        s3.move_ip(c)
        s4.move_ip(c)



def checkEvents():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()



if __name__ == '__main__':
    main()
