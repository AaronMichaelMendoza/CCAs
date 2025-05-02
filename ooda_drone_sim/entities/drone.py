## File name: drone.py
## Description: Holds the drone entity class

import pygame
import config

class Drone:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, world):
        pygame.draw.circle(world, config.DRONE_COLOR, (self.x, self.y), config.DRONE_RADIUS) # surface, color, center, radius  

    def update(self):
        pass