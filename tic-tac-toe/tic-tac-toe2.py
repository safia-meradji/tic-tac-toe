from tkinter import *

##----- Définition des Variables globales -----##
cases = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
joueur = 1            # On commence par J1. J2 est associé au nombre -1
n = 1                 # Numéro du tour de jeu
somme = 0             # Somme des cases/numéro du joueur gagnant

##----- Définition des Fonctions -----##
def affichage_tk(tableau):
    """Cette fonction met à jour l'affichage graphique dans Tkinter."""
    dessin.delete("all")  # Effacer le canevas

    for i in range(3):
        for j in range(3):
            if tableau[i][j] == 1:
                dessin.create_text(j * 100 + 50, i * 100 + 50, text='X', font=('Helvetica', 50), fill='blue')
            elif tableau[i][j] == -1:
                dessin.create_text(j * 100 + 50, i * 100 + 50, text='O', font=('Helvetica', 50), fill='red')

def demande_tk(event):
    """Cette fonction gère les clics sur les cases du morpion."""
    global joueur, somme

    colonne = event.x // 100
    ligne = event.y // 100

    if cases[ligne][colonne] == 0 and somme == 0:
        cases[ligne][colonne] = joueur
        affichage_tk(cases)
        somme = verif_tk(cases)
        joueur = -joueur

    if somme != 0 or n == 9:
        # Réinitialiser le jeu si quelqu'un a gagné ou si c'est un match nul
        reset_jeu()
        
def affichage_tk(tableau):
    """Cette fonction met à jour l'affichage graphique dans Tkinter."""
    for i in range(3):
        for j in range(3):
            if tableau[i][j] == 1:
                dessin.create_text(j * 100 + 50, i * 100 + 50, text='X', font=('Helvetica', 50), fill='blue')
            elif tableau[i][j] == -1:
                dessin.create_text(j * 100 + 50, i * 100 + 50, text='O', font=('Helvetica', 50), fill='red')

def verif_tk(tableau):
    """Calcule des sommes de chaque ligne/colonne/diagonale pour vérifier l'alignement."""
    sommes = [sum(tableau[i]) for i in range(3)] + \
             [sum(tableau[i][j] for i in range(3)) for j in range(3)] + \
             [sum(tableau[i][i] for i in range(3))] + \
             [sum(tableau[i][2 - i] for i in range(3))]

    for s in sommes:
        if s == 3:
            print('Bravo Joueur 1 !')
            return 1
        elif s == -3:
            print('Bravo Joueur 2 !')
            return -1

    return 0

def reset_jeu():
    """Réinitialise le jeu en remettant toutes les cases à zéro."""
    global cases, joueur, n, somme
    cases = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    joueur = 1
    n = 1
    somme = 0
    dessin.delete("all")  # Effacer le canevas

##----- Programme principal -----##
fen = Tk()
fen.title('Morpion')

dessin = Canvas(fen, bg="white", width=303, height=303)
dessin.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

lignes = []
for i in range(4):
    lignes.append(dessin.create_line(0, 100 * i + 2, 303, 100 * i + 2, width=3))
    lignes.append(dessin.create_line(100 * i + 2, 0, 100 * i + 2, 303, width=3))

dessin.bind("<Button-1>", demande_tk)

fen.mainloop()
