import pygame
import time
import random
from pygame.locals import *


pygame.init()   #initialisation

fenetre = pygame.display.set_mode((640,480),RESIZABLE)  # ouvrir une fenetre "realisable" == mode RESIZABLE !! /"FULLSCREEN" 
#fond = pygame.image.load("background.jpg")
fond = pygame.image.load("background2.jpg").convert() #convertir l'image en qlq chose comprenable
fenetre.blit(fond,(0,0)) #coller l'image sur la fenetre !
#pygame.display.flip() #refraichir l'image
 
pion = pygame.image.load("cc.png").convert() #pour les images transparantes 'convert_alpha()'
pion.set_colorkey((255,255,255))
position_pion = pion.get_rect()
fenetre.blit(pion,(0,0))
##############################


fenetre.blit(fond,(0,0))
fenetre.blit(pion,position_pion)


######################################
############################################
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
##########################################################
###############################################################
  









#pygame.display.flip()#refraiche de l'écran

continuer = 1
pygame.key.set_repeat(400, 30)

while continuer:
  for event in pygame.event.get():
          
          if event.type == QUIT:
              continuer = 0
          if event.type == KEYDOWN:
              
              if event.key == K_DOWN:
                  position_pion = position_pion.move(0,3)
              if event.key == K_UP:
                  position_pion = position_pion.move(0,-3)
              if event.key == K_LEFT:
                  position_pion = position_pion.move(-3,0)
              if event.key == K_RIGHT:
                  position_pion = position_pion.move(3,0)
                  
           
            

          if event.type == MOUSEBUTTONDOWN and event.button == 1 :
           print(position_pion)

  
  
  #recollage
  fenetre.blit(fond,(0,0))
  fenetre.blit(pion,position_pion)
 
  #refraiche!
  pygame.display.flip()
    
    



##################################################################
  #############################construction de dé ########################
        
        
    
