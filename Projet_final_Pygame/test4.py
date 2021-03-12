import pygame
from pygame.locals import *

from button_text4 import var

import test1

pygame.init()
win=pygame.display.set_mode((640,480),RESIZABLE)
pygame.display.set_caption("urturn")
fond=pygame.image.load("background4.jpg")
win.blit(fond,(0,0))

 
font=pygame.font.SysFont("comicsansms",30)

text = font.render(var,1,(255,0,0))




continuer = 1
 
while continuer:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
 
    win.blit(text, (0, 0))
 
    pygame.display.flip()
 
pygame.quit()
