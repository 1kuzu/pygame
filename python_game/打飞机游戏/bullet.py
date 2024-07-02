import pygame
#导入pygame中的精灵方法
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color =self.settings.bullet_color
        #在(0,0)处创建一个表示子弹的矩形，并且设置正确的位置
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bulle_height)
        self.rect.midtop=ai_game.ship.rect.midtop

        #存储用小数表示子弹的位置。
        self.y=float(self.rect.y)

    #更新子弹的位置
    def update(self):
        self.y-=self.settings.bullet_speed
        self.rect.y=self.y
    #绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    