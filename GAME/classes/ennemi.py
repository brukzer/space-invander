

class Ennemi:
    def __init__(self,enemyX,enemyY,speed,speed_down,limite_gauche,limite_droite,limite_bas,dh,dv):
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.speed = speed
        self.speed_down = speed_down
        self.limite_gauche = limite_gauche
        self.limite_droite = limite_droite
        self.limite_bas = limite_bas
        self.dh = dh
        self.dv = dv
        
        
    def move(self):
        #TODO optimiser
        #G / D
        self.enemyX += self.speed * self.dh
        if self.enemyX >= self.limite_droite:
            self.dh = -1
        if self.enemyX <= self.limite_gauche:
            self.dh = 1
        #B / H
        self.enemyY += self.speed_down * self.dv
        if self.enemyY >= self.limite_bas:
            self.dv = 0
        #hit box  
        self.hitbox.x = self.enemyX
        self.hitbox.y = self.enemyY
             
    def postion_ennemi(self):
        return self.enemiX, self.enemyY    
        

class Extra(Ennemi):
    def __init__(self,enemyX,enemyY,limite_gauche,limite_droite,limite_bas,enemyImg,dh,dv):
        super().__init__(enemyX,enemyY,5,1,limite_gauche,limite_droite,limite_bas,dh,dv)
        self.enemyImg = enemyImg
        self.hitbox = self.enemyImg.get_rect(topleft=(self.enemyX, self.enemyY))
        
    def afficher(self, screen):
        screen.blit(self.enemyImg,(self.enemyX, self.enemyY))
        