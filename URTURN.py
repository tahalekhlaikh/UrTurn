import pygame
import time
import random
from math import *
from pygame.locals import *
from random import *
pygame.init()
pygame.mixer.init()
import threading
pygame.event.pump()
fenetre=pygame.display.set_mode((640,480))
fond=pygame.image.load("background.jpg")
perso = pygame.image.load("backgroundprimalbad1.png").convert_alpha()
perso1=pygame.image.load("de1.png").convert_alpha()
de=["de11.png","de2.png","de3.png"]
pion=["pionbleuofficiel.png","pionjauneofficiel.png","pionvertofficiel.png","pionrougeofficiel.png"]
fenetre.blit(fond,(0,0))
pygame.display.flip()
fenetre.blit(perso,(0,0))
perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
fenetre.blit(perso2,(0,0))
fenetre.blit(perso1,(530, 200))
fenetre.blit(perso2,(0, 200))
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load("Undertale.mp3")
pygame.mixer.music.play(-1)
pygame.display.flip()
#son=pygame.mixer.Sound("gamer.wav")
#son.play(-1)
fpsClock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
TpsZero = pygame.time.get_ticks() ## Départ
T=["C'est le tour du joueur rouge","C'est le tour du joueur bleu","C'est le tour du joueur jaune","c'est le tour du joueur vert"]
t=0
def reset_temps():
    seconds=0
def temps():
    seconds = (pygame.time.get_ticks() - TpsZero) / 1000
    return(seconds)
def clock():
    time.sleep(5)
def convert():
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
def timer(t):
    t=t+1
    time.sleep(1)
    return(t)
    
V=[(76, 346), (68, 317), (65, 283), (73, 250), (69, 215), (71, 182), (92, 160), (132, 140), (151, 117), (190, 110), (228, 113), (265, 110), (305, 112), (343, 111), (379, 110), (409, 139), (445, 157), (454, 192), (451, 224), (452, 255), (451, 293), (448, 327), (434, 353), (407, 371), (380, 397), (342, 397), (302, 397), (262, 399), (223, 399), (184, 400), (147, 386), (114, 361), (78, 344), (72, 317), (68, 280), (73, 251), (113, 247), (151, 248), (155, 284), (151, 319), (188, 319), (227, 319), (265, 329), (301, 321), (341, 318), (378, 318), (378, 282), (380, 252), (378, 218), (380, 180), (339, 185), (304, 187), (269, 184), (227, 185), (194, 184), (158, 176), (152, 217), (154, 250), (190, 251)]
J=[(441, 156), (448, 190), (448, 225), (448, 259), (450, 293), (447, 327), (435, 352), (407, 375), (381, 399), (343, 399), (304, 400), (260, 398), (221, 399), (184, 400), (147, 388), (113, 362), (73, 344), (71, 315), (64, 282), (72, 249), (67, 215), (71, 181), (96, 155), (133, 139), (153, 112), (191, 110), (228, 110), (266, 111), (305, 113), (342, 109), (380, 111), (406, 140), (445, 156), (449, 190), (451, 223), (451, 260), (416, 261), (378, 249), (378, 217), (378, 182), (342, 184), (306, 183), (266, 182), (229, 184), (191, 184), (153, 185), (153, 219), (153, 253), (151, 286), (151, 320), (185, 321), (224, 319), (262, 330), (297, 320), (338, 317), (374, 319), (376, 285), (374, 248), (335, 252)]  
R=[(379, 397), (340, 398), (303, 397), (261, 398), (223, 398), (186, 399), (148, 389), (112, 363), (76, 345), (72, 318), (66, 282), (70, 250), (65, 212), (74, 182), (95, 157), (133, 139), (157, 113), (193, 109), (229, 111), (269, 111), (305, 111), (341, 108), (382, 113), (411, 140), (444, 157), (455, 191), (450, 225), (451, 260), (451, 286), (452, 326), (436, 349), (407, 369), (383, 399), (344, 399), (309, 398), (265, 394), (265, 361), (266, 330), (302, 317), (337, 318), (377, 319), (377, 283), (378, 250), (378, 222), (379, 184), (343, 184), (306, 185), (270, 181), (230, 181), (195, 184), (156, 183), (154, 218), (154, 257), (152, 285), (152, 316), (190, 321), (223, 318), (265, 330), (264, 293)]
B=[(153, 111), (188, 111), (227, 111), (266, 111), (303, 111), (342, 111), (379, 111), (409, 138), (444, 157), (451, 187), (451, 221), (449, 257), (452, 289), (446, 325), (435, 351), (404, 371), (381, 399), (345, 397), (302, 397), (262, 398), (225, 398), (186, 397), (149, 389), (112, 364), (73, 345), (71, 316), (66, 282), (71, 249), (67, 214), (73, 182), (99, 156), (136, 139), (156, 110), (193, 110), (230, 111), (268, 109), (269, 147), (268, 181), (228, 181), (189, 181), (152, 182), (149, 218), (151, 252), (150, 284), (147, 316), (186, 319), (225, 317), (265, 326), (299, 316), (338, 316), (374, 318), (375, 283), (375, 248), (374, 214), (375, 180), (344, 181), (302, 181), (267, 180), (266, 214)]
continuer=True
while continuer:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            print(pos)

    while(t!=len(B)):
        i=randint(0,2)
        perso2=pygame.image.load(de[i]).convert_alpha()
        fenetre.blit(perso2,(530, 200))
        perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
        fenetre.blit(perso2,J[t])
        perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
        fenetre.blit(perso2,V[t])
        perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
        fenetre.blit(perso2,R[t])
        perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
        fenetre.blit(perso2,B[t])
        text=font.render(str(int(temps())), True, (255, 0, 255))
        fenetre.blit(text,(280,20))
        pygame.display.flip()
        fenetre.blit(perso,(0,0))
        fpsClock.tick(60)
        t=timer(t)
        
pygame.quit()
