# Hayley spent about 5 hours identifying different RGB code combinations, creating different blocks, and writing functions that were 
# an attempt to randomize the shapes, colors, and rotations of these blocks. 

import pygame
import random

# Colors
BLACK = (0,0,0)
PURPLE = (120, 37, 179)
AQUA = (100, 179, 179)
BROWN = (80, 34, 22)
GREEN = (80, 134, 22)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
GRAY = (220,220,220)

shape_colors = [PURPLE, AQUA, BROWN, GREEN, RED, ORANGE]

# Blocks & Rotations
class Shape:
    x = 0
    y = 0
    # Shape of blocks:
    Shapes = [
        [[1,2,5,6]], # O
        [[1,5,9,13], [4,5,6,7]], # I
        [[6,7,9,10], [1,5,6,10]], # S
        [[4,5,9,10], [2,6,5,9]], # Z
        [[1,2,6,10], [5,6,7,9], [2,6,10,11], [3,5,6,7]], # L
        [[1,2,5,9], [0,4,5,6], [1,5,9,8], [4,5,6,10]], # J
        [[1,4,5,6], [1,4,5,9], [4,5,6,9], [1,5,6,9]], # T
    ]
    # Random selection of block type and color:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.type = random.randint(0,len(self.Shapes)-1)
        self.color = random.randint(1,len(shape_colors)-1)
        self.rotation = 0
    # Current rotation of figure:
    def image(self):
        return self.Shapes[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.Shapes[self.type])

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")

def return_shapes():
    return Shape(Shapes)

return_shapes()
