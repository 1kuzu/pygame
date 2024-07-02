import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #管理外星人的基础信息
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.settings=ai_game.settings

    def update(self):
        #向右移动外星人
        self.x+=(self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x=self.x
    
    def check_edges(self):
        #检测外星人是否碰触到屏幕的边缘
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right or self.rect.left<=0:
            return True
    






