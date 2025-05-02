## File name: friend.py
## Description: Holds the friend entity class

import pygame
import math
import random
import config
from entities.drone import Drone

class Friend(Drone):
    def __init__(self, x, y):
        super().__init__(x, y, config.FRIEND_X_SPEED, config.FRIEND_Y_SPEED, config.FRIEND_RADIUS, config.FRIEND_COLOR)

    def update(self, enemies):
        closest_enemy = None
        min_dist = float('inf')
        for enemy in enemies:
            dist = math.hypot(enemy.x - self.x, enemy.y - self.y)
            if dist < min_dist:
                min_dist = dist
                closest_enemy = enemy
        
        if min_dist < config.DETECTION_RADIUS:
            # Flee
            dx = self.x - closest_enemy.x
            dy = self.y - closest_enemy.y
            norm = math.hypot(dx, dy) # Magnitude of difference vector

            if (norm == 0): 
                # They are on top of each other — pick random escape direction
                angle = random.uniform(0, 2 * math.pi)
                self.speed_x = math.cos(angle) * config.FRIEND_X_SPEED
                self.speed_y = math.sin(angle) * config.FRIEND_Y_SPEED
            else: 
                self.speed_x = (dx / norm) * abs(config.FRIEND_X_SPEED) # x direction * speed
                self.speed_y = (dy / norm) * abs(config.FRIEND_Y_SPEED) # y direction * speed 

            # Avoid freezing, enforce minimum speed
            if abs(self.speed_x) < config.MIN_SPEED:
                self.speed_x = math.copysign(config.MIN_SPEED, self.speed_x)
            if abs(self.speed_y) < config.MIN_SPEED:
                self.speed_y = math.copysign(config.MIN_SPEED, self.speed_y)

        else:
            # Idle
            super().update()