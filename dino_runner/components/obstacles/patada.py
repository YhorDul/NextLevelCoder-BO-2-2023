from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Frezer(Obstacle):
    def __init__(self, image_list):
        self.type = random.randint(0, 1)
        super().__init__(image_list[self.type])
        self.rect.y = random.randint(250, 270)