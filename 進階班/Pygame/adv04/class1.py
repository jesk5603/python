######################匯入模組######################
import pygame
import os
import sys
import random


####################定義函式######################
def gophers_update():
    global tick, pos, score, times
    # 每幀循環執行的代碼
    if tick > max_tick:  # 每20次刷新變換一次
        new_pos = random.randint(0, 5)  # 隨機0到5
        pos = pos6[new_pos]  # 更新外部記錄的圓的位置
        tick = 0  # 重置計數器
        times += 1
    else:  # 不刷新變換的時候
        tick += 1  # 增加計數器
    screen.blit(
        gophers,
        (pos[0] - gophers.get_width() / 2, pos[1] - gophers.get_height() / 2))


def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否點擊在指定的區域內"""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


def score_update():
    score_sur = score_font.render(f'score:{score}', False, RED)
    screen.blit(score_sur, (10, 10))


def time_update():
    times_sur = times_font.render(f'times:{times}', False, RED)
    screen.blit(times_sur, (bg_x - 10 - times_sur.get_width(), 10))


def game_over():
    screen.fill(BLACK)
    end_sur = score_font.render(f'Game over~Your Score{score}', False, RED)
    screen.blit(end_sur, (bg_x / 2 - end_sur.get_width() / 2,
                          bg_y / 2 - end_sur.get_height() / 2))


def mouse_update():
    global hammer, hammer_tick
    if hammer == 1:
        if hammer_tick > hammer_max_tick:
            hammer = ham2
            hammer_tick = 0
        else:
            hammer_tick += 1


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()
tick = 0  # 計數器目前值
max_tick = 20  # 設定計數器最大值
bg_img = 'Gophers_BG_800x600 (1).png'
bg = pygame.image.load(bg_img)
######################建立視窗######################
bg_x = bg.get_width()
bg_y = bg.get_height()
screen = pygame.display.set_mode([bg_x, bg_y])  # 設定窗口
pygame.display.set_caption("打地鼠")

######################地鼠物件######################
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450],
        [610, 450]]  # 模擬地鼠出現的位置
pos = pos6[0]  # 外面記錄圓的位置
gophers = pygame.image.load('Gophers150 (1).png')  #地鼠圖片
gophers2 = pygame.image.load('Gophers2_150.png')

######################分數物件######################
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)
#####################滑鼠物件#######################
pygame.mouse.set_visible(False)
ham1 = pygame.image.load('Hammer1.png')
ham2 = pygame.image.load('Hammer2.png')
hammer = ham2
hammer_tick = 0
hammer_max_tick = 5
######################次數物件#####################
times = 0
times_max = 50
typeface = pygame.font.get_default_font()
times_font = pygame.font.Font(typeface, 24)

######################循環偵測######################
while True:
    clock.tick(40)  # 每秒執行30次
    mouse_pos = pygame.mouse.get_pos()
    # 取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        hammer = ham1
        if check_click(mouse_pos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                       pos[1] + 50):
            tick = max_tick + 1  #立即刷新
            score += 1
            times += 1
            hammer = ham2
    if times >= times_max:
        game_over()
    else:
        screen.blit(bg, (0, 0))  # 貼上背景
        gophers_update()
        pygame.draw.circle(screen, BLUE, mouse_pos, 10)
        score_update()
    time_update()
    mouse_update()
    pygame.display.update()