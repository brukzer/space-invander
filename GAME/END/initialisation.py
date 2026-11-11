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


# TAILLE de la fenetre
#TODO fenetre dynamique
L_screen = 1280
H_screen = 800
# affichage fenetre
screen = pygame.display.set_mode((L_screen, H_screen))
# TODO changer les "background" apres chaque niveau
background = pygame.image.load("GAME/assets/background.png")
background = pygame.transform.scale(background, (L_screen, H_screen))  # IA
