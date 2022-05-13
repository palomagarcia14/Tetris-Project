import sys
import pygame
from pygame.locals import *
import time
from pygame.locals import KEYDOWN, K_q

# Constants
X = 600
Y = 600
SCREENSIZE = X, Y
PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 100,100

# Color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

# Initialize pygame
pygame.init()

# Create screen
screen=pygame.display.set_mode((X,Y))

# Font
font = pygame.font.SysFont('freesansbold.ttf', 48)
font2 = pygame.font.SysFont('freesansbold.ttf', 27)
tetris_text = font.render("Let's play Tetris!", True, WHITE)
how2play_text = font.render("HOW TO PLAY:", True, RED)
instructions1_text = font2.render("Blocks will fall from the top of the grid. Using the arrows", True, WHITE)
instructions2_text = font2.render("on your keyboard, you can move the blocks around, either", True, WHITE)
instructions3_text = font2.render("left to right and/or you can rotate them. The objective is to", True, WHITE)
instructions4_text = font2.render("get all the blocks to fill all the empty spaces in a line. When", True, WHITE)
instructions5_text = font2.render("you do this, the blocks vanish and you will be rewarded points.", True, WHITE)
start_text = font.render("Press any key to start.", True, RED)

running = True
background = BLACK
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running = False

    screen.fill(background)
    screen.blit(tetris_text, (170, 25))
    screen.blit(how2play_text, (180, 125))
    screen.blit(instructions1_text, (35,175))
    screen.blit(instructions2_text, (30, 200))
    screen.blit(instructions3_text, (30, 225))
    screen.blit(instructions4_text, (30,250))
    screen.blit(instructions5_text, (30,275))
    screen.blit(start_text, (125, 400))

    pygame.display.update()

def intro_slide():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                screen.blit(tetris_text, (170,25))
                main()
    pygame.quit()

intro_slide() # Start game
