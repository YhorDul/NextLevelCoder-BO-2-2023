from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.bird_obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS
import pygame
import random


class ObstacleManager:

    def __init__(self):
        self.obstacles = []


    def update(self, game):
       
        if len(self.obstacles) == 0:
            self.obstacle_type = random.randint(0, 2)
            if self.obstacle_type == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))

            if self.obstacle_type == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))

            else:
                if self.obstacle_type == 2:
                    self.obstacles.append(Bird(BIRD)) 
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                pygame.time.delay(3000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            if len(self.obstacles) != 0:
                if isinstance(obstacle, Bird):
                    obstacle.fly(BIRD)
            obstacle.draw(screen)

        


