import sys
import pygame
from pygame.locals import KEYDOWN, K_q

pygame.font.init()
# CONSTANTS:
X = 600
Y = 600
SCREENSIZE = X, Y
BLACK = (0, 0, 0)
WHITE = (255,255,255)
PADDING = PADTOPBOTTOM, PADLEFTRIGHT = 100,100

# Creating display surface object
display_surface = pygame.display.set_mode((X,Y))

# Name the window
pygame.display.set_caption('TETRIS')
screen=pygame.display.set_mode((X,Y))

# VARS:
_VARS = {'surface': False}


def main():
    pygame.init()
    _VARS['surface'] = pygame.display.set_mode(SCREENSIZE)
    while True:
        checkEvents()
        _VARS['surface'].fill(BLACK)
        drawGrid(15)
        font = pygame.font.SysFont('freesansbold.ttf', 48)
        tetris_text = font.render("Let's play Tetris!", True, WHITE)
        score_text = font.render ("Score: ", True, WHITE)
        screen.blit(tetris_text, (170, 25))
        screen.blit(score_text, (225, 530))
        pygame.display.update()


def drawGrid(divisions):
    # DRAW Rectangle
    # TOP lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surface'], WHITE,
      (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (X - PADLEFTRIGHT, 0 + PADTOPBOTTOM), 2)
    # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
      _VARS['surface'], WHITE,
      (0 + PADLEFTRIGHT, Y - PADTOPBOTTOM),
      (X - PADLEFTRIGHT, Y - PADTOPBOTTOM), 2)
    # LEFT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surface'], WHITE,
      (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (0 + PADLEFTRIGHT, Y - PADTOPBOTTOM), 2)
    # RIGHT TOP TO BOTTOM
    pygame.draw.line(
      _VARS['surface'], WHITE,
      (X - PADLEFTRIGHT, 0 + PADTOPBOTTOM),
      (X - PADLEFTRIGHT, Y - PADTOPBOTTOM), 2)

    # Get cell size
    horizontal_cellsize = (X - (PADLEFTRIGHT*2))/divisions
    vertical_cellsize = (Y - (PADTOPBOTTOM*2))/divisions

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(divisions):
        pygame.draw.line(
           _VARS['surface'], WHITE,
           (0 + PADLEFTRIGHT+(horizontal_cellsize*x), 0 + PADTOPBOTTOM),
           (0 + PADLEFTRIGHT+horizontal_cellsize*x, Y - PADTOPBOTTOM), 2)
    # HORITZONTAL DIVISION
        pygame.draw.line(
          _VARS['surface'], WHITE,
          (0 + PADLEFTRIGHT, 0 + PADTOPBOTTOM + (vertical_cellsize*x)),
          (X - PADLEFTRIGHT, 0 + PADTOPBOTTOM + (vertical_cellsize*x)), 2)

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    main()
