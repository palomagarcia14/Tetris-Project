import psychopy
import random
from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
from psychopy.hardware import keyboard

import csv
import numpy as np
import pandas as pd

win = visual.Window([1000,700], color='black', fullscr=0)

#using a matrix to keep track of where fallen pieces are
#creates 15 lists (rows) of 10 elements each (all zeroes)
background_grid = [[(0, 0, 0) for i in range(10)] for i in range(15)]

#working on displaying the grid as an imahe
for i in range(len(background_grid)):
    for j in range(len(background_grid[i])):
        x_win_pos = -3#x value of space dependent on i, j, and window size
        y_win_pos = .5#y value of space dependent on i, j, and window size
        square = visual.Rect(win, pos=(x_win_pos, y_win_pos), lineColor="white", fillColor='gray', width=.1, height=.1)
            #width and height need to be adjusted here
        square.draw()
win.flip()
core.wait(5)


#need to include a while statement here that triggers this to repeat when a piece falls
piece_type = random.randint(1,8)
if piece_type == 1: #cyan straight horizontal line
    piece = visual #need to design piece (but don't draw on screen!)
elif piece_type == 2: #royal blue left L
    piece = visual
elif piece_type == 3: #orange right L
    piece = visual
elif piece_type == 4: #yellow square
    piece = visual
elif piece_type == 5: #green parallelogram-type shape
    piece = visual
elif piece_type == 6: #red parallelogram-type shape
    piece = visual
else: #purple T
    piece = visual
