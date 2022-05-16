# Hayley wrote this code while exploring pygame and its text functions. She spent about an hour experimenting with colors and fonts
# and learning how to flip text to the screen in pygame. 
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

# Initialize pygame
pygame.init()

# Create screen
screen=pygame.display.set_mode((X,Y))

# Font
font = pygame.font.SysFont('freesansbold.ttf', 48)
tetris_text = font.render("Let's play Tetris!", True, WHITE)

running = True
background = BLACK
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running = False

    screen.fill(background)
    screen.blit(tetris_text, (170, 25))
    pygame.display.update()

pygame.quit()
