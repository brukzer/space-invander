import pygame


class Player:
    def __init__(self, x, y, speed,direction, vy, limite_droite):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.vy = vy  # deplacement animation
        self.limite_droite = limite_droite

    def move(self,direction) :
        self.x += self.speed * direction 
        self.x = max(0,min(self.x,self.limite_droite)) # min pour droite , max pour gauche


class Avion(Player):
    def __init__(self, x, y, direction, vy, limite_droite, playerImg):
        super().__init__(x, y, 8, direction, vy, limite_droite) # speed est donner ici grace a super mais n est pas reutilise par la sous class
        self.playerImg = playerImg
        

    # TODO mettre dans class Player
    def afficher(self, screen):
        screen.blit(self.playerImg, (self.x, self.y))
