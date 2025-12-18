from etat_jeu import pions_orange, pions_bleu, moulins_orange, moulins_bleu
from constante import traits, moulin

def case_en_pixel(i,j):
    """
    Permet de convertir les case en pixel
    """
    x = (i*87 + 90)
    y = (j*87 + 90)
    return (x, y)

def pixel_vers_case(x, y):
    """
    Permet de convertir les pixel en case 
    """
    x += 43
    y += 43
    i = ((x-90) // 87)
    j = ((y-90) // 87)
    
    return (i,j) 

def case_dans_plateau(i,j):
    """
    Permet de verifier 
    """
    taille = 8
    if i >= taille :
        return False
    if i < 0 :
        return False
    if j >= taille :
        return False
    if j < 0 :
        return False
    
    return True
    

def case_libre(i,j):
    """
    permet de verifier si une case est libre
    """
    if (i,j) not in pions_orange :
        if (i,j) not in pions_bleu :
            return True
        else :
            return False    
    else :
        return False

def clic_case(i, j, tour, phase):
    """
    Gère un clic sur une case selon la phase et le joueur actif
    """
    if tour == 0:
        liste_joueur = pions_orange
        liste_adverse = pions_bleu
    else:
        liste_joueur = pions_bleu
        liste_adverse = pions_orange

    if phase == 'placement':
        if case_libre(i, j):
            liste_joueur.append((i,j))
            if moulins_actifs(liste_joueur, moulins_orange if tour == 0 else moulins_bleu):
                return True, 'supression'
            else:
                return True, 'placement'
        else:
            return False, phase
    elif phase == 'supression':
        if (i,j) in liste_adverse:
            effacer_pion(i,j,liste_adverse)
            return True, 'placement'
        else:
            return False, phase
    return False, phase


def nouveau_tour(tour):
    """
    Permet de savoir a qui est le tour
    """
    return 1 - tour
    
def case_joueur(i, j, couleur):
    """
    Permet de savoir si la case appartient au joueur Bleu ou Orange
    """
    if couleur == 'orange':
        if (i,j) in pions_orange:
            return True
    elif couleur == 'bleu':
        if (i,j) in pions_bleu:
            return True
    return False


def chercher_numero(liste,objet): #cette fonction existe deja pas besoin de la creer (fonction list.index) 
    for i in range(len(liste)):
        if liste[i] == objet :
            return i
    return -1


def coup_possible(debut,fin):
    """
    Permet de savoir si il y a une connexions entre 2 pions
    """
    for i in range(len(traits)):
        if debut == traits[i][0] and fin == traits[i][1]:
                return True
        if debut == traits[i][1] and fin == traits[i][0]:
                return True
    return False

def effacer_pion(i,j,liste):
    """
    Permet d'effacer le pions adverse apres la réalisation d'un moulin
    """
    liste.remove((i,j))

def gagnant():
    """
    Permet de savoir si un joueur a gagné
    """
    if len(pions_orange) < 3:
        return 'Bleu a gagné !'
    elif len(pions_bleu) < 3:
        return 'Orange a gagné !'
    else:
        return None
    

def moulins_actifs(liste_joueur, moulins_joueur):
    """
    Détecte si un NOUVEAU moulin vient d'être formé.
    """
    moulins_actuels = []

    for m in moulin:
        if all(p in liste_joueur for p in m):
            moulins_actuels.append(m)

    nouveaux = [m for m in moulins_actuels if m not in moulins_joueur]

    moulins_joueur.clear()
    moulins_joueur.extend(moulins_actuels)

    return len(nouveaux) > 0
