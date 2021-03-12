import pygame
pygame.init()
import random
from pygame.locals import*
import time
pygame.mixer.init()
import threading
from combobox import chaine



           
pygame.event.pump()
icon_32x32 =pygame.image.load("urturn_menu.jpeg")
pygame.display.set_icon(icon_32x32)
fenetre=pygame.display.set_mode((640,480))
fond=pygame.image.load("foret.jpg")
perso = pygame.image.load("BACKGROUNDOFF.png").convert_alpha()
perso1=pygame.image.load("dee.png").convert_alpha()
de=["dee.png","dee1.png","dee2.png","dee3.png","dee4.png","dee5.png","dee6.png"]
pion=["pionbleuofficiel.png","pionjauneofficiel.png","pionvertofficiel.png","pionrougeofficiel.png"]
fenetre.blit(fond,(0,0))
pygame.display.flip()
fenetre.blit(perso,(0,0))
pygame.display.flip()
i=random.randint(1,4)
 #SONG_END = pygame.USEREVENT + 1
 #pygame.mixer.music.set_endevent(SONG_END)
 #pygame.mixer.music.load("Undertale.mp3")
 #pygame.mixer.music.play(-1)
font = pygame.font.SysFont("comicsansms", 30)
text = font.render("0", True, (0, 0, 255))
fenetre.blit(text,(15,118))
text = font.render("0", True, (240, 195, 0))
fenetre.blit(text,(540,113))
text = font.render("0", True, (0, 255, 0))
fenetre.blit(text,(14,440))
text = font.render("0", True, (255, 0, 0))
fenetre.blit(text,(540,440))
if chaine=="1 Joueur":
  from button_text1 import var
  text = font.render(var, True, (0, 0, 255))
  fenetre.blit(text,(0,0))
  pygame.display.flip()
if chaine=="2 Joueur":
 from button_text2 import var1,var2
 text = font.render(var1, True, (0, 0, 255))
 fenetre.blit(text,(0,0))
 text = font.render(var2, True, (240, 195, 0))
 fenetre.blit(text,(500,20))
 pygame.display.flip()
if chaine=="3 Joueur":
 from button_text3 import var1,var2,var3
 text = font.render(var1, True, (0, 0, 255))
 fenetre.blit(text,(0,0))
 text = font.render(var2, True, (240, 195, 0))
 fenetre.blit(text,(530,0))
 pygame.display.flip()
 text = font.render(var3, True, (0, 255, 0))
 fenetre.blit(text,(140,420))
 pygame.display.flip()
if chaine=="4 Joueur":
 from button_text4 import var1,var2,var3,var4
 text = font.render(var1, True, (0, 0, 255))
 fenetre.blit(text,(0,0))
 text = font.render(var2, True, (240, 195, 0))
 fenetre.blit(text,(530,0))
 pygame.display.flip()
 text = font.render(var3, True, (0, 255, 0))
 fenetre.blit(text,(140,420))
 pygame.display.flip()
 text = font.render(var4, True, (255, 0, 0))
 fenetre.blit(text,(530,410))
 pygame.display.flip()
 

def Dice_Roll():
    pygame.mixer.music.load("Dice_Roll.mp3")
    pygame.mixer.music.play(0)
T=[]
B=[(149, 110), (190, 108), (228, 108), (267, 108), (304, 108), (341, 109), (379, 109), (406, 137)]
J=[(441, 156), (447, 190), (447, 225), (446, 260), (448, 292), (448, 327), (433, 349), (406, 369)]
R=[(378, 396), (340, 395), (301, 395), (260, 395), (223, 395), (185, 393), (148, 384), (111, 361)]
V=[(73, 344), (68, 317), (64, 282), (68, 249), (63, 216), (70, 179), (94, 156), (130, 141)]
BB=[(149, 110), (190, 108), (228, 108), (267, 108), (304, 108), (341, 109), (379, 109), (406, 137),(441, 156), (447, 190), (447, 225), (446, 260), (448, 292), (448, 327), (433, 349), (406, 369),(378, 396), (340, 395), (301, 395), (260, 395),(223, 395),(185, 393),(148, 384), (111, 361),(73, 344), (68, 317), (64, 282), (68, 249), (63, 216), (70, 179), (94, 156), (130, 141)]
JJ=[(441, 156), (447, 190), (447, 225), (446, 260), (448, 292), (448, 327), (433, 349), (406, 369),(378, 396), (340, 395), (301, 395), (260, 395), (223, 395), (185, 393), (148, 384), (111, 361),(73, 344), (68, 317), (64, 282), (68, 249), (63, 216), (70, 179), (94, 156), (130, 141),(149, 110), (190, 108), (228, 108), (267, 108), (304, 108), (341, 109), (379, 109), (406, 137)]
RR=[(378, 396), (340, 395), (301, 395), (260, 395), (223, 395), (185, 393), (148, 384), (111, 361),(73, 344), (68, 317), (64, 282), (68, 249), (63, 216), (70, 179), (94, 156), (130, 141),(149, 110), (190, 108), (228, 108), (267, 108), (304, 108), (341, 109), (379, 109), (406, 137),(441, 156), (447, 190), (447, 225), (446, 260), (448, 292), (448, 327), (433, 349), (406, 369)]
continuer=1
num_6 = pygame.image.load("dee6.png").convert() #pour les images transparantes 'convert_alpha()'
num_6.set_colorkey((255,255,255))

num_5 = pygame.image.load("dee5.png").convert() #pour les images transparantes 'convert_alpha()'
num_5.set_colorkey((255,255,255))

                   
num_4 = pygame.image.load("dee4.png").convert() #pour les images transparantes 'convert_alpha()'
num_4.set_colorkey((255,255,255))

num_3 = pygame.image.load("dee3.png").convert() #pour les images transparantes 'convert_alpha()'
num_3.set_colorkey((255,255,255))

num_2 = pygame.image.load("dee2.png").convert() #pour les images transparantes 'convert_alpha()'
num_2.set_colorkey((255,255,255))

num_1 = pygame.image.load("dee1.png").convert() #pour les images transparantes 'convert_alpha()'
num_1.set_colorkey((255,255,255))

num_0= pygame.image.load("dee.png").convert() #pour les images transparantes 'convert_alpha()'
num_0.set_colorkey((255,255,255))

num = [0,num_1,num_2,num_3,num_4,num_5,num_6]
BHOME=[(46,61),(100,61),(47,108),(100,108)]
VHOME=[(39,394),(92,392),(45,444),(92,444)]
JHOME=[(433,61),(478,60),(432,108),(478,109)]
RHOME=[(437,388),(480,387),(441,445),(479,445)]

VV=[(73, 344), (68, 317), (64, 282), (68, 249), (63, 216), (70, 179), (94, 156), (130, 141),(149, 110), (190, 108), (228, 108), (267, 108), (304, 108), (341, 109), (379, 109), (406, 137),(441, 156), (447, 190), (447, 225), (446, 260), (448, 292), (448, 327), (433, 349), (406, 369),(378, 396), (340, 395), (301, 395), (260, 395), (223, 395), (185, 393), (148, 384), (111, 361)]
def joueur_tour(i):
    if i%4 == 0 :
        tour=pygame.image.load("TourBleu.png").convert_alpha()
        fenetre.blit(tour,(158,51))
    if i%4 == 1 :
        tour=pygame.image.load("TourJaune.png").convert_alpha()
        fenetre.blit(tour,(158,51))
    if i%4 == 2 :
        tour=pygame.image.load("TourVert.png").convert_alpha()
        fenetre.blit(tour,(158,51))
    if i%4 == 3 :
        tour=pygame.image.load("TourRouge.png").convert_alpha()
        fenetre.blit(tour,(158,51))
        
def tourDeRole(i): #pour donner un tour de role à chacun !! 
    if i%4 == 0 :
        return "Bleu"
    if i%4 == 1 :
        return "Jaune"
    if i%4 == 2 :
        return "Vert"
    if i%4 == 3 :
        return "Rouge"
k=0#à chaque fois on incremente de 1 pou faire passer le tour au joueur suivant
def affichage_de(j):
    fenetre.blit(num[j],(530,200))
def de():
    time.sleep(0.5)
    i=random.randint(1,6)
    print(i)
    fenetre.blit(num[i],(530,200))
    pygame.display.flip() 
    return(i)
def init_pion(b,r,j,v):
    k=4
    for t in range(0,4):
        perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
        fenetre.blit(perso2,JHOME[t])
        perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
        fenetre.blit(perso2,VHOME[t])
        perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
        fenetre.blit(perso2,RHOME[t])
        perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
        fenetre.blit(perso2,BHOME[t])
def est_home(Roi):
    print(0)
l=0
b=0
bb=1#permet de changer de position et la memoriser
r=0
rr=1
j=0
jj=1
v=0
vv=1
k=0
#les v designent si un pion est sur le terrain ou pas#
#les vv desiqnent l'emplacement du pion#
joueur_tour(l)
while continuer==1:
    init_pion(b,r,j,v)
    joueur_tour(l+1)
    #print(Roi)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            print(pos)
            T.append(pos)
            #print(T)
        if event.type == QUIT :
            continuer = 0
        if event.type == MOUSEBUTTONUP:
            init_pion(b,r,j,v)
            if event.pos[0]< 632 and event.pos[0]>531 and event.pos[1]>309 and event.pos[1]<338:#appuyer sur le bouton pour lancer le dé#
                Dice_Roll()
                time.sleep(2)
                k=de()
                affichage_de(k)
                init_pion(b,r,j,v)
                Roi=tourDeRole(l)
                print(Roi)
                if(k==6):
                    if(b==0 and Roi=="Bleu"and l%4==0) :
                        affichage_de(k)
                        perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                        fenetre.blit(perso2,BB[0])
                        if(v==1):
                            perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                            fenetre.blit(perso2,VV[vv])
                        if(r==1):
                            perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                            fenetre.blit(perso2,RR[rr])
                        if(j==1):
                            perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                            fenetre.blit(perso2,JJ[jj])
                        pygame.display.flip()
                        b=b+1
                        bb=0
                        l=l+1
                        
                    elif(b==1 and Roi=="Bleu" and l%4==0 ):
                        l=l+1
                        bb+=k
                        for i in range(0,k):
                            fenetre.blit(perso,(0,0))
                            perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                            fenetre.blit(perso2,BB[bb-k+i+1])
                            if(v==1):
                                perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                                fenetre.blit(perso2,VV[vv])
                            if(r==1):
                                perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                                fenetre.blit(perso2,RR[rr])
                            if(j==1):
                                perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                                fenetre.blit(perso2,JJ[jj])
                            pygame.display.flip()
                            time.sleep(0.5)
                            pygame.display.flip()
                            init_pion(b,r,j,v)
                            affichage_de(k)

    #--------------------------------------------------------------------------------------------------------------#
                    elif(r==0 and Roi=="Rouge" and l%4==3):
                        affichage_de(k)
                        perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                        fenetre.blit(perso2,RR[0])
                        if(v==1):
                            perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                            fenetre.blit(perso2,VV[vv])
                        if(b==1):
                            perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                            fenetre.blit(perso2,BB[bb])
                        if(j==1):
                            perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                            fenetre.blit(perso2,JJ[jj])
                        pygame.display.flip()
                        r=r+1
                        rr=0
                        l=l+1
                        
                    elif(r==1 and Roi=="Rouge" and l%4==3):
                        rr+=k
                        l=l+1
                        for i in range(0,k):
                            fenetre.blit(perso,(0,0))
                            perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                            fenetre.blit(perso2,RR[rr-k+i+1])
                            if(v==1):
                                perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                                fenetre.blit(perso2,VV[vv])
                            if(b==1):
                                perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                                fenetre.blit(perso2,BB[bb])
                            if(j==1):
                                perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                                fenetre.blit(perso2,JJ[jj])
                            time.sleep(0.5)
                            pygame.display.flip()
                            init_pion(b,r,j,v)
    #----------------------------------------------------------------------------------------------------------------#
                    elif(v==0 and Roi=="Vert" and l%4==2):
                        affichage_de(k)
                        perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                        fenetre.blit(perso2,VV[0])
                        if(b==1):
                            perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                            fenetre.blit(perso2,BB[bb])
                        if(r==1):
                            perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                            fenetre.blit(perso2,RR[rr])
                        if(j==1):
                            perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                            fenetre.blit(perso2,JJ[jj])
                        pygame.display.flip()
                        v=v+1
                        vv=0
                        l=l+1
                    elif(v==1 and Roi=="Vert" and l%4==2):
                        vv+=k
                        affichage_de(k)
                        init_pion(b,r,j,v)
                        for i in range(0,k):
                            fenetre.blit(perso,(0,0))
                            perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                            fenetre.blit(perso2,VV[vv-k+i+1])
                            if(b==1):
                                perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                                fenetre.blit(perso2,BB[bb])
                            if(r==1):
                                perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                                fenetre.blit(perso2,RR[rr])
                            if(j==1):
                                perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                                fenetre.blit(perso2,JJ[jj])
                            time.sleep(0.5)
                            pygame.display.flip()
                            init_pion(b,r,j,v)
                            affichage_de(k)
    #----------------------------------------------------------------------------------------------------------------#
                    elif(j==0 and Roi=="Jaune" and l%4==1):
                        affichage_de(k)
                        perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                        fenetre.blit(perso2,JJ[0])
                        if(v==1):
                            perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                            fenetre.blit(perso2,VV[vv])
                        if(r==1):
                            perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                            fenetre.blit(perso2,RR[rr])
                        if(b==1):
                            perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                            fenetre.blit(perso2,BB[bb])
                        pygame.display.flip()
                        j=j+1
                        jj=0
                        l=l+1
                    elif(j==1 and Roi=="Jaune" and l%4==1):
                        jj+=k
                        l=l+1
                        for i in range(0,k):
                            fenetre.blit(perso,(0,0))
                            perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                            fenetre.blit(perso2,JJ[jj-k+i+1])
                            if(v==1):
                                perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                                fenetre.blit(perso2,VV[vv])
                            if(r==1):
                                perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                                fenetre.blit(perso2,RR[rr])
                            if(b==1):
                                perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                                fenetre.blit(perso2,BB[bb])
                            time.sleep(0.5)
                            pygame.display.flip()
                            init_pion(b,r,j,v)
    #-------------------------------------------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------------#
                else:
                    if(b==0 and Roi=="Bleu"  and l%4==0 ):
                        l=l+1
                        affichage_de(k)
                        init_pion(b,r,j,v)
                        if(v==1):
                                perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                                fenetre.blit(perso2,VV[vv])
                        if(r==1):
                                perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                                fenetre.blit(perso2,RR[rr])
                        if(j==1):
                                perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                                fenetre.blit(perso2,JJ[jj])
                    elif(b==1 and Roi=="Bleu" and l%4==0 ):
                        bb+=k
                        l=l+1
                        for i in range(0,k):
                            affichage_de(k)
                            fenetre.blit(perso,(0,0))
                            perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                            fenetre.blit(perso2,BB[bb-k+i+1])
                            if(v==1):
                                perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                                fenetre.blit(perso2,VV[vv])
                            if(r==1):
                                perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                                fenetre.blit(perso2,RR[rr])
                            if(j==1):
                                perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                                fenetre.blit(perso2,JJ[jj])
                            time.sleep(0.5)
                            pygame.display.flip()
                            init_pion(b,r,j,v)
        #------------------------------------------------------------------------------------------------#
                    elif(r==0 and Roi=="Rouge" and l%4==3):
                        l=l+1
                        affichage_de(k)
                        init_pion(b,r,j,v)
                        if(v==1):
                            perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                            fenetre.blit(perso2,VV[vv])
                        if(b==1):
                            perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                            fenetre.blit(perso2,BB[bb])
                        if(j==1):
                            perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                            fenetre.blit(perso2,JJ[jj])
                    elif(r==1 and Roi=="Rouge" and l%4==3):
                        rr+=k
                        l=l+1
                        for i in range(0,k):
                            affichage_de(k)
                            fenetre.blit(perso,(0,0))
                            perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                            fenetre.blit(perso2,RR[rr-k+i+1])
                            if(v==1):
                                perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                                fenetre.blit(perso2,VV[vv])
                            if(b==1):
                                perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                                fenetre.blit(perso2,BB[bb])
                            if(j==1):
                                perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                                fenetre.blit(perso2,JJ[jj])
                            time.sleep(0.5)
                            pygame.display.flip()
                            init_pion(b,r,j,v)
        #-------------------------------------------------------------------------------------------------------#
                    elif(v==0 and Roi=="Vert" and l%4==2):
                        l=l+1
                        affichage_de(k)
                        init_pion(b,r,j,v)
                        if(b==1):
                            perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                            fenetre.blit(perso2,BB[bb])
                        if(r==1):
                            perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                            fenetre.blit(perso2,RR[rr])
                        if(j==1):
                            perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                            fenetre.blit(perso2,JJ[jj])
                    elif(v==1 and Roi=="Vert" and l%4==2):
                        vv+=k
                        l=l+1
                        for i in range(0,k):
                            affichage_de(k)
                            fenetre.blit(perso,(0,0))
                            perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                            fenetre.blit(perso2,VV[vv-k+i+1])
                            if(b==1):
                                perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                                fenetre.blit(perso2,BB[bb])
                            if(r==1):
                                perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                                fenetre.blit(perso2,RR[rr])
                            if(j==1):
                                perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                                fenetre.blit(perso2,JJ[jj])
                            time.sleep(0.5)
                            pygame.display.flip()
                            init_pion(b,r,j,v)
        #--------------------------------------------------------------------------------------------------------#
                    elif(j==0 and Roi=="Jaune" and l%4==1):
                        l=l+1
                        affichage_de(k)
                        init_pion(b,r,j,v)
                        if(v==1):
                            perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                            fenetre.blit(perso2,VV[vv])
                        if(r==1):
                            perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                            fenetre.blit(perso2,RR[rr])
                        if(b==1):
                            perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                            fenetre.blit(perso2,BB[bb])
                    elif(j==1 and Roi=="Jaune" and l%4==1):
                        jj+=k
                        l=l+1
                        for i in range(0,k):
                            affichage_de(k)
                            fenetre.blit(perso,(0,0))
                            perso2=pygame.image.load("pionjauneofficiel.png").convert_alpha()
                            fenetre.blit(perso2,JJ[jj-k+i+1])
                            if(v==1):
                                perso2=pygame.image.load("pionvertofficiel.png").convert_alpha()
                                fenetre.blit(perso2,VV[vv])
                            if(r==1):
                                perso2=pygame.image.load("pionrougeofficiel.png").convert_alpha()
                                fenetre.blit(perso2,RR[rr])
                            if(b==1):
                                perso2=pygame.image.load("pionbleuofficiel.png").convert_alpha()
                                fenetre.blit(perso2,BB[bb])
                            time.sleep(0.5)
                            pygame.display.flip()
                            init_pion(b,r,j,v)
            if event.pos[0]< 630 and event.pos[0]>595 and event.pos[1]>0 and event.pos[1]<34:
                        print(0)
                        import menu
                          

                
                    
#fct verification out of range
