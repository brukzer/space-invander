import pygame

#playerX_deplacment // vx = 0

class Player:
    def __init__(self,x,y,gvx,dvx,vy):
        self.x = x
        self.y = y
        # deplacment joueur
        self.gvx = gvx
        self.dvx = dvx
        #deplacement animation
        self.vy = vy

    def dep_gauche(self):
        self.x += self.gvx

    def dep_droite(self):
        self.x += self.dvx
        
        

class Avion(Player):
    def __init__(self,x,y,gvx,dvx,vy,playerImg):
        super().__init__(x,y,gvx,dvx,vy)
        self.playerImg = playerImg

    #screen doit etre pris en  arg !!
    def afficher(self,screen):
        screen.blit(self.playerImg, (self.x, self.y))
        