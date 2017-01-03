'''
VERSION 3.0 DU SNAKE
Thibault de SURREL
'''

from tkinter import *
from random import *
from tkinter.messagebox import *

def PommeBouger():
    #Positionnement aleatoire de la pomme
    global PosX,PosY,PosXPo,PosYPo,score,pomme
    PosXPo = randint(2,47)
    PosXPo = (PosXPo * 20)
    PosYPo = randint(2,31)
    PosYPo = (PosYPo * 20)
    pomme = Canevas.create_oval(PosXPo-r, PosYPo-r, PosXPo+r, PosYPo+r, outline = 'black', fill= 'red',tags ='pomme')


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
    #Verification du snake sur pomme
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
    global fin, score,nbDerreurs, fenetre, nomJou, Champ,texte3
    maFenetre.destroy()
    fin = 1


    fenetre = Tk()
    fenetre['bg'] = couleur
    fenetre.title("Perdu...")
    fenetre.geometry('300x400')
    texte = Label(fenetre, text='Vous avez perdu...',bg = couleur)
    texte.pack(pady = 10)
    texte2 = Label(fenetre, text='Votre score : '+str(score))
    texte2.pack()
    texte3 = Label(fenetre, text='Entrez votre nom : ')
    texte3.pack()
    nomJou = StringVar()
    Champ = Entry(fenetre, textvariable = nomJou)
    Champ.pack()
    fenetre.bind('<Key>', RecupNom)

def Highscore(nom):
    global fenetreFin, score

    FichierScores = open('TopScores.txt').readlines()
    FichierNoms = open('TopNoms.txt').readlines()
    TopScore1 = int(FichierScores[0])
    TopScore2 = int(FichierScores[1])
    TopScore3 = int(FichierScores[2])
    TopNom1 = FichierNoms[0]
    TopNom2 = FichierNoms[1]
    TopNom3 = FichierNoms[2]

    if score > int(TopScore1):
        TopScore3 = TopScore2
        TopNom3 = TopNom2
        TopScore2 = TopScore1
        TopNom2 = TopNom1
        TopScore1 = score
        TopNom1 = str(nom)+'\n'

    elif score > int(TopScore2):

        TopScore3 = TopScore2
        TopNom3 = TopNom2
        TopScore2 = score
        TopNom2 = str(nom)+'\n'

    elif score > int(TopScore3):

        TopScore3 = score
        TopNom3 = str(nom)+'\n'

    FichierScores = open('TopScores.txt','w')
    FichierScores.write(str(TopScore1)+'\n')
    FichierScores.write(str(TopScore2)+'\n')
    FichierScores.write(str(TopScore3)+'\n')
    FichierScores.close()

    FichierNoms = open('TopNoms.txt','w')
    FichierNoms.write(TopNom1)
    FichierNoms.write(TopNom2)
    FichierNoms.write(TopNom3)
    FichierNoms.close()
    AfficheHighScore()

def AfficheHighScore():
    global fin, fenetre
    if fin != 1:
        fenetre.destroy()
        fenetre = Tk()
        fenetre.title("Highscore")
        fenetre.geometry('300x400')
        fenetre['bg'] = couleur
    
    fin = 1        
    TopScores = open('TopScores.txt').readlines()
    TopNoms = open('TopNoms.txt').readlines()


    texte0 = Label(fenetre, text = 'Classement : ',bg = couleur)
    texte0.pack(pady = 20)
    texte1 = Label(fenetre,text = '1. ' + str(TopNoms[0]) + str(TopScores[0]) + '\n 2. ' + str(TopNoms[1]) + str(TopScores[1]) + '\n 3. ' + str(TopNoms[2]) + str(TopScores[2]),bg = couleur)

    texte1.pack(padx = 10, pady = 10)

    BoutonReJouer = Button(fenetre, text = "JOUER ?",  fg ='navy',command = Setup)
    BoutonReJouer.pack(pady = 10,padx = 10)
    BoutonMenu = Button(fenetre, text = "MENU",  fg ='navy',bg = couleur,command = Menu)
    BoutonMenu.pack(pady = 10,padx = 10)

def RecupNom(event):
    touche = event.keysym
    if touche == 'Return':
        nom = nomJou.get()
        Champ.destroy()
        texte3.destroy()
        Highscore(nom)

def SnakeBouger():
    #Deplacement du snake
    global PosX,PosY,PosXPo,PosYPo,score,pomme,snake,mouvement,taille,temps,fin,nbDerreurs
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
            aSuppr = Canevas.find_all()[-((score+1)*2)]
            tag = Canevas.gettags(aSuppr)
            if tag[0] == 'snake':
                Canevas.delete(aSuppr)
        except:
            pass



    if fin != 1:
        maFenetre.after(int(temps),SnakeBouger)

def Setup():
    #Declaration des variables
    global PosX,PosY,PosXPo,PosYPo,score,taille,temps,Canevas,r,mouvement,fin,nbDerreurs,maFenetre,scoreAff
    
    fenetre.destroy()
    #Creation de la fenetre
    maFenetre = Tk()
    maFenetre.title('Snake')

    
    score = 0
    PosX= 480
    PosXPo = 480
    PosY = 320
    r = 10
    mouvement = "none"
    taille = 1
    temps = 200
    fin = 0
    nbDerreurs = 0


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

def Menu():
    global fenetre, fin
    if fin:
        fenetre.destroy()
    fin = 0
    
    fenetre = Tk()
    fenetre.title("Menu")
    fenetre['bg'] = couleur
    fenetre.geometry('300x300')

    BoutonJouer = Button(fenetre, text = "JOUER !",  fg ='navy',bg = couleur,command = Setup)
    BoutonJouer.pack(pady = 10 , padx = 10)
    BoutonCommentJouer = Button(fenetre, text = "Comment jouer ?",  fg ='navy',bg = couleur,command = CommentJouer)
    BoutonCommentJouer.pack(pady = 10,padx = 10)
    BoutonCredits = Button(fenetre, text = "Credit",  fg ='navy',bg = couleur,command = Credits)
    BoutonCredits.pack(pady = 10,padx = 10)
    BoutonHighScore = Button(fenetre, text = 'Highscore', fg = 'navy',bg = couleur, command = AfficheHighScore)
    BoutonHighScore.pack(pady = 10,padx = 10)
    BoutonQuitter = Button(fenetre, text = "Quitter",  fg ='navy',bg = couleur,command = fenetre.destroy)
    BoutonQuitter.pack(pady = 10,padx = 10)
    fenetre.mainloop()

def CommentJouer():
    showinfo('Comment Jouer ?','Vous dirigez un serpent grace aux fleches du clavier.\n Vous devez manger les pommes pour grandir.\n Il ne faut pas passer sur sa queue sinon on a perdu :( \n Courage et bon jeu !  ')
def Credits():
    showinfo('Credits', 'Jeu cree par Thibault de Surrel \n\n\n 2016')

couleur = '#00f911'
fin = 0
Menu()


                                                                      

