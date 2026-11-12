import pygame
from classes.player import Avion
from classes.ennemi import Extra
from end.init import init_game


clock = pygame.time.Clock() # gere les fps
running = True # variable on/off


def main(clock, running):
    screen, background, joueur,ennemi = init_game() #charge tout les "objets" à afficher
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
## ----------- Générez l'affichage ici -----------
        screen.blit(background, (0, 0)) #fond
        joueur.afficher(screen) #player
        # TODO ajoute la boucle "spawn ennemi" + deplacment + collision
        ennemi.afficher(screen)
            #arme
            #reste de l'affichage
## ----------- Générez l'affichage jusqu'ici -----------

## ----------- Générez le jeu ici -----------
        # déplacement player
        # TODO traiter le conflit des touches ou/et souris 
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
## ----------- Générez le jeu jusqu'ici -----------

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
        
    pygame.quit()
if __name__ == "__main__":
    # ?? le menu devra lancer cette fonction avec un button "jouer"
    main(clock, running)
