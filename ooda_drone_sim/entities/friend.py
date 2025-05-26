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
        observations = self.observe(enemies)
        threat_info = self.orient(observations)
        decision = self.decide(threat_info)
        self.act(decision)

    def observe(self, enemies):
        observations = []
        for enemy in enemies:
            dist = math.hypot(enemy.x - self.x, enemy.y - self.y)
            observations.append((enemy, dist))
        return observations
    
    def orient(self, observations):
        closest_enemy = None
        min_dist = float('inf')
        for enemy, dist in observations:
            if dist < min_dist:
                min_dist = dist
                closest_enemy = enemy
        return {"enemy": closest_enemy, "distance": min_dist}
    
    def decide(self, threat_info):
        if threat_info["distance"] < config.DETECTION_RADIUS:
            return "flee", threat_info["enemy"]
        else:
            return "idle", None
        
    def act(self, decision):
        action, target = decision

        if action == "flee":
            dx = self.x - target.x
            dy = self.y - target.y
            norm = math.hypot(dx, dy)

            if norm == 0:
                angle = random.uniform(0, 2 * math.pi)
                self.speed_x = math.cos(angle) * config.FRIEND_X_SPEED
                self.speed_y = math.sin(angle) * config.FRIEND_Y_SPEED
            else:
                self.speed_x = (dx / norm) * abs(config.FRIEND_X_SPEED)
                self.speed_y = (dy / norm) * abs(config.FRIEND_Y_SPEED)

            # Enforce minimum speed
            if abs(self.speed_x) < config.MIN_SPEED:
                self.speed_x = math.copysign(config.MIN_SPEED, self.speed_x)
            if abs(self.speed_y) < config.MIN_SPEED:
                self.speed_y = math.copysign(config.MIN_SPEED, self.speed_y)

            self.x += self.speed_x
            self.y += self.speed_y

        elif action == "idle":
            super().update()