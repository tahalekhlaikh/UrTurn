import pygame
import time
import random 
from pygame.locals import *

def de():
    time.sleep(0.5)

    i = random.randint(1,4)
    print(i)
    
    if(i==4):
        fenetre.blit(fond,(0,0))
        fenetre.blit(num_4,(303-201,399-132))
  
        
    if(i==3):
        fenetre.blit(fond,(0,0))
        fenetre.blit(num_3,(303-201,399-132))
       

    if(i==2):
        fenetre.blit(fond,(0,0))
        fenetre.blit(num_2,(303-201,399-132))
       

    return i



        
pygame.init()

fenetre = pygame.display.set_mode((640,480),RESIZABLE)
fond = pygame.image.load("background.jpg").convert()



###################################################
num_4 = pygame.image.load("4.png").convert() #pour les images transparantes 'convert_alpha()'
num_4.set_colorkey((255,255,255))
#position_num_4 = num_4.get_rect()


num_3 = pygame.image.load("3.png").convert() #pour les images transparantes 'convert_alpha()'
num_3.set_colorkey((255,255,255))
#position_num_3 = num_3.get_rect()



num_2 = pygame.image.load("2.png").convert() #pour les images transparantes 'convert_alpha()'
num_2.set_colorkey((255,255,255))
####################################################
pion = pygame.image.load("cc.png").convert()
pion.set_colorkey((255,255,255))
fenetre.blit(pion,(0,0))
position_pion = pion.get_rect() 

    


while(True):
    time.sleep(0.5)
    i = 0
    j= de()
    if(j==4):
        while(i < j):
            position_pion = position_pion.move(4,0)
            time.sleep(0.5)
            i += 1
    else:
        while(i < j):
            position_pion = position_pion.move(0,4)
            time.sleep(0.5)
            i += 1
        
        
    
        
        
        
        

    







#print( position_num_4)

###############################

#print( position_num_3)
#fenetre.blit(num_3,(303-201,399-132))
#############################################

#position_num_2 = num_2.get_rect()
#print( position_num_2)
#fenetre.blit(num_2,(303-201,399-132))
############################################


#pygame.display.flip()
