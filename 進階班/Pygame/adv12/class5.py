import pygame
import sys
import os
from pygame.locals import *
import random


######################載入套件######################
######################物件類別######################
class Missile:
    def __init__(self, x, y, image, shift):
        self.x = x
        self.y = y
        self.image = image
        self.active = False
        self.shift = shift

    def launch(self, x, y):
        if not self.active:
            self.x = x
            self.y = y
            self.active = True

    def move(self):
        if self.active:
            self.y -= self.shift
            if self.y < 0:
                self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))


class Enermy:
    def __init__(self, x, y, image, shift):
        self.x = x
        self.y = y
        self.image = image
        self.active = True
        self.shift = shift
        self.wh = image.get_width() // 2
        self.hh = image.get_height() // 2

    def move(self):
        if self.active:
            self.y += self.shift
            if self.y > bg_y:
                self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, (self.x - self.wh, self.y - self.hh))

    def reset(self, x, y, image, shift):
        self.x = x
        self.y = y
        self.image = image
        self.active = True
        self.shift = shift
        self.wh = image.get_width() // 2
        self.hh = image.get_height() // 2


######################定義函式區######################
def roll_bg():
    global roll_y
    roll_y = (roll_y + 20) % bg_y
    screen.blit(img_bg, [0, roll_y - bg_y])
    screen.blit(img_bg, [0, roll_y])


def move_starship():
    global ss_x, ss_y, ss_hh, ss_wh, ss_img, burn_shift
    ss_img = img_sship[0]
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        ss_y -= 20
    if key[pygame.K_DOWN]:
        ss_y += 20
    if key[pygame.K_LEFT]:
        ss_x -= 20
        ss_img = img_sship[1]
    if key[pygame.K_RIGHT]:
        ss_x += 20
        ss_img = img_sship[2]
    ss_hh = ss_img.get_height() / 2
    ss_wh = ss_img.get_width() / 2
    if ss_y < ss_hh:
        ss_y = ss_hh
    if ss_y > bg_y - ss_hh:
        ss_y = bg_y - ss_hh
    if ss_x < ss_wh:
        ss_x = ss_wh
    if ss_x > bg_x - ss_wh:
        ss_x = bg_x - ss_wh
    burn_shift = (burn_shift + 2) % 6
    screen.blit(img_burn, [ss_x - burn_w / 2, ss_y + burn_h + burn_shift])
    screen.blit(ss_img, [ss_x - ss_wh, ss_y - ss_hh])


def create_enemy():
    emy_img = random.choice(enemy_show)  # 取得敵機圖片
    emy_wh = emy_img.get_width() // 2  # 取得敵機圖片寬度
    emy_x = random.randint(emy_wh, bg_x - emy_wh)  # 隨機生成敵機位置
    emy_y = random.randint(-bg_y, -emy_wh)  # 隨機生成敵機位置
    return emy_x, emy_y, emy_img  # 回傳敵機位置、敵機圖片


######################初始化設定######################
os.chdir(sys.path[0])
pygame.init()
clock = pygame.time.Clock()

img_bg = pygame.image.load("space.png")
######################載入圖片######################
img_bg = pygame.image.load("space.png")
img_sship = [
    pygame.image.load("fighter_M.png"),
    pygame.image.load("fighter_L.png"),
    pygame.image.load("fighter_R.png"),
]
img_burn = pygame.image.load("starship_burner.png")
img_weapon = pygame.image.load("bullet.png")
img_enemy = pygame.image.load("enemy1.png")
img_enemy2 = pygame.image.load("enemy2.png")
enemy_show = [img_enemy, img_enemy2]

######################遊戲視窗設定######################
bg_x = img_bg.get_width()
bg_y = img_bg.get_height()
bg_size = (bg_x, bg_y)
pygame.display.set_caption("Galaxy Lancer")
screen = pygame.display.set_mode(bg_size)
roll_y = 0
######################玩家設定######################
ss_x = bg_x / 2
ss_y = bg_y / 2
ss_wh = img_sship[0].get_width() / 2
ss_hh = img_sship[0].get_height() / 2
ss_img = img_sship[0]
burn_shift = 0
burn_w, burn_h = img_burn.get_rect().size
####################飛彈設定######################
msl_wh = img_weapon.get_width() / 2
msl_hh = img_weapon.get_height() / 2
msl_shift = 30
Missile_MAX = 10
missiles = [Missile(0, 0, img_weapon, msl_shift) for _ in range(Missile_MAX)]
msl_cooldown = 0
msl_cooldown_max = 10
missie = Missile(0, 0, img_weapon, 30)
#####################敵機設定#####################
emy_shift = 5
emy_shift2 = 10
enemy = Enermy(*create_enemy(), emy_shift)
enemy2 = Enermy(*create_enemy(), emy_shift2)

######################主程式######################
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F1:
                screen = pygame.display.set_mode(bg_size, FULLSCREEN)
            elif event.key == K_ESCAPE:
                screen = pygame.display.set_mode(bg_size)
            if event.key == K_SPACE and msl_cooldown == 0:
                for missie in missiles:
                    if not missie.active:
                        missie.launch(ss_x - msl_wh, ss_y - msl_hh)
                        msl_cooldown = msl_cooldown_max
                        break
    roll_bg()
    move_starship()
    msl_cooldown = max(0, msl_cooldown - 1)
    for missie in missiles:
        missie.move()
        missie.draw(screen)
    enemy.move()
    enemy.draw(screen)
    if not enemy.active:
        enemy.reset(*create_enemy(), emy_shift)
    enemy2.move()
    enemy2.draw(screen)
    if not enemy2.active:
        enemy2.reset(*create_enemy(), emy_shift)
    pygame.display.update()
