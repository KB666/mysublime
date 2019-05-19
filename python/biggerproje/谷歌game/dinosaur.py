#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-17 12:25:23
# @Author  : ljljlhj (ljljlhj@foxmail.com)
# @Link    : ${link}
# @Version : $Id$

import pygame
from pygame.locals import *

SCREENWEIDTH = 339
SCREENHEIGHT = 223
# 设置屏幕高度和宽度

FPS = 30  # 设置更新时间


# 定义地图类
class MyMap():
    """docstring for """

    def __init__(self, x, y, SCREEN):
        self.bg = pygame.image.load(r'image/bg.png').convert_alpha()
        self.x = x
        self.y = y
        self.SCREEN = SCREEN

    def map_rolling(self):
        # 小于330则地图完全移动完毕
        if self.x < -330:
            self.x = 339
        else:
            self.x -= 3

    def map_draw(self):
        # 更新地图
        self.SCREEN.blit(self.bg, (self.x, self.y))


def mainGmae():
    score = 0  # 记录得分
    over = False
    global FPSLOCK
    pygame.init()  # 初始化pygame
    FPSLOCK = pygame.time.Clock()  # 刷新屏幕的时间锁
    SCREEN = pygame.display.set_mode((SCREENWEIDTH, SCREENHEIGHT))  # 设置屏幕大小
    pygame.display.set_caption('小恐龙')  # 设置窗体标题
    bg1 = MyMap(0, 0, SCREEN)
    bg2 = MyMap(339, 0, SCREEN)
    while True:
        # 判断关闭窗口
        for event in pygame.event.get():
            if event.type == QUIT:
                over = True
                exit()
        if over == False:
            bg1.map_draw()  # 绘制地图起到更新地图的作用
            # 地图移动
            bg1.map_rolling()
            bg2.map_draw()
            bg2.map_rolling()
    # 更新窗口
    pygame.display.update()
    # 多久更新一次
    FPSLOCK.tick(FPS)


if __name__ == '__main__':  # 创建程序入口
    mainGmae()
