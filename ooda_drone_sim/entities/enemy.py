## File name: enemy.py
## Description: Holds the enemy entity class

import pygame
import math
import random
import config
from entities.drone import Drone

class Enemy(Drone):
    def __init__(self, x, y):
        super().__init__(x, y, config.ENEMY_X_SPEED, config.ENEMY_Y_SPEED, config.ENEMY_RADIUS, config.ENEMY_COLOR)

    def update(self, friend):
        # Direction vector is toward the friend
        dx = friend.x - self.x
        dy = friend.y - self.y
        norm = math.hypot(dx, dy)
        if norm == 0:
            angle = random.uniform(0, 2 * math.pi)
            self.speed_x = math.cos(angle) * config.ENEMY_X_SPEED
            self.speed_y = math.sin(angle) * config.ENEMY_Y_SPEED
        else:
            self.speed_x = (dx / norm) * config.ENEMY_X_SPEED
            self.speed_y = (dy / norm) * config.ENEMY_Y_SPEED

        super().update()

    # TODO Create function to have enemies not bump into each other, or swarm behavior