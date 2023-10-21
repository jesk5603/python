######################匯入模組######################
import pygame
import sys

####################初始化######################
pygame.init()  # 啟動 Pygame
width = 640
height = 320

######################建立視窗######################
screen = pygame.display.set_mode((width, height))  # 建立繪圖視窗
pygame.display.set_caption("My Game")  # 繪圖視窗標題

######################建立畫布######################
bg = pygame.Surface(screen.get_size())  # 建立畫布
bg.fill((255, 255, 255))  # 畫布為白色

######################繪製圖形######################
# 畫圓形, (畫布, 顏色, 圓心, 半徑, 線寬)
pygame.draw.circle(bg, (0, 0, 255), (200, 100), 30, 0)
pygame.draw.circle(bg, (0, 0, 255), (400, 100), 30, 0)

# 畫矩形, (畫布, 顏色, [x, y, 寬, 高], 線寬)
pygame.draw.rect(bg, (0, 255, 0), [270, 130, 60, 40], 5)

# 畫橢圓, (畫布, 顏色, [x, y, 寬, 高], 線寬)
pygame.draw.ellipse(bg, (255, 0, 0), [130, 160, 60, 35], 5)
pygame.draw.ellipse(bg, (255, 0, 0), [400, 160, 60, 35], 5)

# 畫線, (畫布, 顏色, 起點, 終點, 線寬)
pygame.draw.line(bg, (255, 0, 255), (280, 220), (320, 220), 3)

# 畫多邊形, (畫布, 顏色, [[x1, y1], [x2, y2], [x3, y3]], 線寬)
# pygame.draw.polygon(bg, (100, 200, 45), [[100, 100], [0, 200], [200, 200]], 0)

# 畫圓弧, (畫布, 顏色, [x, y, 寬, 高], 起始角度, 結束角度, 線寬)
# pygame.draw.arc(bg, (255, 10, 0), [100, 100, 100, 50], math.radians(180), math.radians(0), 2)

######################循環偵測######################
paint = False  # 繪圖狀態
color = (0, 255, 255)  # 繪圖顏色
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 使用者按關閉鈕
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:  # 偵測滑鼠按下
            if event.button == 1:  # 左鍵
                color = (255, 0, 0)
            if event.button == 3:  # 右鍵
                color = (255, 255, 255)
            print("click!!")
            print(pygame.mouse.get_pos())  # 取得滑鼠座標
            paint = not (paint)  # 切換繪圖狀態

    if paint:  # 繪圖狀態
        x, y = pygame.mouse.get_pos()  # 取得滑鼠座標
        pygame.draw.circle(bg, color, (x, y), 10, 0)  # 跟著滑鼠畫圓，左鍵紅色，右鍵白色

    screen.blit(bg, (0, 0))  # 繪製畫布於視窗左上角
    pygame.display.update()  # 更新視窗