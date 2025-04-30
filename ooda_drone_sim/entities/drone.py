## File name: drone.py
## Description: Holds the drone entity class

import pygame

class Drone:
    def __init__(self, radius, longitude, latitude):
        self.radius = radius
        self.x = longitude
        self.y = latitude

    def draw(self, world):
        # Draw a black circle
        pygame.draw.circle(world, (0, 0, 0), (self.x, self.y), self.radius) # surface, color, center, radius  

    def update(self):
        pass  # You'll use this next week to make things move