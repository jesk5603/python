######################匯入模組######################
import pygame
import sys
import math
######################初始化######################

pygame.init()  # 啟動 pygame
width = 640
height = 320

######################建立視窗及物件######################

screen = pygame.display.set_mode((width, height))  #設定視窗大小
pygame.display.set_caption('game')

######################建立畫布######################

bg = pygame.Surface((width, height))  #建立畫布
bg.fill((255, 255, 255))  #設定顏色
'''畫圓形,(畫布,顏色,圓心,半徑,線寬)'''
# pygame.draw.circle(bg, (0, 0, 0), (300, 150), 100, 0)
# pygame.draw.circle(bg, (255, 255, 255), (300, 150), 30, 0)
'''畫矩形,(畫布,顏色,[X,Y,寬,高],線寬)'''
# pygame.draw.rect(bg, (0, 255, 0), [0, 0, 60, 40], 5)
'''畫橢圓,(畫布,顏色,[X,Y,寬,高],線寬)'''
# pygame.draw.ellipse(bg, (255, 0, 0), [0, 0, 60, 35], 5)
# pygame.draw.ellipse(bg, (255, 0, 0), [0, 0, 60, 35], 5)
'''畫圓形,(畫布,顏色,起點,終點,線寬)'''
# pygame.draw.line(bg, (255, 0, 255), (0, 0), (300, 300), 3)
# pygame.draw.line(bg, (255, 0, 255), (300, 0), (300, 300), 3)
'''畫多邊形(畫布,顏色,[[x1,y1],[x2,y2],[x3,y3]],線寬)'''
pygame.draw.polygon(bg, (255, 0, 0),
                    [[100, 100], [150, 300], [0, 200], [200, 200], [70, 300]],
                    0)
pygame.draw.polygon(bg, (255, 0, 0),
                    [[110, 270], [150, 300], [0, 200], [200, 200], [70, 300]],
                    0)
'''圓弧,(畫布,顏色,[X,Y,寬,高],起始角度,結束角度,線寬)'''
# pygame.draw.arc(bg, (255, 10, 0), [100, 100, 100, 50], math.radians(180),math.radians(0), 2)

######################循環偵測######################
paint = False
color = 255
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #如果按下[X]就退出
            sys.exit()  #離開遊戲
    screen.blit(bg, (0, 0))  #繪製畫布於視窗左上角
    pygame.display.update()  #更新視窗
    if event.type == pygame.MOUSEBUTTONDOWN:  #偵測滑鼠按下
        if event.button == 3:
            color = (255, 0, 0)
        if event.button == 1:
            color = (255, 255, 255)
        print('click')
        print(pygame.mouse.get_pos())  #取得滑鼠座標
        paint = not (paint)

    if paint:
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(bg, color, (x, y), 5, 0)

    screen.blit(bg, (0, 0))  #繪製畫布於視窗左上角
    pygame.display.update()  #更新視窗
