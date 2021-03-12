import pygame


pygame.init()
pygame.display.set_caption("urturn")

win1=pygame.display.set_mode((500,333))


fond=pygame.image.load("click_option.jpg")
win1.fill((0,0,255))
win1.blit(fond,(0,0))
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
            pygame.draw.rect(win1, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win1, self.color, (self.x, self.y, self.width, self.height), 0)

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
       
       
        whitebutton4.draw(win1)
    def recursive():
      
     
        import menu
run = True

whitebutton4= button((255,255,255),180,280,154,55,'retourner')
N=0
pygame.display.flip()
while run: 
 
 btn_retourner=pygame.image.load("btn_retourner.png")
 
 button.redrawWindow()

 win1.blit(btn_retourner,(178,280))
 pygame.display.flip()
 pygame.display.update()
 pos=pygame.mouse.get_pos()
 
 for event in pygame.event.get():
  if event.type == pygame.MOUSEBUTTONDOWN:

       if whitebutton4.isOver(pos):
         
         button.recursive()
      
           
         print("click sur retourner")
        
          
           
           
           
     
  if event.type==pygame.QUIT:
   run = False
   pygame.quit()
   quit()
     
    



