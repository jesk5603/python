######################匯入模組######################
import pygame
import os
import sys
import random


####################定義函式######################
def gophers_update():
    """更新地鼠"""
    global tick, pos, times, gophers_tick, histur  # 使用全域變數
    if tick > max_tick:  # 每20次刷新變換一次
        new_pos = random.randint(0, 5)  # 隨機0到5
        pos = pos6[new_pos]  # 更新外部記錄的圓的位置
        tick = 0  # 重置計數器
        times += 1  # 次數加1
    else:  # 不刷新變換的時候
        tick += 1  # 增加計數器
    if histur == gophers2:
        if gophers_tick > gophers_max_tick:
            histur = gophers
            gophers_tick = 0
        else:
            gophers_tick += 1
    screen.blit(
        histur,
        (pos[0] - gophers.get_width() / 2, pos[1] - gophers.get_height() / 2))


def score_update():
    """更新分數"""
    score_sur = score_font.render(str(score), False, RED)  # 分數文字渲染
    screen.blit(score_sur, (10, 10))  # 將分數文字貼到視窗上


def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否點擊在指定的區域內"""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


def times_update():
    """更新次數"""
    times_sur = times_font.render(str(times), True, RED)  # 次數文字渲染
    screen.blit(times_sur,
                (bg_x - times_sur.get_width() - 10, 10))  # 將次數文字貼到視窗的右上角


def game_over():
    """遊戲結束"""
    screen.fill(BLACK)
    end_sur = score_font.render(f"Game Over~ Your Score is:{score}", False,
                                RED)
    screen.blit(end_sur, (bg_x / 2 - end_sur.get_width() / 2,
                          bg_y / 2 - end_sur.get_height() / 2))


def mouse_update():
    global hammer, hammer_tick

    if hammer == ham1:
        if hammer_tick > hammer_max_tick:
            hammer = ham2
            hammer_tick = 0
        else:
            hammer_tick += 1

    screen.blit(hammer,
                (mouse_pos[0] - 15, mouse_pos[1] - 15))  # 讓鎚子的中心點在滑鼠的位置


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()
tick = 0  # 計數器目前值
max_tick = 20  # 設定計數器最大值
bg_img = "Gophers_BG_800x600.png"
bg = pygame.image.load(bg_img)

bg_x = bg.get_width()
bg_y = bg.get_height()

######################建立視窗######################
screen = pygame.display.set_mode([bg_x, bg_y])  # 設定窗口
pygame.display.set_caption("打地鼠")

######################地鼠物件######################
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450],
        [610, 450]]  # 六個位置
pos = pos6[0]  # 外面記錄圓的位置
gophers = pygame.image.load("Gophers150.png")  # 地鼠圖片
gophers2 = pygame.image.load('Gophers2_150.png')
histur = gophers
gophers_tick = 0
gophers_max_tick = 5
######################分數物件######################
score = 0  # 分數計數
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)

######################次數物件######################
times = 0  # 次數計數
times_max = 5  # 地鼠出現最大次數
typeface = pygame.font.get_default_font()
times_font = pygame.font.Font(typeface, 24)

######################滑鼠物件######################
pygame.mouse.set_visible(False)  # 隱藏滑鼠
ham1 = pygame.image.load("Hammer1.png")  # 鎚子圖片
ham2 = pygame.image.load("Hammer2.png")  # 鎚子圖片
hammer = ham2  # 設定目前要顯示的鎚子圖片
hammer_tick = 0  # 計數器目前值
hammer_max_tick = 5  # 設定計數器最大值
######################聲音物件######################
pygame.mixer.music.load('hit.mp3')
######################循環偵測######################
while True:
    clock.tick(30)  # 每秒執行30次
    mouse_pos = pygame.mouse.get_pos()

    # 取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            hammer = ham1
            if check_click(mouse_pos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                if times < times_max:
                    tick = max_tick + 1  # 立即刷新
                    score += 1  # 分數加1
                    histur = gophers2
                    pygame.mixer.music.play()
    if times >= times_max:  # 次數用完
        game_over()  # 遊戲結束
    else:  # 次數還沒用完
        screen.blit(bg, (0, 0))  # 將背景貼到視窗上
        gophers_update()  # 更新地鼠
        # pygame.draw.circle(screen, BLUE, mouse_pos, 10)  # 在滑鼠位置畫一個圓
        score_update()  # 更新分數
        times_update()  # 更新次數
        mouse_update()  # 更新滑鼠

    pygame.display.update()