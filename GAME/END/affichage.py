# Score

import pygame

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

scoreX = 10
scoreY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# show_score(textX, testY) => GAME LOOP / afficher score

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text(): #fonction a lancer + break pour fin
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    
"""
# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
"""