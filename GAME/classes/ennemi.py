

"""
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)
"""

class Ennemi:
    def __init__(self,enemyX,enemyY,enemyGVX,enemyDVX,enemyVY,):
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyGVX = enemyGVX
        self.enemyDVX = enemyDVX
        self.enemyVY = enemyVY
        
    def apparaitre(self):
        pass
    def deplacement(self):
        pass
    def touche_le_fond(self):
        pass

class Extra(Ennemi):
    def __init__(self,enemyX,enemyY,enemyGVX,enemyDVX,enemyVY,enemyImg):
        super().__init__(enemyX,enemyY,enemyGVX,enemyDVX,enemyVY)
        self.enemyImg = enemyImg
        
    def afficher(self, screen):
        screen.blit(self.enemyImg,(self.enemyX, self.enemyY))