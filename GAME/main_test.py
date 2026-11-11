#screen = pygame.display.set_mode((800, 600))
#background = pygame.image.load('background.png')

# Example file showing a basic pygame "game loop"
import pygame
from objets.player import Avion 

# pygame setup

# TAILLE de la fenetre
L_screen= 1280
H_screen = 720
# affichage fenetre
screen = pygame.display.set_mode((L_screen, H_screen))
#TODO changer les "background" apres chaque nv
background = pygame.image.load('background.png')
#IA
background = pygame.transform.scale(background, (L_screen, H_screen))

# gere les fps
clock = pygame.time.Clock()

#variable on/off
running = True

#Initialiser class
playerImg = pygame.image.load('player.png')
# reprend la dimension d affichage => placer player  #?? trouver une meilleur methode
x = L_screen // 2
y = int(H_screen * 0.8)
joueur = Avion(x,y,-8,8,0,playerImg)


def lancer(screen,clock,running):
    pygame.init()
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.blit(background, (0, 0))
        joueur.afficher(screen)
      
        ## ??Générez votre jeu ici
        #placement player
        #TODO traiter le conflit des touche "<-" et "->"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                joueur.dep_gauche()
            if event.key == pygame.K_RIGHT:
                joueur.dep_droite()
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
    #?? le menu devra lancer cette fonction avec un button "jouer"
    lancer(screen,clock,running)
    