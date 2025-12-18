from fltk import *
from constante import pts, traits, l, h
from etat_jeu import pions_orange, pions_bleu
from utils import case_en_pixel


def dessin_trait ():
    """
    Permet de dessiner le plateaux
    """
    for i in range (len(traits)):
        a = traits[i][0][0]
        b = traits[i][0][1]
        c = traits[i][1][0]
        d = traits[i][1][1]
    
        y = case_en_pixel(a,b)
        z = case_en_pixel(c,d)
        ligne(y[0],y[1],z[0],z[1])
    

def dessin_socle() :
    """
    Permet de dessiner les emplcements ou l'on placer les pions
    """
    for y in range(len(pts)):      
        for x in range(len(pts[0])): 
            if (pts[y][x] == True):
                a = (l)/(len(pts[0])+1)
                b = (h)/(len(pts)+1)
                cercle((x+1)*a, (y+1)*b, 10, remplissage = 'black')
    

def dessiner_marqueur(case):
    """
    Permet de savoir quel jetons nous avons selectionné
    """
    i,j = case
    cx,cy = case_en_pixel(i,j)
    cercle(cx,cy,25)

def dessin_pions():
    """
    Pemrmet de dessiner les pions
    """
    for i,j in pions_orange:
        cercle(*case_en_pixel(i,j), 16, remplissage='orange')
    for i,j in pions_bleu:
        cercle(*case_en_pixel(i,j), 16, remplissage='blue')
 

def choix_nombre_pions():
    """
    Permet de choisir le nombre de pions dans la fenêtre
    """
    cree_fenetre(l, h)

    while True:
        efface_tout()
        texte(l/2, h*0.1, "Choisissez le nombre de pions", ancrage='center', taille=18)

        rectangle(l/2 - 100, 100, l/2 + 100, 140)
        texte(l/2, 120, "8 pions", ancrage='center')

        rectangle(l/2 - 100, 160, l/2 + 100, 200)
        texte(l/2, 180, "12 pions", ancrage='center')

        rectangle(l/2 - 100, 220, l/2 + 100, 260)
        texte(l/2, 240, "16 pions", ancrage='center')

        mise_a_jour()

        ev = attend_ev()
        if type_ev(ev) == "ClicGauche":
            x, y = abscisse(ev), ordonnee(ev)

            if l/2 - 100 <= x <= l/2 + 100:
                if 100 <= y <= 140:
                    ferme_fenetre()
                    return 8
                elif 160 <= y <= 200:
                    ferme_fenetre()
                    return 12
                elif 220 <= y <= 260:
                    ferme_fenetre()
                    return 16


def ecran_victoire(gagnant):
    """
    Affiche l'écran de victoire dans une nouvelle fenêtre
    """
    ferme_fenetre()         
    cree_fenetre(l, h)    
    rectangle(0, 0, l, h, remplissage='white')
    texte(l/2, h/2,
          "Le joueur " + gagnant,
          ancrage='center',
          taille=20)
    mise_a_jour()
    attend_ev()              
    ferme_fenetre()

def dessin(tour = None, phase = None):
    """
    Fonction qui fait toute la partie graphique
    """
    dessin_trait ()
    dessin_socle()
    dessin_pions()

    if tour is not None and phase is not None:
        texte(100, 20,
              "Tour du joueur " + ("orange" if tour == 0 else "bleu") + " - Phase: " + phase,
              ancrage='w',
              taille=16)