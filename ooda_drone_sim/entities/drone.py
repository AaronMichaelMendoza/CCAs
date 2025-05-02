## File name: drone.py
## Description: Holds the drone entity class

import pygame
import config

class Drone:
    def __init__(self, x, y, speed_x, speed_y, radius, color):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.color = color

    def draw(self, world):
        pygame.draw.circle(world, self.color, (self.x, self.y), self.radius) # surface, color, center, radius  

    def update(self):
        if (self.x > config.SCREEN_WIDTH or self.x < 0):
            self.speed_x *= -1
        if (self.y > config.SCREEN_HEIGHT or self.y < 0):
            self.speed_y *= -1
        self.x += self.speed_x
        self.y += self.speed_y  