import pygame
from classes.player import Avion
from classes.ennemi import Extra
import random



# affichage fenetre
L_screen, H_screen = 1280, 800  # TAILLE de la fenetre
### variablie limite ###
limite_gauche = 0
limite_droite = int(L_screen) - 30  # limite_gauche = 0, implémenté ??
limite_bas = int(H_screen) - 15
limite_haut = 0


def init_game():

    pygame.init()
    back = pygame.image.load("GAME/assets/background.png")
    background = pygame.transform.scale(back, (L_screen, H_screen))  # IA

    return background


def init_player():

    playerImg = pygame.image.load("GAME/assets/player.png").convert_alpha()
    playerImg = pygame.transform.scale(playerImg, (150, 150))  # IA
    joueur_x = L_screen // 2 
    joueur_y = H_screen * 0.8
    direction, vy = None, None
    joueur = Avion(
        joueur_x, joueur_y, direction, vy, limite_droite, playerImg
    )  # "classe init"

    return joueur


def init_ennemy():

    dh, dv = 1, 1
    enemyX = random.randrange(0, L_screen, 5)
    enemyY = H_screen * 0.1
    enemyImg = pygame.image.load("GAME/assets/enemy.png")
    ennemi = Extra(
        enemyX, enemyY, limite_gauche, limite_droite, limite_bas, enemyImg, dh, dv
    )

    return ennemi
