import pygame

def collision(bullets,ennemies):
    
    for bullet in bullets:
        for ennemi in ennemies:
            if bullet.hitbox.colliderect(ennemi.hitbox):
                print("Collision !")
'''
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
'''