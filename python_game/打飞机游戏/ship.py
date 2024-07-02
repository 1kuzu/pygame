import pygame
from pygame.sprite import Sprite
 
class Ship(Sprite):
    #一个管理飞船的类
 
    def __init__(self, ai_game):
        
        super().__init__()
        #初始化飞船并且设置它的初始位置
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船的图片并且获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船都放在底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 将self.rect的值转化为浮点型然后赋值给self.x
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #根据移动标志来调整飞船的位置
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        self.rect.x=self.x
    


    def blitme(self):
        #实时绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #让飞船在屏幕底部居中
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
