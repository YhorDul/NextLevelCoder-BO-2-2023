import random
import pygame
from dino_runner.components.powerups.seed import Seed

from dino_runner.components.powerups.shield import Shield


class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.points = 0
        self.option_numbers = list(range(1, 10))
        #self.wich_appears = 0

    def reset_power_ups(self, points):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points
        #self.wich_appears = random.randint(100, 400) + self.points

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                print("generating powerup")
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                wich_appears = random.randint(0, 5)
                if wich_appears == 0:
                    self.power_ups.append(Seed())
                else:
                    self.power_ups.append(Shield())

        return self.power_ups

    def update(self, points, game_speed, player, game):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.rect.colliderect(power_up.rect):
                if isinstance(power_up, Shield):
                    self.start_power_up(player, power_up)
                elif isinstance(power_up, Seed):
                    self.add_life(game, power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def start_power_up(self, player, power_up):
        power_up.start_time = pygame.time.get_ticks ()
        player.shield = True
        player.show_text = True
        player.type = power_up.type
        power_up.start_time = pygame.time.get_ticks()
        time_random = random.randrange(5, 8)
        player.shield_time_up = power_up.start_time + (time_random * 1000)
        self.power_ups.remove(power_up)

    def start_default_powerup(self, player):
        power_up = Shield()
        self.power_ups.append(power_up)
        self.start_power_up(player, power_up)
    
    def add_life(self, game, power_up):
        if not power_up.is_used:
            power_up.is_used = True
            if game.death_count >= 1:
                game.death_count -= 1
            
