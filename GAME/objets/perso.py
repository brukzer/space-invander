

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0



def player(x, y):
    screen.blit(playerImg, (x, y))