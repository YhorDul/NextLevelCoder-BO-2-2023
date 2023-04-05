from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random

class Bird(Obstacle):
    def __init__(self, image_list):
        self.type = 0
        super().__init__(image_list[self.type])
        self.rect.y = random.randint(250, 300)
        self.rect.x += 400 
        self.step_index = 0

    def fly(self, image_list):
        self.image = image_list[0] if self.step_index < 5 else image_list[1]
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0
        

        
        
