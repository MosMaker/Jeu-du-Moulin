from fltk import *
from constante import l, h
from jeu import placer_cercles, deplacer_cercles
from affichage import choix_nombre_pions


#programme principal
if __name__ =='__main__':
    n = choix_nombre_pions()
    cree_fenetre(l,h)
    placer_cercles(n)
    deplacer_cercles()
    ferme_fenetre() 