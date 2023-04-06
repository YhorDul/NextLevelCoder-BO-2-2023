import pygame
from dino_runner.utils.constants import FONT_STYLE, COLORS,SCREEN_HEIGHT,SCREEN_WIDTH


class TextUtils:
    def get_score_element(self, points):
        font = pygame.font.Font(FONT_STYLE, 22) 
        text = font.render('Points: '+ str(points), True, COLORS['Golden']) 
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        return text, text_rect
    
    def get_centered_message(self, message, height = SCREEN_HEIGHT//2 + 100, width = SCREEN_WIDTH//2):
        font = pygame.font.Font(FONT_STYLE, 35) 
        text = font.render(message, True, COLORS['Golden']) 
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        return text, text_rect
    
    def get_time_powerup(self, time_to_show):
        font = pygame.font.Font(FONT_STYLE, 15) 
        text = font.render('Time power up: '+ str(time_to_show), True, COLORS['Blue']) 
        text_rect = text.get_rect()
        text_rect.center = (100,50)
        return text, text_rect
        
        

