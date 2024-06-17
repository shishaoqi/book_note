import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        pygame.init()

        # 配置
        self.St = Settings()

        self.screen = pygame.display.set_mode((self.St.screen_width, self.St.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #创建完 Ship 类后，导入并设置为 ship
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.St.bg_color)
            self.ship.blitme()

            # 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()