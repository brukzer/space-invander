import pygame
from pygame import mixer


def collision(bullets,ennemies,explosionSound):
    
    for bullet in bullets:
        for ennemi in ennemies:
            if bullet.hitbox.colliderect(ennemi.hitbox):
                #recuperer la position de la collision
                collision_xy = bullet.hitbox.clip(ennemi.hitbox) #IA
                x = collision_xy.centerx
                y = collision_xy.centery
                #animations
                explosionSound.play()
                
                bullets.remove(bullet)
                ennemies.remove(ennemi)
