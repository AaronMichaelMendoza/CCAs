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
        self.current_threat = None
        self.flee_vector = (self.speed_x, self.speed_y)

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
        biggest_threat = None
        max_threat_score = float('inf')
        for enemy, dist in observations:
            threat_score = config.DISTANCE_WEIGHT / dist
            if threat_score < max_threat_score:
                max_threat_score = threat_score
                biggest_threat = enemy
        return {"enemy": biggest_threat, "threat_score": max_threat_score}
    
    def decide(self, threat_info):
        if threat_info["threat_score"] < config.THREAT_SCORE_THRESHOLD:
            return "flee", threat_info["enemy"]
        else:
            return "idle", None
        
    def act(self, decision):
        action, enemy = decision

        if action == "flee":
            # Only recalculate direction if enemy has changed or norm is small
            if self.current_threat != enemy or math.hypot(self.speed_x, self.speed_y) < config.MIN_SPEED:
                dx = self.x - enemy.x
                dy = self.y - enemy.y
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

                self.current_threat = enemy  # Track current enemy

            # Move and bounce
            self.x += self.speed_x
            self.y += self.speed_y
            super().enforce_boundary()

        elif action == "idle":
            self.current_threat = None  # reset flee logic
            super().update()