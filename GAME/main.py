import pygame
from end.init import init_game, init_player, init_ennemy,L_screen, H_screen 
from classes.arme import Weapon

clock = pygame.time.Clock()  # gere les fps
running = True  # variable on/off

#TODO ranger les variables


screen = pygame.display.set_mode((L_screen, H_screen))


def main(clock, running, screen):

    background = init_game()  
    joueur = init_player()
    # création des armes
    weapons = Weapon(screen)
    spawn_timer = 0
    ennemis = []
    ennemis.append(init_ennemy())

    while running:
        ## TIME ##
        spawn_timer += clock.get_time()

        # Gestion des evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ## ----------- Générez l'affichage ici -----------
        screen.blit(background, (0, 0))  # fond
        ### JOUEUR ###
        joueur.afficher(screen)  # player
        ### ENNEMI ###
        if spawn_timer > 2000:  # 2000 ms = 2 secondes
            spawn_timer = 0
            ennemis.append(
                init_ennemy()
            )
        for e in ennemis:
            e.afficher(screen)
            e.move()

            # reste de l'affichage
        ## ----------- Générez l'affichage jusqu'ici -----------

        # Detection des touches maintenues
        keys = pygame.key.get_pressed()
        ### JOUEUR ###
        # Deplacement continu
        if keys[pygame.K_LEFT]:
            joueur.move(-1)
        if keys[pygame.K_RIGHT]:
            joueur.move(1)
        # Tirs continus
        if keys[pygame.K_SPACE]:
            weapons.shoot_continuous(joueur.x + 30, joueur.y)

        ### ennemi ###

        weapons.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    # ?? le menu devra lancer cette fonction avec un button "jouer"
    main(clock, running, screen)
