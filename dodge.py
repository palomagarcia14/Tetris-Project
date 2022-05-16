# Hayley took the working code and readjusted the previous intro screen so that it was compatible with the new screen dimensions.
# She also added text to the game screen and made edits throughout the to accomodate the need for text fonts and colors. This took about two hours. 

import sys
import pygame as pg
from pygame.locals import KEYDOWN, K_q
import time
import random

pg.font.init()
font = pg.font.SysFont('freesansbold.ttf', 48)

SCREENSIZE = WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
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



def main():
    global canfall, s1,s2,s3,s4,scolor
    global canfalla, a1,a2,a3,a4,acolor
    pg.init()
    _VARS['surf'] = pg.display.set_mode(SCREENSIZE)
    while True:
        checkEvents()
        _VARS['surf'].fill(BLACK)
        drawGrid1()
        drawBounds()
        leftright()
        font = pg.font.SysFont('freesansbold.ttf', 48)
        dodge_text = font.render("Dodge the blocks!", True, WHITE)
        Screen.blit(dodge_text, (160,25))
        if canfall == True:
            squareFall()
        elif canfall == False:
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
            squareFalla()
        elif canfalla == False:
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
    for i in range(5, 20):
        for j in range(5, 15):
            pg.draw.rect(_VARS['surf'], color, pg.Rect(j*25, i*25,25,25), 2)

    pg.draw.rect(_VARS['surf'], [255,0,0], lilguy)
    pg.display.flip()

def drawBounds():

    pg.draw.rect(_VARS['surf'], [255,0,255], b1)
    pg.draw.rect(_VARS['surf'], [255,0,255], b2)
    pg.draw.rect(_VARS['surf'], [255,0,255], b3)
    pg.draw.rect(_VARS['surf'], [255,0,255], b4)


def squareFall():
    global canfall, s1,s2,s3,s4,scolor


    if s3.colliderect(b1) :
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

def squareFalla():
    global canfalla, a1,a2,a3,a4,acolor
    if a3.colliderect(b1):
            pg.draw.rect(_VARS['surf'], scolor, a1)
            pg.draw.rect(_VARS['surf'], scolor, a2)
            pg.draw.rect(_VARS['surf'], scolor, a3)
            pg.draw.rect(_VARS['surf'], scolor, a4)
            canfalla = False
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

def gameover():
    global canfalla, a1,a2,a3,a4
    global canfall, s1,s2,s3,s4
    if lilguy.colliderect(a1) or lilguy.colliderect(a2) or lilguy.colliderect(a3) or lilguy.colliderect(a4)  or lilguy.colliderect(s1) or lilguy.colliderect(s2)  or lilguy.colliderect(s3)  or lilguy.colliderect(s4):
        sys.exit()


def checkEvents():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
     
# Function for instructions screen
def start_screen():
    run = True
    while run:
        # Make background black: 
        Screen.fill((0,0,0))
        # Create text: 
        font2 = pg.font.SysFont('freesansbold.ttf', 26)
        dodge_text = font.render("Dodge the blocks!", True, WHITE)
        how2play_text = font.render("HOW TO PLAY:", True, RED)
        instructions1_text = font2.render("Blocks will fall from the top of the grid. Using the arrows on your", True, WHITE)
        instructions2_text = font2.render("your keyboard, you can move the red square left, right, up, and ", True, WHITE)
        instructions3_text = font2.render("down.The objective is to dodge the falling blocks. When you", True, WHITE)
        instructions4_text = font2.render("succesfully dodge the falling blocks, you will be rewarded points.", True, WHITE)
        instructions5_text = font2.render("If the blocks and red square collide, the game will be terminated.", True, WHITE)
        start_text = font.render("Press any key to start.", True, RED)
        # Draw text on screen: 
        Screen.blit(dodge_text, (160, 25))
        Screen.blit(how2play_text, (180, 150))
        Screen.blit(instructions1_text, (36,210))
        Screen.blit(instructions2_text, (34, 235))
        Screen.blit(instructions3_text, (35, 260))
        Screen.blit(instructions4_text, (28,285))
        Screen.blit(instructions5_text, (33,310))
        Screen.blit(start_text, (135, 400))
        pg.display.update()
        # Key presses: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                main()

    pg.quit()

# Window dimensions and caption: 
Screen = pg.display.set_mode((600,600))
pg.display.set_caption('Dodge the blocks')

start_screen() # Start game
