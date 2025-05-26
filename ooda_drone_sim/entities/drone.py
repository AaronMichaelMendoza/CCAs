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
        self.x += self.speed_x
        self.y += self.speed_y
        self.enforce_boundary()

    def enforce_boundary(self):
        if self.x + self.radius > config.SCREEN_WIDTH or self.x - self.radius < 0:
            self.speed_x *= -1
        if self.y + self.radius > config.SCREEN_HEIGHT or self.y - self.radius < 0:
            self.speed_y *= -1