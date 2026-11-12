# Enemy
enemyImg = []
#liste qui contient la position de tout les ennemi
enemyX = []
enemyY = []
#liste qui contient le vecteur de tout les ennemi
enemyX_change = []
enemyY_change = []
num_of_enemies = 6


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

class Ennemi:
    def __init__(self):
        pass
    def apparaitre(self):
        pass
    def deplacement(self):
        pass
    def touche_le_fond(self):
        pass