## File name: enemy.py
## Description: Holds the enemy entity class

import pygame

class Enemy:
    def __init__(self, radius, longitude, latitude):
        self.radius = radius
        self.x = longitude
        self.y = latitude

    def draw(self, world):
        # Draw a grayish circle
        pygame.draw.circle(world, (50, 50, 50), (self.x, self.y), self.radius) # surface, color, center, radius  

    def update(self):
        pass  