## File name: enemy.py
## Description: Holds the enemy entity class

import pygame
import config
from entities.drone import Drone

class Enemy(Drone):
    def __init__(self, x, y):
        super().__init__(x, y, config.ENEMY_X_SPEED, config.ENEMY_Y_SPEED, config.ENEMY_RADIUS, config.ENEMY_COLOR)