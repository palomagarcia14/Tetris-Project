# Hayley spent about 4 hours familiarzing herself with the pygame module and its keypress commands. This was more time consuming than
# expected because her keyboard was not reacting at all to the code. She had to go into her settings and change the access settings for her keyboard.
# This code was the group's first attempt to work with keypresses in pygame. 
# get out
# -*- coding: utf-8 -*-
"""tetris_keypress.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dIyqmVo4UMyDwkreT7DzV5lyl9FcBESu
"""
# Moving object when key is pressed
import pygame
import sys
pygame.init()
fps=30
fpsclock=pygame.time.Clock()
sur_obj=pygame.display.set_mode((400,300))
pygame.display.set_caption("Keyboard_Input")
Black=(0,0,0)
p1=10
p2=10
step=5
while True:
    sur_obj.fill(Black)
    pygame.draw.rect(sur_obj, (255,0,0), (p1, p2, 70, 65))
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        p1 -= step
    if key_input[pygame.K_RIGHT]:
        p1 += step
    if key_input[pygame.K_DOWN]:
        p2 += step
    pygame.display.update()
    fpsclock.tick(fps)
