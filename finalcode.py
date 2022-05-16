# As a group, we spent about 10 hours planning our project, and downloading and learning Psychopy. We didn’t end up using PsychoPy, so we also all spent 
# about 4 hours learning pygame after switching. We also spent about 8 hours together trying to figure out how the class data structure worked in python 
# for piece generation, but ultimately gave up after trial and error and opted for a randomized list.

# In addition to the 20 hours spent in class, office hours, and group meetings to become acquainted with PyschoPy and Pygame, Hayley spent a great deal 
# of time coding the key presses, text, game and instruction screens. She spent about 6 hours learning how to draw text/buttons and position them on the
# screen in PsychoPy. She also experimented with PsychoPy events like the mouse click and key press reactions. She spent another 6 hours applying these 
# PsychoPy commands to create the first outlines of the introduction and game screens. When the group decided to use Pygame instead of PsychoPy, Hayley 
# then spent another 10 hours familiarizing herself with Pygame functions and converting the code that she had for the instruction and game screens. She
# spent an additional 4 hours experimenting with the keypress commands, getting a figure to move according to the arrows on the keyboard, and getting the
# instructions screen to shift to the game screen in reaction to a keypress. This took longer than anticipated because her keyboard initially would not 
# respond to keypresses because of limitations in her privacy settings. Hayley then spent about 5 hours helping her group to create different blocks and
# write functions that were an attempt to randomize the shapes, colors, and rotations of the blocks. When the group decided to shift from creating Tetris
# to a “Dodge the blocks” game, she spent another 6 hours translating pre-existing code so that it would be compatible with the new game and instruction 
# screens. 

# Imports: 
import sys
import pygame as pg
from pygame.locals import KEYDOWN, K_q
import time
import random

# Font - Hayley initialized and created the conditions for the font. 
pg.font.init()
font = pg.font.SysFont('freesansbold.ttf', 48)

# Constants: 
gameDisplay = pg.display.set_mode((600, 600))
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
# this following list allows each piece shape to correspond to a particular integer. This way, when a random integer is called from the list, a random
# shape will also appear. This took a lot of trial and error because our group didn't understand the difference between global and local variables. 
# This made it difficult for us to treat each piece independently. It took around 3 hours of group work to trouble shoot and Ashley spent an additional 4 
# hours to get everything in the correct coordinates, and 2 hours debugging to get the code reacting smoothly with the rest of the code. 
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
canfall = True # the canfall variable was very helpful for us as we struggled for a long time with how to signal to the game to allow a new piece to fall. 
# This was another thing that benefited fromt he knowledge of global variables. We also had to be very strategic as to when we were updating this variable.
#Overall piece generation was extremely hard for the group to achieve through our trials we looked a many online resources. We spent hours brainstorming 
# and Ashley spent around 8 hours trying many different variations of code to get this to work. 

# the Alist was a later addition to the code to make the game more interesting. The starting Y coordinates are lower on the screen so these pieces 
# are generated at different times than the pieces from the other lists. 
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

#the current_score variable was added by Paloma who researched how to have a global variable that can be updated constantly throughout the game. This was 
# important and also allowed us to better understand how global variables functioned. 
current_score = 0

# this main section was a new concept to the team that required some research into how it can be used effectively, and how it functions. This research was
# done by the whole group when we were learning how pygame functioned. We ran into a lot of issues with this early on, but eventually figured out how to make 
# it work for us. 
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
        # Hayley added text to top of the screen: 
        font = pg.font.SysFont('freesansbold.ttf', 48)
        dodge_text = font.render("Dodge the blocks!", True, WHITE)
        Screen.blit(dodge_text, (160,25))
        if canfall == True:
            drawGrid1()
            squareFall()
        elif canfall == False:
            drawGrid1()
            plist = [1, 2, 3 ,4,5] # this code from above is repeated here in order to get a new piece to generate every time the old piece can no longer fall
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



#this code draws the grid and score board using for-loops of coordinates. This was the 3rd grid we made, our first two were just made of lines, but this final one was made of
#individual squares using loops. The first two grids were made by Hayley and Ashley coded the final grid. Paloma worked on the score board display and had
# to research how to use pygames to display figures, and numbers that could be updated. This also made good use of global variables.

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

#these bounds were created by Ashley in an attempt to have the shapes recognize when they have fallen too far. It took around 1.5 hours to have it working 
# with the rest of the code.
def drawBounds():

    pg.draw.rect(_VARS['surf'], [255,0,255], b1)
    pg.draw.rect(_VARS['surf'], [255,0,255], b2)
    pg.draw.rect(_VARS['surf'], [255,0,255], b3)
    pg.draw.rect(_VARS['surf'], [255,0,255], b4)
    pg.draw.rect(_VARS['surf'], [255,0,0], lilguy)

# the Squarefall method was tricky because it started out just moving a single square, but the group had to transition it to make a set of squares that 
# combine to form a full piece. It was tricky to brainstorm how to get the individual squares to all move as a unit, we had to research was to reference them
# in a way that could be updated. The group did research on this and Ashley spent an additional 10 hours doing trial and error on this function from start to finish. 
def squareFall():
    global canfall, s1,s2,s3,s4,scolor
    global current_score

#this function checks if the piece has collided with the boundaries, signaling that a new piece should be generated. It also adds the score which is a function that
# Paloma worked to get functioning properly. 
    if s3.colliderect(b1) :
            pg.draw.rect(_VARS['surf'], scolor, s1)
            pg.draw.rect(_VARS['surf'], scolor, s2)
            pg.draw.rect(_VARS['surf'], scolor, s3)
            pg.draw.rect(_VARS['surf'], scolor, s4)
            canfall = False
            current_score +=1


    else:
#this function allows the piece to move down as a unit.
        v = [0, 25]
        s1.move_ip(v)
        pg.draw.rect(_VARS['surf'], scolor, s1)
        s2.move_ip(v)
        pg.draw.rect(_VARS['surf'], scolor, s2)
        s3.move_ip(v)
        pg.draw.rect(_VARS['surf'], scolor, s3)
        s4.move_ip(v)
        pg.draw.rect(_VARS['surf'], scolor, s4)
#the following code is similar to above, just added to make the game more interesting and adjusted. 
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

#this function allows the small red square ton move around the screen. Ashley did research and trial and error to add this. It started as a function that 
#could move the pieces as they fell in tetris, but once we switched games, it changed to move the red square around the pieces. 
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

#As a planB, we came up with a option to change our game from tetris to dodge the block. As part of that plan, we created this function that makes the player
#lose the game if the red block collides with the falling pieces. This function was written by Ashley to shut off the game. Unfortunately, this came after many 
#hours of trying to figure out how to implement all of the functions of tetris.
def gameover():
    global canfalla, a1,a2,a3,a4
    global canfall, s1,s2,s3,s4
    if lilguy.colliderect(a1) or lilguy.colliderect(a2) or lilguy.colliderect(a3) or lilguy.colliderect(a4)  or lilguy.colliderect(s1) or lilguy.colliderect(s2)  or lilguy.colliderect(s3)  or lilguy.colliderect(s4):
        sys.exit()

# Hayley created a function that terminates the code in response to a keypress. 
def checkEvents():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

            
#This start screen was written by Hayley and took a lot of trial and error to format and also allow it to switch to the correct screen once the keys have been
#pressed. 

# Function for instructions screen:
def start_screen():
    run = True
    while run:
        Screen.fill((0,0,0))
        font2 = pg.font.SysFont('freesansbold.ttf', 26)
        # Write Text: 
        dodge_text = font.render("Dodge the blocks!", True, WHITE)
        how2play_text = font.render("HOW TO PLAY:", True, RED)
        instructions1_text = font2.render("Blocks will fall from the top of the grid. Using the arrows on your", True, WHITE)
        instructions2_text = font2.render("your keyboard, you can move the red square left, right, up, and ", True, WHITE)
        instructions3_text = font2.render("down.The objective is to dodge the falling blocks. When you", True, WHITE)
        instructions4_text = font2.render("succesfully dodge the falling blocks, you will be rewarded points.", True, WHITE)
        instructions5_text = font2.render("If the blocks and red square collide, the game will be terminated.", True, WHITE)
        start_text = font.render("Press any key to start.", True, RED)
        # Draw text to screen: 
        Screen.blit(dodge_text, (160, 25))
        Screen.blit(how2play_text, (180, 150))
        Screen.blit(instructions1_text, (36,210))
        Screen.blit(instructions2_text, (34, 235))
        Screen.blit(instructions3_text, (35, 260))
        Screen.blit(instructions4_text, (28,285))
        Screen.blit(instructions5_text, (33,310))
        Screen.blit(start_text, (135, 400))
        pg.display.update()
        # Change to game screen if key pressed: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                main()

    pg.quit()

Screen = pg.display.set_mode((600,600))
pg.display.set_caption('Dodge the blocks')

start_screen() # Start game 
