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
rect = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
# these longer rectangles were created as the border for the grid so that we could track if the shapes hit the boundaries. 
b1 = pg.Rect(5*25, 20*25,250,25)
b2 = pg.Rect(5*25, 4*25,250,25)
b3 = pg.Rect(4*25, 4*25,25,425)
b4 = pg.Rect(15*25, 4*25,25,425)

# the following list allowed us to pick out a random integer that corresponded to a particular shape type. 
plist = [1, 2, 3 ,4,5]
randi = random.choice(plist)
if randi == 1: #square shape
    s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
    s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
    s3 = pg.Rect(STARTX, 125, SQUARE_LEN, SQUARE_WID)
    s4 = pg.Rect(STARTX + SQUARE_LEN, 125, SQUARE_LEN, SQUARE_WID)
    scolor = [255,255,0]
elif randi == 2:#line shape
    s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
    s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
    s3 = pg.Rect(STARTX- SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
    s4 = pg.Rect(STARTX+ SQUARE_LEN +SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
    scolor = [0,255,255]
elif randi == 3:#w shape
    s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
    s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
    s4 = pg.Rect(STARTX- SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
    s3 = pg.Rect(STARTX, 125, SQUARE_LEN, SQUARE_WID)
    scolor = [255,0,255]
elif randi == 4:#L shape
    s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
    s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
    s4 = pg.Rect(STARTX- SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
    s3 = pg.Rect(STARTX- SQUARE_LEN, 125, SQUARE_LEN, SQUARE_WID)
    scolor = [255, 128, 0]
elif randi == 5: #s shape
    s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
    s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
    s3 = pg.Rect(STARTX- SQUARE_LEN, 125, SQUARE_LEN, SQUARE_WID)
    s4 = pg.Rect(STARTX, 125, SQUARE_LEN, SQUARE_WID)
    scolor = [0,255,128]
canfall = True
#this current score global variable was created by Paloma 
current_score = 0

def main():
    global canfall, s1,s2,s3,s4
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
                s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
                s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
                s3 = pg.Rect(STARTX- SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
                s4 = pg.Rect(STARTX+ SQUARE_LEN +SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
                scolor = [0,255,255]
            elif randi == 3:#w
                s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
                s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
                s4 = pg.Rect(STARTX- SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
                s3 = pg.Rect(STARTX, 125, SQUARE_LEN, SQUARE_WID)
                scolor = [255,0,255]
            elif randi == 4:
                s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
                s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
                s4 = pg.Rect(STARTX- SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
                s3 = pg.Rect(STARTX- SQUARE_LEN, 125, SQUARE_LEN, SQUARE_WID)
                scolor = [255, 128, 0]
            elif randi ==5:
                s1 = pg.Rect(STARTX, 100, SQUARE_LEN, SQUARE_WID)
                s2 = pg.Rect(STARTX + SQUARE_LEN, 100, SQUARE_LEN, SQUARE_WID)
                s3 = pg.Rect(STARTX- SQUARE_LEN, 125, SQUARE_LEN, SQUARE_WID)
                s4 = pg.Rect(STARTX, 125, SQUARE_LEN, SQUARE_WID)
                scolor = [0,255,128]
            pg.draw.rect(_VARS['surf'], scolor, s1)
            pg.draw.rect(_VARS['surf'], scolor, s2)
            pg.draw.rect(_VARS['surf'], scolor, s3)
            pg.draw.rect(_VARS['surf'], scolor, s4)
            canfall = True

        pg.display.update()
        time.sleep(1)

#def sets():

def drawGrid1():
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


def squareFall():
    global canfall, s1,s2,s3,s4

    if s3.colliderect(b1):
            pg.draw.rect(_VARS['surf'], scolor, s1)
            pg.draw.rect(_VARS['surf'], scolor, s2)
            pg.draw.rect(_VARS['surf'], scolor, s3)
            pg.draw.rect(_VARS['surf'], scolor, s4)
            canfall = False


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
