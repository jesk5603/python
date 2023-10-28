######################匯入模組######################
import pygame
import sys
import os
from pygame.locals import *


####################定義函式######################
def bg_update():
    global bg_roll_x
    bg_roll_x = (bg_roll_x - 5) % bg_x
    screen.blit(img, (bg_roll_x - bg_x, 0))
    screen.blit(img, (bg_roll_x, 0))


def move_dinosaur():
    global ds_y, ds_index, jumpState, jumpValue
    if jumpState:
        if ds_y >= LIMTT_LOW:
            jumpValue = -jump_height
        if ds_y <= 0:
            jumpValue = jump_height
        ds_y += jumpValue
        if ds_y >= LIMTT_LOW:
            jumpState = False
            ds_y = LIMTT_LOW

    ds_index = (ds_index - 1) % len(img_dinosaur)
    screen.blit(img_dinosaur[ds_index], (ds_x, ds_y))


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
LIMTT_LOW = 140  #地面高度
clock = pygame.time.Clock()
####################載入圖片物件######################
img = pygame.image.load('bg.png')
img_dinosaur = [pygame.image.load('小恐龍1.png'), pygame.image.load('小恐龍2.png')]
bg_x = img.get_width()
bg_y = img.get_height()
bg_roll_x = 0
######################建立視窗######################
screen = pygame.display.set_mode((bg_x, bg_y))
pygame.display.set_caption('Dinosaur')
######################分數物件######################

######################恐龍物件######################
ds_x = 50
ds_y = LIMTT_LOW
ds_index = 0
jumpState = False
jumpValue = 0
jump_height = 13
######################仙人掌物件######################

######################循環偵測######################
while True:

    clock.tick(150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and ds_y <= LIMTT_LOW:
                jumpState = True
    bg_update()
    move_dinosaur()
    pygame.display.update()
