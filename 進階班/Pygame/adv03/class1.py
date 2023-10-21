######################匯入模組######################
import pygame
import random
import sys
import os


####################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否點擊在指定的區域內"""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


def snow_fall():
    """下雪"""
    global x_site, y_site, x_shift, radius
    # 畫出雪花
    pygame.draw.circle(screen, WHITE, (x_site, y_site), radius)

    # 計算雪花下次顯示的座標
    x_site += x_shift
    y_site += radius

    # 如果雪花落出畫面，重設位置
    if y_site > bg_y or x_site > bg_x:
        y_site = random.randint(-10, -1)
        x_site = random.randint(0, bg_x)


####################初始化######################
os.chdir(sys.path[0])  # 設定程式執行路徑
pygame.init()
bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)

bg_x = bg.get_width()  # 640
bg_y = bg.get_height()  # 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

######################建立視窗######################
screen = pygame.display.set_mode((bg_x, bg_y))
pygame.display.set_caption("Snow")

####################撥放音樂######################
mp3_path = "snow-dream.mp3"
pygame.mixer.music.load(mp3_path)  # 音樂載入程式
pygame.mixer.music.play()  # 播放音樂
pygame.mixer.music.fadeout(600000)  # 設定音樂撥放時間單位毫秒
pygame.mixer.music.pause()  # 暫停音樂

####################設定文字######################
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render("Stop", True, BLACK)
tit_w = title.get_width()
tit_h = title.get_height()

####################設定雪花基本參數######################
x_site = random.randrange(0, bg_x)  # 雪花圓心位置
y_site = random.randrange(-10, -1)  # 雪花圓心位置
x_shift = random.randint(-1, 1)  # x 軸偏移量
radius = random.randint(4, 6)  # 半徑和 y下降量

####################新增fps######################
clock = pygame.time.Clock()

######################循環偵測######################
paint = False  # 是否要下雪
cnt = 0  # 計算雪落下的次數

while True:
    clock.tick(20)  # 設定每秒20幀執行

    # 取得滑鼠位置
    mouse_pos = pygame.mouse.get_pos()

    # 取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                paint = not paint

    if cnt > 10:
        # 當雪球落下10次之後，改變下墜方向
        cnt = 0
        x_shift = random.randint(-3, 3)
    else:
        cnt += 1

    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))

    if paint:
        # 當要下雪時撥放音樂，並顯示Start文字按鈕
        title = font.render("Start", True, BLACK)
        pygame.mixer.music.unpause()
        snow_fall()
    else:
        # 當不下雪時暫停音樂，並顯示Stop文字按鈕
        title = font.render("Stop", True, BLACK)
        pygame.mixer.music.pause()  # 暫停音樂

    # 更新繪圖視窗
    pygame.display.update()