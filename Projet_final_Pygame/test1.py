import pygame
from pygame.locals import *
from combobox import chaine

import EMPLACEMENTOFF


pygame.init()
win=pygame.display.set_mode((640,480),RESIZABLE)
pygame.display.set_caption("urturn")
fond=pygame.image.load("backgoundprimalbad1.jpg")
win.blit(fond,(0,0))
pygame.display.flip()
font = pygame.font.SysFont("comicsansms", 30)
if chaine=="1 Joueur":
 from button_text1 import var
 text = font.render(var, True, (0, 0, 255))
 win.blit(text,(0,0))
 pygame.display.flip()
if chaine=="2 Joueur":
 from button_text2 import var1,var2
 text = font.render(var1, True, (0, 0, 255))
 win.blit(text,(0,0))
 text = font.render(var2, True, (0, 0, 255))
 win.blit(text,(530,0))
 pygame.display.flip()
if chaine=="3 Joueur":
 from button_text3 import var1,var2,var3
 text = font.render(var1, True, (0, 0, 255))
 win.blit(text,(0,0))
 text = font.render(var2, True, (0, 0, 255))
 win.blit(text,(530,0))
 pygame.display.flip()
 text = font.render(var3, True, (0, 255, 0))
 win.blit(text,(0,420))
 pygame.display.flip()
if chaine=="4 Joueur":
 from button_text4 import var1,var2,var3,var4
 text = font.render(var1, True, (0, 0, 255))
 win.blit(text,(0,0))
 text = font.render(var2, True, (0, 0, 255))
 win.blit(text,(530,0))
 pygame.display.flip()
 text = font.render(var3, True, (0, 255, 0))
 win.blit(text,(0,420))
 pygame.display.flip()
 text = font.render(var4, True, (255, 0, 0))
 win.blit(text,(530,420))
 pygame.display.flip()
 



continuer = 1
 
while continuer:
 
 
  for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
 
    
 
pygame.quit()
