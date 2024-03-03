import pygame
import sys
import os
from pygame.locals import *
import random
from typing import List


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


class Enemy:
    def __init__(self, x, y, image, shift, burn_img):
        self.x = x
        self.y = y
        self.image = image
        self.active = True
        self.shift = shift
        self.wh = image.get_width() // 2
        self.hh = image.get_height() // 2
        self.burn_shift = 0
        self.burn_img = burn_img
        self.burn_w, self.burn_h = burn_img.get_rect().size
        self.EXP: int = 0
        self.hit = False

    def move(self):
        if self.active:
            self.y += self.shift
            if self.y > bg_y:
                self.reset(*create_enemy(), emy_shift)

    def draw(self, screen):
        if self.active:
            self.burn_shift = (self.burn_shift + 2) % 6
            screen.blit(
                self.burn_img,
                [self.x - self.burn_w / 2, self.y - self.burn_h - self.burn_shift],
            )
            screen.blit(self.image, (self.x - self.wh, self.y - self.hh))

    def reset(self, x, y, image, shift):
        self.x = x
        self.y = y
        self.image = image
        self.active = True
        self.shift = shift
        self.wh = image.get_width() // 2
        self.hh = image.get_height() // 2
        self.EXP = 0
        self.hit = False


class FastMissile(Missile):  # 設定這種飛彈的速度為10,比一般的飛彈快
    def __init__(self, x, y, image, shift):
        super().__init__(x, y, image, shift)
        self.shift += 10


class PiercingMissile(Missile):  # 設定這種飛彈可以穿透敵人
    def __init__(self, x, y, image, shift):
        super().__init__(x, y, image, shift)


class PowerUp:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.wh = image.get_width() / 2
        self.hh = image.get_height() / 2
        self.active = True
        self.type = random.choice([FastMissile, PiercingMissile, Missile])

    def draw(self, screen):
        if self.active:
            self.y += 5
            screen.blit(img_powerup, (self.x - self.wh, self.y - self.hh))
            if self.y > bg_y:
                self.active = False


######################定義函式區######################
def roll_bg():
    global roll_y
    roll_y = (roll_y + 20) % bg_y
    screen.blit(img_bg, [0, roll_y - bg_y])
    screen.blit(img_bg, [0, roll_y])


def is_hit(x1, y1, x2, y2, r):
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 < r**2:
        return True

    else:
        return False


def move_starship():
    global ss_x, ss_y, ss_hh, ss_wh, ss_img, burn_shift, ss_invincible
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
    ss_invincible = max(0, ss_invincible - 1)  # 更新飛船無敵時間
    if ss_invincible % 2 == 0:
        screen.blit(img_burn, [ss_x - burn_w / 2, ss_y + burn_h + burn_shift])
        screen.blit(ss_img, [ss_x - ss_wh, ss_y - ss_hh])


def score_update():
    global score
    score_sur = score_font.render(str(score), True, (255, 0, 0))
    screen.blit(score_sur, [10, 10])


def create_enemy():
    emy_img = random.choice(enemy_show)  # 取得敵機圖片
    emy_wh = emy_img.get_width() // 2  # 取得敵機圖片寬度
    emy_x = random.randint(emy_wh, bg_x - emy_wh)  # 隨機生成敵機位置
    emy_y = random.randint(-bg_y, -emy_wh)  # 隨機生成敵機位置
    return emy_x, emy_y, emy_img  # 回傳敵機位置、敵機圖片


def draw_explode(enemy: Enemy):
    if 0 < enemy.EXP < 6:
        exp_w, exp_h = img_explode[enemy.EXP].get_rect().size
        screen.blit(img_explode[enemy.EXP], [enemy.x - exp_w / 2, enemy.y - exp_h / 2])
        enemy.EXP += 1


def shield_update():
    shield_w = img_shield.get_width() * ss_shield / 100  # 計算保護罩寬度
    shield_h = img_shield.get_height()  # 保護罩高度
    screen.blit(img_shield, [0, bg_y - 40], [0, 0, shield_w, shield_h])


def show_gameover():
    screen.blit(
        img_gg, [bg_x / 2 - img_gg.get_width() / 2, bg_y / 2 - img_gg.get_height() / 2]
    )


######################初始化設定######################
os.chdir(sys.path[0])
pygame.init()
clock = pygame.time.Clock()
gameover = False
img_bg = pygame.image.load("space.png")
######################載入圖片######################
img_bg = pygame.image.load("space.png")
img_sship = [
    pygame.image.load("fighter_M.png"),
    pygame.image.load("fighter_L.png"),
    pygame.image.load("fighter_R.png"),
]
img_burn = pygame.image.load("starship_burner.png")
img_emy_burn = pygame.transform.rotate(img_burn, 180)  # 旋轉180度
img_weapon = pygame.image.load("bullet.png")
img_enemy = pygame.image.load("enemy1.png")
img_enemy2 = pygame.image.load("enemy2.png")
img_explode = [
    None,
    pygame.image.load("explosion1.png"),
    pygame.image.load("explosion2.png"),
    pygame.image.load("explosion3.png"),
    pygame.image.load("explosion4.png"),
    pygame.image.load("explosion5.png"),
]
img_shield = pygame.image.load("shield.png")
img_gg = pygame.image.load("gameover.png")
img_powerup = pygame.image.load("powerup.png")
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
ss_invincible = 0
ss_shield = 100  # 飛船保護罩壽命總共100點
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
enemy_show = [img_enemy, img_enemy2]
emy_shift = 5
emy_list: List[Enemy] = []
emy_num = 10

for i in range(emy_num):
    emy_list.append(Enemy(*create_enemy(), emy_shift, img_emy_burn))
######################音樂設定####################
pygame.mixer.music.load("hit (1).mp3")

######################分數設定####################
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 36)

######################道具列表######################
powerups: List[PowerUp] = []

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
    if gameover:
        show_gameover()
    else:
        roll_bg()
        move_starship()
        msl_cooldown = max(0, msl_cooldown - 1)
        for missie in missiles:
            missie.move()
            missie.draw(screen)
        for emy in emy_list:
            emy.move()
            emy.draw(screen)
            draw_explode(emy)
            for missile in missiles:
                if missile.active and is_hit(
                    missile.x, missile.y, emy.x, emy.y, emy.wh + msl_wh
                ):
                    if emy.hit:
                        break
                    emy.hit = True
                    if not isinstance(missile, PiercingMissile):  # 如果是穿透飛彈
                        missile.active = False
                    emy.active = False
                    score += 1
                    emy.EXP = 1
                    pygame.mixer.music.play()
                    powerups.append(PowerUp(emy.x, emy.y, img_powerup))  # 敵機爆炸時,隨機掉落道具
                    break

            if not emy.active and emy.EXP == 6:
                emy.reset(*create_enemy(), emy_shift)
            if (
                emy.active
                and is_hit(emy.x, emy.y, ss_x, ss_y, emy.wh + ss_wh)
                and ss_invincible == 0
            ):
                ss_invincible = 40
                score -= 1
                ss_shield -= 20

        if ss_shield <= 0:
            gameover = True
            break
    for powerup in powerups:
        powerup.draw(screen)
        if not powerup.active:
            powerups.remove(powerup)
        score_update()
        shield_update()
    pygame.display.update()
