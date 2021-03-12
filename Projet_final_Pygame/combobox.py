
from tkinter import *
import pygame
pygame.init()

w = Tk()
 
# création listbox
lbx = Listbox(w)
lbx.insert(0, "1 Joueur")
lbx.insert(1, "2 Joueur")
lbx.insert(2, "3 Joueur")
lbx.insert(3, "4 Joueur")
lbx.select_set(0)
lbx.grid(row=0, column=0)
 
# on crée une variable StringVar() pour stocker la
# valeur de l'item sélectionné
selected_item = StringVar()
chaine=str()
# fonction appelée avec le bouton
def updateLabel():
    line = lbx.curselection()[0]
    item = lbx.get(line)
    
    if item =="1 Joueur":
       w.destroy()
       global chaine
       chaine=item
       
       import button_text1
      
    if item =="2 Joueur":
     w.destroy()
     chaine=item
     import button_text2
     
     

     
    if item =="3 Joueur":
      w.destroy()
      chaine=item
      import button_text3
    if item =="4 Joueur":
        
      w.destroy()
      chaine=item
      import button_text4
    
    # on affecte la valeur de l'item à la variable :
    selected_item.set(item)
   
 
# bouton
bt = Button(w, text="Confirmer", command=updateLabel)
bt.grid(row=1, column=0)

# label qui affiche l'item sélectionné
# on utilise une option textvariable pour
# le lier à l'objet StringVar qu'on a défini auparavant
lbl = Label(w, textvariable=selected_item)

lbl.grid(row=2,column=0)
print(chaine)

 
w.mainloop()
