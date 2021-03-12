import pygame
import random
from pygame.locals import *
from random import *
import time
from sys import exit
pygame.init()
fenetre = pygame.display.set_mode((640, 640))
fond=pygame.image.load("modebadr1.jpg")
def clock():
    time.sleep(2)
def convert():
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
continuer = 1
#while continuer:
    #for event in pygame.event.get():
        #i=randint(0,5)
        #clock
