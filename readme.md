# Jeu du Moulin simplifié
Version simplifiée du Jeu du Moulin développé en **Python** avec la bibliothèque graphique **FLTK**.  
Projet réalisé dans le cadre d’un apprentissage de la programmation et de la gestion d’événements.

---

## Fonctionnalités
- Plateau du Jeu du Moulin fidèle à l’original
- Placement des pions tour par tour
- Déplacement des pions avec connexions valides
- Mode **vol** lorsque le joueur n’a plus que 3 pions
- Détection des **moulins** -> 3 pions alignés
- Suppression d’un pion adverse après un moulin
- Affichage du **tour du joueur** et de la **phase de jeu**
- Écran de victoire en fin de partie

---

## Règles implémentées
- Un moulin est formé lorsque **3 pions sont alignés**
- Chaque moulin nouvellement formé permet de supprimer un pion adverse
- La partie se termine lorsqu’un joueur possède moins de 3 pions

---

## Structure du projet
```text
jeu-du-moulin/
│
├── main.py # Programme principal
├── jeu.py # Logique du jeu (placement, déplacement, suppression)
├── affichage.py # Affichage graphique (plateau, pions, textes)
├── utils.py # Fonctions utilitaires (moulins, déplacements, règles)
├── constante.py # Constantes du plateau (points, traits, moulins)
├── etat_jeu.py # État du jeu (listes de pions, moulins)
│
└── README.md
```

---

## Lancer le jeu
1. S’assurer d’avoir **Python 3**
2. Lancer le fichier principal :

```bash
python3 main.py
```

## Concepts utilisés
- Programmation événementielle
- Gestion d’état de jeu
- Séparation logique / affichage
- Structures de données (listes, tuples)
- Détection de configurations (moulins)


## Améliorations possibles (en cours de réalisation)
- Respect complet de la règle interdisant de supprimer un pion dans un moulin
- Animation des déplacements
- Ajout de plusieurs niveaux/plateaux
- Mode deux joueurs / Ordinateur

