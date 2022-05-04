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


#maybe we should define each piece by the coordinates it will first fill
    #then we could just do math on the coordinates in response to the keypresses

#this function takes no input and randomly selects a type of tetris piece
    #it outputs the starting coordinates within the grid of all 4 squares and what color they should be
def piece_generator
    piece_type = random.randint(1,8)
    if piece_type == 1: #cyan straight horizontal line ("I")
        starting_position = [[0, 3], [0, 4], [0, 5], [0,6]] #starting coordinates of this piece
        color = [] #cyan
    elif piece_type == 2: #royal blue left L
        starting_position = [[1,4], [1,5], [1,6], [0,6]]
        color = [] #royal blue
    elif piece_type == 3: #orange right L
        starting_position = [[1,4], [1,5], [1,6], [0,4]]
        color = [] #orange
    elif piece_type == 4: #yellow square
        starting_position = [[0,4], [1,4], [0,5], [1,5]]
        color = [] #yellow
    elif piece_type == 5: #green parallelogram-type shape
        starting_position = [[1,4], [0,5], [1,5], [0,6]]
        color = [] #green
    elif piece_type == 6: #red parallelogram-type shape
        starting_position = [[0,4], [0,5], [1,5], [1,6]]
        color = [] #red
    elif piece_type == 7: #purple T
        starting_position = [[0,4], [0,5], [1,5], [0,6]]
        color = [] #purple
    return stating_position, color




#then for a given amount of time that passes, we can just adjust the coordinates on the piece within the grid
