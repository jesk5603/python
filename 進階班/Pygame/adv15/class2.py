######################載入套件######################
from typing import List
import pygame
import sys
import os
from pygame.locals import *
import random


######################物件類別######################
class Brick:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hit = False

    def draw(self, screen):
        if not self.hit:
            pygame.draw.rect(screen, self.color, self.rect)


######################定義函式區######################
def text_update():
    """顯示文字"""
    bricks_num = number_font.render(str(len(bricks)), True, RED)
    life_num = life_font.render(str(life), True, BLUE)
    screen.blit(bricks_num, [10, 10])
    screen.blit(life_num, [bg_x - 30, 10])


def is_hit(x, y, boxRect):
    """矩形碰撞判斷"""
    return (
        boxRect[0] <= x <= boxRect[0] + boxRect[2]
        and boxRect[1] <= y <= boxRect[1] + boxRect[3]
    )


def reset_game():
    """重置遊戲"""
    global dx, dy, act, life, game_over

    game_over = False
    life = 3
    act = False
    dx = 8
    dy = -8
    bricks.clear()
    for i in range(TOTAL_BLOCK):
        r = random.randint(100, 200)
        g = random.randint(100, 200)
        b = random.randint(100, 200)
        x = (i % bricks_row) * (brick_w + bricks_gap) + 70
        y = (i // bricks_row) * (brick_h + bricks_gap) + 60
        brick = Brick(x, y, 58, 16, (r, g, b))
        bricks.append(brick)


def paddle_update():
    """底板設定"""
    global dy

    paddly_rect = [paddle_x, paddle_y, paddle_w, paddle_h]

    if is_hit(ball_x, ball_y, paddly_rect) and dy > 0:
        """當球往下碰到底板時，才能反彈"""
        dy = -dy

    pygame.draw.rect(screen, RED, paddly_rect)


def ball_update():
    """球設定"""
    global ball_x, ball_y, dx, dy, act, life

    if act == False:
        ball_x = paddle_x + paddle_w // 2
        ball_y = paddle_y - ball_radius
    else:
        ball_x += dx
        ball_y += dy

        if ball_y > paddle_y + ball_radius:
            life -= 1
            act = False

        if ball_x > bg_x - ball_diameter or ball_x < ball_diameter:  # 球碰到右牆或左牆
            dx = -dx

        if ball_y < ball_diameter:  # 球碰到上牆
            dy = -dy

    pygame.draw.circle(screen, ball_color, [ball_x, ball_y], ball_radius)


def show_game_over():
    screen.blit(img_gg, ((bg_x - gg_w) / 2, (bg_y - gg_h) / 2))


######################初始化設定######################
os.chdir(sys.path[0])
pygame.init()
pygame.mouse.set_visible(False)  # 隱藏滑鼠

BLACK = (0, 0, 0)  # 黑色
WHITE = (255, 255, 255)  # 白色
RED = (255, 0, 0)  # 紅色
BLUE = (0, 0, 255)  # 藍色

clock = pygame.time.Clock()  # 設定FPS
act = False  # 是否開始遊戲
life = 3  # 生命值

######################載入圖片######################
img_gg = pygame.image.load("gameover.png")

######################遊戲視窗設定######################
bg_x = 800
bg_y = 600
bg_size = (bg_x, bg_y)
pygame.display.set_caption("打磚塊遊戲")
screen = pygame.display.set_mode(bg_size)

######################磚塊######################
bricks_row = 11
bricks_col = 9
TOTAL_BLOCK = bricks_row * bricks_col
brick_w = 58
brick_h = 16
bricks_gap = 2
bricks: List[Brick] = []
for i in range(TOTAL_BLOCK):
    r = random.randint(100, 200)
    g = random.randint(100, 200)
    b = random.randint(100, 200)
    x = (i % bricks_row) * (brick_w + bricks_gap) + 70
    y = (i // bricks_row) * (brick_h + bricks_gap) + 60
    brick = Brick(x, y, 58, 16, (r, g, b))
    bricks.append(brick)


######################顯示文字設定######################
typeface = pygame.font.get_default_font()
number_font = pygame.font.Font(typeface, 36)
life_font = pygame.font.Font(typeface, 36)

######################底板設定######################
paddle_x = 0
paddle_y = bg_y - 48
paddle_w = 100
paddle_h = 10

######################球設定######################
ball_radius = 8  # 半徑
ball_x = paddle_x + paddle_w // 2  # 球的初始位置
ball_y = paddle_y - ball_radius  # 球的初始位置
ball_diameter = ball_radius * 2  # 直徑
ball_color = WHITE
dx = 8  # 球的移動速度
dy = -8  # 球的移動速度
######################遊戲結束設定######################
game_over = False
gg_w = img_gg.get_width()
gg_h = img_gg.get_height()

######################主程式######################
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            paddle_x = pygame.mouse.get_pos()[0] - 50  # 以滑鼠的中心點為底板的中心點
        if event.type == pygame.MOUSEBUTTONDOWN:
            if act == False:
                act = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE and game_over:
                reset_game()

    if game_over:
        show_game_over()
    else:
        screen.fill(BLACK)
        for brick in bricks:
            if is_hit(ball_x, ball_y, brick.rect):
                brick.hit = True
                dy = -dy
            brick.draw(screen)
        bricks = [brick for brick in bricks if not brick.hit]

        text_update()
        paddle_update()
        ball_update()

        if life <= 0:
            game_over = True

    pygame.display.update()
