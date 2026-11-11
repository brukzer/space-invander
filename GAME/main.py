# screen = pygame.display.set_mode((800, 600))
# background = pygame.image.load('background.png')

# Example file showing a basic pygame "game loop"
import pygame
from objets.player import Avion
from 
# pygame setup

# TAILLE de la fenetre
#TODO fenetre dynamique
L_screen = 1280
H_screen = 800
# affichage fenetre
screen = pygame.display.set_mode((L_screen, H_screen))
# TODO changer les "background" apres chaque niveau
background = pygame.image.load("GAME/assets/background.png")
background = pygame.transform.scale(background, (L_screen, H_screen))  # IA

# gere les fps
clock = pygame.time.Clock()

# variable on/off
running = True

# Initialiser class Player.Avion
#TODO Creer une selection d'avion
playerImg = pygame.image.load("GAME/assets/player.png").convert_alpha()
playerImg = pygame.transform.scale(playerImg, (150, 150))#IA
# reprend la dimension d affichage pour afficher player  #?? trouver une meilleur methode
x = L_screen // 2
y = int(H_screen * 0.8)
# TODO adapté a la taille de 'player' afin d éviter les débordements
limite_droite = int(L_screen) - 30
joueur = Avion(x, y, -8, 8, 0, limite_droite, playerImg)


def main(screen, clock, running):
    pygame.init()
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # afficher fond + player + arme
        screen.blit(background, (0, 0))
        joueur.afficher(screen)
        #arme

        ## ??Générez votre jeu ici
        # placement player
        # TODO traiter le conflit des touches ou souris "<-" et "->" 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                joueur.dep_gauche()
            if event.key == pygame.K_RIGHT:
                joueur.dep_droite()

            # TODO adapter les tirs
            """
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            """
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    # ?? le menu devra lancer cette fonction avec un button "jouer"
    main(screen, clock, running)
