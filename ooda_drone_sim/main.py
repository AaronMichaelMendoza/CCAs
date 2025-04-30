## File name: main.py
## Description: Entry point that runs simulation

import pygame
import config as constants
from entities.drone import Drone
from entities.enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()

friend = Drone(50, 200, 150)
foe = Enemy(30, 400, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255, 255, 255))  # Clear screen every frame

    friend.update()
    foe.update()

    friend.draw(screen)
    foe.draw(screen)

    pygame.display.flip()         # Refresh screen

    clock.tick(constants.FPS)  # Limit to 60 FPS