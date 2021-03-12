import pygame
import time
import random
from random import *
from pygame.locals import *
from tkinter import *
pygame.init()
T=["de.jpg","de2.jpeg","de3.jpeg","de4.jpeg","de5.jpeg","de6.jpeg"]
fenetre = pygame.display.set_mode((640, 480))
fond=pygame.image.load("planche.jpg")
#font=pygame.font.Font(None,24)
#text = font.render("Texte",0,(255,0,0))
def clock():
    time.sleep(2)
def convert():
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
continuer = 1
while continuer:
    for event in pygame.event.get():
        i=randint(0,5)
        print(i)
        perso = pygame.image.load(T[i]).convert_alpha()
        fenetre.blit(perso,(0,0))
        pygame.display.flip()
        clock()
        convert()
 
pygame.quit()
