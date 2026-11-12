import pygame

from classes.player import Avion

from classes.ennemi import Extra
from end.init import init_game
from classes.arme import Weapon

clock = pygame.time.Clock() # gere les fps
running = True # variable on/off


def main(clock, running):

    screen, background, joueur, ennemi = init_game() #charge tout les "objets" à afficher

    # création des armes
    weapons = Weapon(screen)

    while running:
        # Gestion des evenements
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

        # Detection des touches maintenues
        keys = pygame.key.get_pressed()

        # Deplacement continu
        if keys[pygame.K_LEFT]:
            joueur.dep_gauche()

        if keys[pygame.K_RIGHT]:
            joueur.dep_droite()

        # Tirs continus
        if keys[pygame.K_SPACE]:
            weapons.shoot_continuous(joueur.x + 30, joueur.y)

        # Affichage
        screen.blit(background, (0, 0))
        joueur.afficher(screen)
        weapons.update()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    # ?? le menu devra lancer cette fonction avec un button "jouer"
    main(clock, running)
