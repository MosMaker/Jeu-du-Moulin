from fltk import *
from constante import pts
from etat_jeu import pions_orange, pions_bleu, moulins_orange, moulins_bleu
from utils import case_libre, nouveau_tour, moulins_actifs, coup_possible, case_joueur, effacer_pion, gagnant, chercher_numero, pixel_vers_case, case_dans_plateau
from affichage import dessin, dessiner_marqueur, ecran_victoire

def deplacer_pion_orange(depart,arrivee):
    """exemple :
    orange = [(0,0),(6,0),(4,4)]
    on veut deplacer (0,0) en (3,0)
    i = chercher le numero de (0,0) dans la liste orange
    orange[i] = (3,0)
    orange[0] = (3,0) 
    """
    i = chercher_numero(pions_orange,depart)
    pions_orange[i] = arrivee
    
    
def deplacer_piont_bleu(depart,arrivee):
    """
    Permet de deplacer un pions bleu si cela est possible
    """
    i = chercher_numero(pions_bleu,depart)
    pions_bleu[i] = arrivee
    
 
#==========PLACEMENT DES PIONS==============#

def placer_cercles(n):
    """
    Permet de placer les pions chacun son tour
    """
    piont_a = n // 2
    piont_b = n // 2
    tour = 0
    phase = 'placement'

    while piont_a > 0 or piont_b > 0:
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == "ClicGauche":
            x = abscisse(ev)
            y = ordonnee(ev)
            i,j = pixel_vers_case(x, y)

            if not case_dans_plateau(i, j) or not pts[i][j]:
                continue

            if phase == 'placement':
                if case_libre(i, j):
                    if tour == 0 and piont_a > 0:
                        pions_orange.append((i, j))
                        piont_a -= 1
                        if moulins_actifs(pions_orange, moulins_orange):
                            phase = 'supression'
                        else:
                            tour = nouveau_tour(tour)
                        
                    elif tour == 1 and piont_b > 0:
                        pions_bleu.append((i, j))
                        piont_b -= 1
                        if moulins_actifs(pions_bleu, moulins_bleu):
                            phase = 'supression'
                        else:
                            tour = nouveau_tour(tour)
                
            elif phase == 'supression':
                if tour == 0 and (i, j) in pions_bleu:
                    effacer_pion(i, j, pions_bleu)
                    phase = 'placement'
                    tour = nouveau_tour(tour)

                elif tour == 1 and (i, j) in pions_orange:
                    effacer_pion(i, j, pions_orange)
                    phase = 'placement'
                    tour = nouveau_tour(tour)

        efface_tout()
        dessin(tour, phase)
        mise_a_jour()

    attend_ev()
    gagnant_jeu = gagnant()
    if gagnant_jeu is not None:
        ecran_victoire(gagnant_jeu)
        return



#=================DEPLACEMENT DES PIONS================#

        
def deplacer_cercles():
    """
    Permet de deplacer les pions chacun son tour une fois tous placer 
    """
    c  = None
    tour = 0
    phase = 'selection' # l'autre phase = deplacement
    while True :
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == "ClicGauche":
            x,y = abscisse(ev),ordonnee(ev)
            i,j = pixel_vers_case(x, y)

            if not case_dans_plateau(i,j) or not pts[i][j]:
                continue
            if tour == 0:
                couleur = 'orange'
            else:   
                couleur = 'bleu'
            
            if phase == 'selection':
                if case_joueur(i, j, couleur):
                    c = (i,j)
                    if (tour == 0 and len(pions_orange) <= 3) or (tour == 1 and len(pions_bleu) <= 3):
                        phase = 'vol'
                    else:
                        phase = 'deplacement'
            
            elif phase == 'deplacement' or phase == 'vol':
                if case_joueur(i, j, couleur):
                    c = (i, j)
                elif case_libre(i,j):
                    if coup_possible(c, (i, j)) or phase == 'vol':
                        if tour == 0:
                            deplacer_pion_orange(c, (i,j))
                            if moulins_actifs(pions_orange, moulins_orange):
                                phase = 'supression'
                            else:
                                tour = nouveau_tour(tour)
                                phase = 'selection'
                        else:
                            deplacer_piont_bleu(c, (i,j))
                            if moulins_actifs(pions_bleu, moulins_bleu):
                                phase = 'supression'
                            else:
                                tour = nouveau_tour(tour)
                                phase = 'selection'
                                                

            elif phase == 'supression':
                if tour == 0 and (i, j) in pions_bleu:
                    effacer_pion(i, j, pions_bleu)

                    gagnant_jeu = gagnant()
                    if gagnant_jeu is not None:
                        ecran_victoire(gagnant_jeu)
                        return

                    tour = nouveau_tour(tour)
                    phase = 'selection'

                elif tour == 1 and (i, j) in pions_orange:
                    effacer_pion(i, j, pions_orange)

                    gagnant_jeu = gagnant()
                    if gagnant_jeu is not None:
                        ecran_victoire(gagnant_jeu)
                        return

                    tour = nouveau_tour(tour)
                    phase = 'selection'

        efface_tout()
        dessin(tour, phase)
        if c is not None and (phase == "deplacement" or phase == "vol"):
            dessiner_marqueur(c)
           
        mise_a_jour()
        


    
