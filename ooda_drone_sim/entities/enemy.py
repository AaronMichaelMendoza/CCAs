## File name: enemy.py
## Description: Holds the enemy entity class

import pygame
import config

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, world):
        pygame.draw.circle(world, config.ENEMY_COLOR, (self.x, self.y), config.ENEMY_RADIUS) # surface, color, center, radius  

    def update(self):
        pass  