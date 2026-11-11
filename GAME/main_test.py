#screen = pygame.display.set_mode((800, 600))
#background = pygame.image.load('background.png')

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
#taille de la fenetre
L_screen= 1280
H_screen = 720
#fenetre
screen = pygame.display.set_mode((L_screen, H_screen))
#TODO changer les "background" apres chaque nv
background = pygame.image.load('background.png')
#IA
background = pygame.transform.scale(background, (L_screen, H_screen))
# gere les fps
clock = pygame.time.Clock()
#variable on/off
running = True


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
        ## ??Générez votre jeu ici

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()








if __name__ == "__main__":
    lancer(screen,clock,running)
    