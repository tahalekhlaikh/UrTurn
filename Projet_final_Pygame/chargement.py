import pygame
import time
pygame.init()
fenetre=pygame.display.set_mode((640,480))
fond=pygame.image.load("CHARGEMENT1.png")
chargement=["CHARGEMENT1.png","CHARGEMENT2.png","CHARGEMENT3.png","CHARGEMENT4.png"]
fenetre.blit(fond,(0,0))
pygame.display.flip()
i=0
def clock():
    time.sleep(2)
continuer=1
while continuer:
    for i in range(0,len(chargement)):
        fond=pygame.image.load(chargement[i])
        clock()
        fenetre.blit(fond,(0,0))
        pygame.display.flip()
    clock()
    import test1
