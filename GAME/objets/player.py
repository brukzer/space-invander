import pygame


class Player:
    def __init__(self, x, y, gvx, dvx, vy, limite_droite):
        self.x = x
        self.y = y
        self.gvx = gvx  # deplacment gauche
        self.dvx = dvx  # deplacment droite
        self.vy = vy  # deplacement animation
        self.limite_droite = limite_droite

    def dep_gauche(self):
        self.x += self.gvx
        # limite le deplacement dans la fenetre
        if self.x <= 0:
            self.x = 0

    def dep_droite(self):
        self.x += self.dvx
        # limite le deplacement dans la fenetre
        if self.x >= self.limite_droite:
            self.x = self.limite_droite


class Avion(Player):
    def __init__(self, x, y, gvx, dvx, vy, limite_droite, playerImg):
        super().__init__(x, y, gvx, dvx, vy, limite_droite)
        self.playerImg = playerImg

    # screen doit etre pris en  arg !!
    def afficher(self, screen):
        screen.blit(self.playerImg, (self.x, self.y))
