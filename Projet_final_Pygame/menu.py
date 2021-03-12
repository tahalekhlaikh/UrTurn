import pygame

from pygame.locals import *
pygame.init()

win=pygame.display.set_mode((500,454),RESIZABLE)


pygame.display.set_caption("urturn")
fond=pygame.image.load("urturn_menu.jpeg")
win.blit(fond,(0,0))
pygame.display.flip()
         
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('bold', 30)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text,(self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
    
    def redrawWindow():
       
        whitebutton1.draw(win)
        whitebutton2.draw(win)
        whitebutton3.draw(win)
        whitebutton4.draw(win)
run = True
whitebutton1 = button((255,255,255),130,50,154,63,'jouer')
whitebutton2= button((255,255,255),130,150,154,63,'options')
whitebutton3= button((255,255,255),130,250,154,59,'Régle du jeu')
whitebutton4= button((255,255,255),130,350,154,55,'quitter')

pygame.display.flip()
while run: 

 btn_jouer=pygame.image.load("btn_jouer.png")
 btn_options=pygame.image.load("btn_options.png")
 btn_regles=pygame.image.load("btn_regles.png")
 btn_quitter=pygame.image.load("btn_quitter.png")
 
 

 win.blit(btn_jouer,(130,50))
 win.blit(btn_options,(130,150))
 win.blit(btn_regles,(130,250))
 win.blit(btn_quitter,(130,350))
 pygame.display.update()
 pos=pygame.mouse.get_pos()
 for event in pygame.event.get():
  if event.type == pygame.MOUSEBUTTONDOWN:
      if whitebutton1.isOver(pos):
           
           pygame.quit()
           
           import chargement.py
           
           break
           
      if whitebutton4.isOver(pos):
           print("click sur quit")
           run=False
           pygame.quit()
           quit()
      if whitebutton3.isOver(pos):
        print("click sur regles")
        
        import click_regles
        
        
        
        
    
     
  if event.type==pygame.QUIT:
   run = False
   pygame.quit()
   quit()
     
    




