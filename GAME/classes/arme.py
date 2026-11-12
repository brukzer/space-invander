# arme + balle
#recuperer la position du canon  pour y tirer la balle correctement positionné 
# #bonus tirer grace a la souris + viser


import pygame


class Bullet:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./GAME/assets/bullet.png')
        self.x = 0
        self.y = 0
        self.speed = 10 # !! négatif car on remonte la page
        self.state = "ready"

    def fire(self, x, y):
        if self.state == "ready":
            self.x = x
            self.y = y
            self.state = "fire"

    def update(self):
        if self.state == "fire":
            self.y -= self.speed

            if self.y < 0:
                self.state = "ready"
            else:
                self.screen.blit(self.image, (self.x, self.y))


class Weapon:
    def __init__(self, screen):
        self.screen = screen

        self.bullets = []

        self.last_shot = 0
        self.shoot_delay = 400 # firerate (en millisecondes)

    def create_2_bullets(self, x, y):
        bullet1 = Bullet(self.screen)
        bullet2 = Bullet(self.screen)

        bullet1.fire(x, y)
        bullet2.fire(x + 60, y)

        self.bullets.append(bullet1)
        self.bullets.append(bullet2)

    def shoot_continuous(self, x, y):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot >= self.shoot_delay:
            self.create_2_bullets(x, y)
            self.last_shot = current_time

    def update(self):
        for bullet in self.bullets[:]:
            bullet.update()

            if bullet.state == "ready":
                self.bullets.remove(bullet)
