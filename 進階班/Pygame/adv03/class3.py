######################匯入模組######################
import pygame
import os
import sys
import random


####################定義函式######################
def gophers_update():
    global tick, pos
    # 每幀循環執行的代碼
    if tick > max_tick:  # 每20次刷新變換一次
        new_pos = random.randint(0, 5)  # 隨機0到5
        pos = pos6[new_pos]  # 更新外部記錄的圓的位置
        tick = 0  # 重置計數器
    else:  # 不刷新變換的時候
        tick += 1  # 增加計數器
    pygame.draw.circle(screen, BLUE, pos, 50)  # 使用隨機位置


####################初始化######################
pygame.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()
tick = 0  # 計數器目前值
max_tick = 20  # 設定計數器最大值

######################建立視窗######################
bg_x = 600
bg_y = 400
screen = pygame.display.set_mode([bg_x, bg_y])  # 設定窗口
pygame.display.set_caption("打地鼠")

######################背景物件######################
bg = pygame.Surface([bg_x, bg_y])  # 繪製背景容器
bg.fill(BLACK)  # 將背景填滿黑色

######################地鼠物件######################
pos6 = [[200, 200], [300, 200], [400, 200], [200, 300], [300, 300],
        [400, 300]]  # 模擬地鼠出現的位置
pos = pos6[0]  # 外面記錄圓的位置

######################分數物件######################

######################循環偵測######################
while True:
    clock.tick(30)  # 每秒執行30次

    # 取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(bg, (0, 0))  # 貼上背景
    gophers_update()

    pygame.display.update()