######################匯入模組######################
import pygame
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

####################設定文字######################
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render("Stop", True, BLACK)
tit_w = title.get_width()
tit_h = title.get_height()

####################設定雪花基本參數######################

####################新增fps######################
clock = pygame.time.Clock()

######################循環偵測######################
paint = False  # 是否要下雪

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

    if paint:
        title = font.render("Start", True, BLACK)
    else:
        title = font.render("Stop", True, BLACK)

    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    # 更新繪圖視窗
    pygame.display.update()