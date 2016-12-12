'''
VERSION 3.0 DU SNAKE
Thibault de SURREL
'''

from tkinter import *
from random import *

def PommeBouger():
    #Positionnement aléatoire de la pomme
    global PosX,PosY,PosXPo,PosYPo,score,pomme
    PosXPo = randint(1,48)
    PosXPo = (PosXPo * 20)
    PosYPo = randint(1,32)
    PosYPo = (PosYPo * 20)
    pomme = Canevas.create_rectangle(PosXPo-r, PosYPo-r, PosXPo+r, PosYPo+r, outline = 'black', fill= 'red',tags ='pomme') 
    

def Clavier(event):
    global PosX,PosY,PosXPo,PosYPo,score,pomme,snake,mouvement,taille
    touche = event.keysym
    #Detection des touches
    
    if touche == 'Up' and mouvement != 'down':
        mouvement = 'up'
    if touche == 'Down'and mouvement != 'up':
        mouvement = 'down'
    if touche == 'Right'  and mouvement != 'left':
        mouvement = 'right'
    if touche == 'Left'  and mouvement != 'right':
        mouvement = 'left'
    if taille == 1:
        Canevas.delete('snake1')
    


def TestPomme():
    #Vérification du snake sur pomme
    global PosX,PosY,PosXPo,PosYPo,score,pomme,snake,mouvement,temps
    if ((PosX+r > PosXPo-r) and (PosX-r < PosXPo+r)) and ((PosY+r > PosYPo-r) and (PosY-r < PosYPo+r)):
        score += 1
        scoreAff.set("Score : " + str(score))
        Canevas.delete(pomme)
        if temps > 55:
            temps = temps * 0.94
        PommeBouger()
    

def TestSnake():
    global PosX,PosY,PosXPo,PosYPo,score,pomme,snake,mouvement,temps, fin
    parDessus = Canevas.find_overlapping(PosX-(r-1), PosY+(r-1), PosX-(r-1), PosY+(r-1))
    if len(parDessus) > 1:
        Perdu()
        

                        
def Perdu():
    global fin, score
    maFenetre.destroy()
    fin = 1

    fenetreFin = Tk()
    fenetreFin.title("Perdu...")
    fenetreFin.geometry('300x100+800+450')
    texte = Label(fenetreFin, text='Vous avez perdu...')
    texte.pack(pady = 10)
    texte2 = Label(fenetreFin, text='Votre score : ')
    texte2.pack(side = LEFT, padx = 20)
    texteScore = Label(fenetreFin , text =str(score))
    texteScore.pack(side = RIGHT, padx = 75)
    
   

def SnakeBouger():
    #Deplacement du snake
    global PosX,PosY,PosXPo,PosYPo,score,pomme,snake,mouvement,taille,temps,fin
    if mouvement == 'up':
        PosY -= 20
        taille += 1
        Canevas.create_rectangle(PosX-r, PosY-r, PosX+r, PosY+r, outline = 'black', fill = 'green',tags ='snake')
    if mouvement == 'down':
        PosY += 20
        taille += 1
        Canevas.create_rectangle(PosX-r, PosY-r, PosX+r, PosY+r, outline = 'black', fill = 'green',tags = 'snake')
    if mouvement == 'right':
        PosX += 20
        taille += 1
        Canevas.create_rectangle(PosX-r, PosY-r, PosX+r, PosY+r, outline = 'black', fill = 'green',tags = 'snake')
    if mouvement == 'left':
        PosX -= 20
        taille += 1
        Canevas.create_rectangle(PosX-r, PosY-r, PosX+r, PosY+r, outline = 'black', fill = 'green',tags = 'snake')
    TestPomme()
    TestSnake()
    if PosX < 0 or PosY < 0 or PosX > 960  or PosY > 640:
        Perdu()
        
    #Suppretion de la fin du snake
    if taille > 2:
        try:
            aSuppr = Canevas.find_all()[-(score+1)*2]
            tag = Canevas.gettags(aSuppr)
            if tag[0] == 'snake':
                Canevas.delete(aSuppr)
        except:
            pass


    if fin != 1:
        maFenetre.after(int(temps),SnakeBouger)

    
#Creation de la fenetre
maFenetre = Tk()
maFenetre.title('Snake')

#Declaration des variables
global PosX,PosY,PosXPo,PosYPo,score,taille,temps
score = 0
PosX= 480
PosXPo = 480
PosY = 320
r = 10
mouvement = "none"
taille = 1
temps = 200
fin = 0

#Creation de la zone graphique 
Largeur = 955
Hauteur = 640

Canevas = Canvas(maFenetre, width= Largeur, height = Hauteur, bg= "white")
snake = Canevas.create_rectangle(PosX-r, PosY-r, PosX+r, PosY+r, outline = 'black', fill = 'green', tags = 'snake1')
scoreAff = StringVar()
scoreAff.set("Score : " +str(score))
LabelScore = Label(maFenetre, textvariable = scoreAff, fg='red', bg='white', anchor = S)
LabelScore.pack(padx = 5, pady= 5)

PommeBouger()
Canevas.focus_set()
Canevas.bind('<Key>', Clavier)
Canevas.pack(padx = 5, pady = 5)
SnakeBouger()


#Creation du boutton "Quitter"
Button(maFenetre, text = 'Quitter', command = maFenetre.destroy).pack(side=LEFT, padx = 5, pady= 5)

maFenetre.mainloop()
                                                                      

