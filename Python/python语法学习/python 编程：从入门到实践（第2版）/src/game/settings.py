from dotenv import load_dotenv
import os

load_dotenv() # 加载 .env

class Settings:
    """"存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置。"""
        # 屏幕设置
        self.screen_width = int(os.getenv('SCREEN_WIDTH'))
        self.screen_height = int(os.getenv('SCREEN_HEIGHT'))
        color = os.getenv('BG_COLOR').split(",")
        # print(color)
        self.bg_color = tuple(int(color[i]) for i in range(len(color)))