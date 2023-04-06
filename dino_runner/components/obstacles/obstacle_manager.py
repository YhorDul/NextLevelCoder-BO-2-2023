from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.bird_obstacles.bird import Bird
from dino_runner.components.obstacles.patada import Frezer
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS, FREZER
import pygame
import random


class ObstacleManager:

    def __init__(self):
        self.obstacles = []


    def update(self, game):
       
        if len(self.obstacles) == 0:
            self.obstacle_type = random.randint(0, 3)
            if self.obstacle_type == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))

            if self.obstacle_type == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))

            if self.obstacle_type == 2:
                self.obstacles.append(Frezer(FREZER))

            else:
                if self.obstacle_type == 3:
                    self.obstacles.append(Bird(BIRD)) 
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.mixer.music.load("dino_runner/assets/music/gokuuu.mp3")
                    pygame.mixer.music.play()
                    pygame.time.delay(2000)
                    game.playing = False
                    game.death_count +=1
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            if len(self.obstacles) != 0:
                if isinstance(obstacle, Bird):
                    obstacle.fly(BIRD)
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles = []
        


