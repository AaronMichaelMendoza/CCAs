## File name: main.py
## Description: Entry point that runs simulation

import pygame
import random
import config
from entities.friend import Friend
from entities.enemy import Enemy

# Initialization
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

def main():
    start_friend_x = random.randint(config.FRIEND_RADIUS, config.SCREEN_WIDTH - config.FRIEND_RADIUS)
    start_friend_y = random.randint(config.FRIEND_RADIUS, config.SCREEN_HEIGHT - config.FRIEND_RADIUS)
    friend = Friend(start_friend_x, start_friend_y)

    enemies = []
    for _ in range(config.NUM_ENEMIES):
        start_enemy_x = random.randint(config.ENEMY_RADIUS, config.SCREEN_WIDTH - config.ENEMY_RADIUS)
        start_enemy_y = random.randint(config.ENEMY_RADIUS, config.SCREEN_HEIGHT - config.ENEMY_RADIUS) 
        enemies.append(Enemy(start_enemy_x, start_enemy_y))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Clear screen every frame
        screen.fill(config.SCREEN_COLOR)  

        # OODA loop
        friend.update(enemies)
        for enemy in enemies:
            enemy.update(friend) 

        friend.draw(screen)
        for enemy in enemies:
            enemy.draw(screen) 

        # Refresh screen
        pygame.display.flip()         

        # Limit to 60 FPS
        clock.tick(config.FPS)  

if __name__ == "__main__":
    main()