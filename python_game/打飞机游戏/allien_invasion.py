import pygame
from time import sleep
import sys
#导入设置类
from settings import Settings
#导入飞船类
from ship import Ship
#导入子弹类
from bullet import Bullet
#导入外星人类
from alien import Alien
#导入统计信息
from game_stats import GameStats
#导入按钮类

from button import Button
#导入记分牌
from scoreboard import Scoreboard


class AlienInvasion:
    def __init__(self):
        #调用函数pygame.init,初始化背景设置
        pygame.init()
        #实例化settings
        self.settings=Settings()

        #创建一个显示窗口，宽1200 高度800,将设置放在settings模块中
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        #游戏的一个窗口上的名称
        pygame.display.set_caption("打飞机")
        #定义游戏的背景颜色，从setting中调用
        self.bg_color=(self.settings.bg_color)
        #实例化飞船
        self.ship=Ship(self)
        #初始化子弹
        self.bullets=pygame.sprite.Group()
        #初始化外星人
        self.aliens=pygame.sprite.Group()
        #创建外星人群
        self._create_fleet()
        #创建存储游戏统计信息的实例并且创建记分牌
        self.stats=GameStats(self)
        self.sb = Scoreboard(self)
        #创建Play按钮
        self.play_button = Button(self,"Play")
        




    def run_game(self):
        #开始游戏的主循环
        while True:
            #响应鼠标和键盘的事件
            self._check_events()
            if self.stats.game_active:
                #更新飞船的位置
                self.ship.update()
                #更新子弹的位置
                self._update_bullets()
                #更新外星人的位置
                self._upadate_aliens()
            #响应屏幕刷新的事件    
            self._update_screen()


    def _check_events(self):
        #监控键鼠标的事件循环，如果触发退出事件，则关闭
        for event in pygame.event.get():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            if event.type == pygame.QUIT:
                sys.exit()
            #控制飞船的移动
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
            #控制鼠标点击按钮的事件
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
            #管理开始按钮
    def _check_play_button(self,mouse_pos):
        button_clicked=self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #重置游戏设置
            self.settings.initialize_dynamic_settings()
        #重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active=True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
        #清空剩下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
        #创建一群新的外星人并且让飞船居中
            self._create_fleet()
            self.ship.center_ship() 
            #隐藏鼠标光标
            pygame.mouse.set_visible(False)


            
    #管理键盘按键按下事件触发      
    def _check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
            #向右移动飞船
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            #向右移动飞船
            self.ship.moving_left=True
            #发射子弹
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key==pygame.K_q:
            #按下q键退出游戏
            sys.exit()

    #管理按键松开的触发事件
    def _check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
            #向右移动飞船
            self.ship.moving_right=False
        if event.key==pygame.K_LEFT:
            #向右移动飞船
            self.ship.moving_left=False

    #管理子弹的射出
    def _fire_bullet(self):
        #在限制子弹在屏幕中同时出现的次数前提下射出子弹
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet =Bullet(self)
            self.bullets.add(new_bullet)

    #子弹的管理
    def _update_bullets(self):
        #子弹位置的更新
        self.bullets.update()
        #删除越过屏幕的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
            # print(len(self.bullets))
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        #响应子弹和外星人发生碰撞
        #删除彼此碰撞的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        #整群外星人都被消灭，清空子弹，创建新的一群外星人，提高他们的速度，提高等级
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level +=1
            self.sb.prep_level()
        if collisions:
            self.stats.score +=self.settings.alien_points
            #碰撞之后更新当前得分和最高得分
            self.sb.prep_score()
            self.sb.check_high_score()
        
        
    #创建外星人群
    def _create_fleet(self):
        #创建第一个外星人
        alien = Alien(self)
        #计算一个屏幕能够容纳多少个外星人
        alien_width,alien_height=alien.rect.size
        available_space_x=self.settings.screen_width -(2*alien_width)
        number_alien_x = available_space_x//(2*alien_width)
        #计算屏幕可以容纳多少行外星人
        ship_height=self.ship.rect.height
        available_space_y=(self.settings.screen_height-(3*alien_height)-ship_height)
        number_rows=available_space_y//(2*alien_height)
        # 创建外星人
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number,row_number)


    def _create_alien(self,alien_number,row_number):
        #创建一个外星人并且放在当前行
        alien = Alien(self)
        alien_width,alien_height=alien.rect.size
        alien.x = alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
        self.aliens.add(alien)
    
        #管理所有外星人的移动
    def _upadate_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人与飞船的碰撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        #检测是否有外星人到达了屏幕底端
        self._check_aliens_bottom() 

    def _ship_hit(self):
        #响应飞船被外星人撞到
        if self.stats.ships_left>0: 
            self.stats.ships_left-=1
            self.sb.prep_ships()
            #清空剩下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            #创建一群新的外星人，并且将飞船放到屏幕的中央
            self._create_fleet()
            self.ship.center_ship()
            #暂停
            sleep(0.5)
        else:
            self.stats.game_active=False
            pygame.mouse.set_visible(True)

    #检测外星人是否碰触到屏幕底部
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=screen_rect.bottom:
                self._ship_hit()
                break
    


    #检测外星人是够碰触屏幕右侧后改变外星人的方向
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    #改变外星人群移动的方向
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet__drop_speed
        self.settings.fleet_direction*=-1

    
    # 刷新屏幕
    def _update_screen(self):
        #填充背景色，每次循环刷新
        self.screen.fill(self.settings.bg_color)
        #画出飞船和它的位置在主循环中
        self.ship.blitme()
        #子弹发射的渲染
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #外星人的渲染
        self.aliens.draw(self.screen)
        #显示得分
        self.sb.show_score()
        #对按钮的渲染
        if not self.stats.game_active:
            self.play_button.draw_button()
        #更新屏幕用的代码
        pygame.display.flip()

#运行主类
if __name__ == '__main__':
    ai =AlienInvasion()
    ai.run_game()
