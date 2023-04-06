import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, CLOUD_D, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, COLORS, RUNNING, DRAGON_MENU
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.text_util import TextUtils
import random


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 0
        self.y_pos_cloud = random.randint(80, 100)
        self.x_pos_cloud_d = 0
        self.y_pos_cloud_d = random.randint(60, 100)
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.text_utils = TextUtils()
        self.points = 0
        self.game_running = True
        self.death_count = 0
        self.powerup_manager = PowerUpManager()
        pygame.mixer.music.load("dino_runner/assets/music/Menuporta.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        
        

    def execute(self):
        while self.game_running:
            if not self.playing:
                self.show_menu()
  

    def run(self):
        # Game loop: events - update - draw
        self.powerup_manager.reset_power_ups(self.points)
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.color_screen()
        #self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
        cloud_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (cloud_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (cloud_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = image_width/2
        self.x_pos_cloud -= self.game_speed

        cloud_width_d = CLOUD_D.get_width()
        self.screen.blit(CLOUD_D, (cloud_width_d + self.x_pos_cloud_d, self.y_pos_cloud_d))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD_D, (cloud_width_d + self.x_pos_cloud_d, self.y_pos_cloud_d))
            self.x_pos_cloud_d = image_width
        self.x_pos_cloud_d -= self.game_speed

    def score(self):
        self.points += 1
        text, text_rect = self.text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)
        active_powers, time_powerup = self.player.check_invincibility(self.screen)
        if active_powers:
            text, text_rect = self.text_utils.get_time_powerup(time_powerup)
            self.screen.blit(text, text_rect)

    def show_menu(self):
        self.game_running = True
        self.screen.fill(COLORS['White'])
        self.print_menu_elements()
        
        pygame.display.update()
        self.handle_key_event_on_menu()
        
    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2

        if self.death_count == 0:
            text, text_rect = self.text_utils.get_centered_message("Press Any Key to Start")
            self.screen.blit(text, text_rect)
        
        elif self.death_count > 0:
            score, score_rect = self.text_utils.get_centered_message('Your Score: ' + str(self.points), height=half_screen_height +50)
            death, deaht_rect = self.text_utils.get_centered_message('Death count: ' + str(self.death_count), height=half_screen_height +100)

            self.screen.blit(score, score_rect)
            self.screen.blit(death, deaht_rect)  
        self.screen.blit(DRAGON_MENU[0], (half_screen_width - 400, half_screen_height - 300))
        self.screen.blit(DRAGON_MENU[1], (half_screen_width - 550, half_screen_height + 100))
        self.screen.blit(DRAGON_MENU[2], (half_screen_width + 200, half_screen_height + 50))

    def handle_key_event_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def color_screen(self):
        if self.points >= 0:
            self.screen.fill((255,255,255))
        if self.points >= 500:
            self.screen.fill((225,225,225))
        if self.points >= 502:
            self.screen.fill((200,200,200))
        if self.points >= 504:
            self.screen.fill((181,178,178))
        if self.points >= 506:
            self.screen.fill((150, 150, 150))
        if self.points >= 508:
            self.screen.fill((125, 125, 125))
        if self.points >= 510:
            self.screen.fill((100, 100, 100))
        if self.points >= 512:
            self.screen.fill((75, 75, 75))
        if self.points >= 514:
            self.screen.fill((50, 50, 50))
        if self.points >= 516:
            self.screen.fill((25, 25, 25))
        if self.points >= 520:
            self.screen.fill((0,0,0))
        

