# -*- coding: utf-8 -*-
"""tetris_game_screen

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lb_UAZQGy_NywECyywsyBL3x551kN7pu
"""

from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
from psychopy.hardware import keyboard

import csv
import numpy as np
import pandas as pd

# Size of window and pixels
full_scr = input('full screen? 1(yes) or 0 (no)')
if full_scr:
  win = win = visual.Window([1440,900], color='black', fullscr=0)
else:
  win = visual.Window([600,400], color='black', fullscr=0)

 # Text
intro_text = visual.TextStim(win,text="Let's play TETRIS!", pos = (0,350), color='orange', bold=True, font='New Century', units = 'pix')
intro_text.draw()

# Boxes
mybox1 = visual.Rect(win, pos=(-.3,0),lineColor='white', lineWidth=5, width=.5, height=1.2)
mybox2_text = visual.TextStim(win, pos =(-.3,0.2),text = 'Level', color='orange')
mybox2 = visual.Rect(win, pos=(0.3,0.2), lineColor='white', lineWidth=5, width=.5, height=0.2)
mybox3_text = visual.TextStim(win, pos=(0.3,0), text = 'Score', color = 'orange')
mybox3 = visual.Rect(win, pos=(0.3,0), lineColor='white', lineWidth=5, width=.5, height=0.2)
mybox4_text = visual.TextStim(win,pos=(0.3, -0.2),text='Lines', color='orange')
mybox4 = visual.Rect(win, pos=(0.3,-0.2), lineColor='white', lineWidth=5, width=.5, height=0.2)
mybox1.draw()
mybox2.draw()
mybox2_text.draw()
mybox3.draw()
mybox3_text.draw()
mybox4.draw()
mybox4_text.draw()
win.flip()
core.wait(5)
