## File name: main.py
## Description: Entry point that runs simulation

import pygame
import config
from entities.friend import Friend
from entities.enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

friend = Friend(200, 150)
enemy = Enemy(400, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear screen every frame
    screen.fill(config.SCREEN_COLOR)  

    friend.update()
    enemy.update()

    friend.draw(screen)
    enemy.draw(screen)

    # Refresh screen
    pygame.display.flip()         

    # Limit to 60 FPS
    clock.tick(config.FPS)  