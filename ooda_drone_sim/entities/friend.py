## File name: friend.py
## Description: Holds the friend entity class

import pygame
import config
from entities.drone import Drone

class Friend(Drone):
    def __init__(self, x, y):
        super().__init__(x, y, config.DRONE_X_SPEED, config.DRONE_Y_SPEED, config.DRONE_RADIUS, config.DRONE_COLOR)