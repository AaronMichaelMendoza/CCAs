## File name: main.py
## Description: Entry point that runs simulation

import pygame
import config
from entities.drone import Drone
from entities.enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

friend = Drone(200, 150)
foe = Enemy(400, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear screen every frame
    screen.fill(config.SCREEN_COLOR)  

    friend.update()
    foe.update()

    friend.draw(screen)
    foe.draw(screen)

    # Refresh screen
    pygame.display.flip()         

    # Limit to 60 FPS
    clock.tick(config.FPS)  