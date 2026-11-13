## Processus

1 compréhension du code
2 réorganisation en classe (+ adaptation et personnalisation) et structure(fichier; main, objets, physique, affichage, ...)
objectif, morcifier un max le code afion d optimiser sa prise en main rapide pour le second groupe, l ensemble des objets sera organisé en class et sous class pour realisé facilement des implementations
le fichier init doit permmetre d initialiser la class parents, les sous class sont init par le main ou la selection dans le futur menu #TODO adapte fichir init
3 optimisation selon la matiere du cour  (decorateur, ...)
4 ajout de fonctionalite ***BONUS***

!!! retrouver les choix "d'architecture" non noté pour le compte rendu !!! 
!!! faire fausse phasse prépa !!!


## LUKA
# commit
1 screen + ecran ✅ => taille dynamique ❌ , ameliorer background ❌ 
    main.py

2 affichage perso + deplacement✅ => ...❌ 
    main.py, perso.py

3 allègement du main dans initialisation + reorganisation ✅  
=>reorganisé init.py (un fonction = une initialisatione ???) ❌ 
    main.py,init.py

4 affichage ennemi ✅ => ajoute la boucle "spawn ennemi" + déplacment ✅ 

5 collision balle / ennemi ❌ 

**
"=>" signifie "à implémenter"
**

# utilisation IA

- gerer la taille d un image avec pygame
- integrer proprment la vitesse d un joueur selon le vaisseau choisis (vx)
- petit beug 
    - enemyX = random.randrange(0, L_screen, 5) ,enemyY = int(H_screen * 0.1) plutot que enemyX, enemyY = random.randrange(0, L_screen, 5),int(H_screen * 0.1)
    - comment recuperer la liste bullets de la classe weapon dans le main => utiliser l instance pas la class

## ROMEO

1 bullet + tire ✅   

## TODO 
1) separer l'affichage du main
1) ranger assets
2) optimiser le code à l'aide de décorateur et autre matiere vue en cours
3) separer constante et variable 

## TODO ++
1) ajouter un barre de vie
2) permettre aux ennemi de tirer 
3) BONUS in game
4) obstacle
5) BOSS
6) niveau de jeux
7) ennemi different
8) barre de vie ennemi
9) arme différente
10) perso  différents
11) animation