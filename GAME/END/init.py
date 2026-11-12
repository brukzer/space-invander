import pygame
from classes.player import Avion
from classes.ennemi import Extra

# TODO fenetre dynamique


def init_game():
    ### initialiser jeux ###
   
    pygame.init()
    L_screen, H_screen = 1280, 800  # TAILLE de la fenetre
   ### initialiser fenetre ###
    screen = pygame.display.set_mode((L_screen, H_screen))  # affichage fenetre
    # TODO changer les "background" apres chaque niveau
    back = pygame.image.load("GAME/assets/background.png")
    background = pygame.transform.scale(back, (L_screen, H_screen))  # IA

    ### Initialiser class Player.Avion ###
    # TODO Creer une selection d'avion
    playerImg = pygame.image.load("GAME/assets/player.png").convert_alpha()
    playerImg = pygame.transform.scale(playerImg, (150, 150))  # IA
    x, y = L_screen // 2, int(H_screen * 0.8)  # reprend la dimension d affichage pour afficher player  #?? trouver une meilleur methode
    # TODO adapté a la taille de 'player' afin d éviter les débordements
    limite_droite = int(L_screen) - 30  # limite_gauche = 0, implémenté ??
    joueur = Avion(x, y, -8, 8, 0, limite_droite, playerImg)  # "classe init"

    ### initialiser ennemi ###
    enemyX, enemyY = L_screen // 2, int(H_screen * 0.3)  
    enemyImg = pygame.image.load("GAME/assets/enemy.png")
    ennemi = Extra(enemyX,enemyY,0,0,0,enemyImg)
    
    return screen, background, joueur, ennemi
