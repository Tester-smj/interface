#coding=utf-8

interval = 0


while True:
    if 用户点击了关闭:
        退出
    interval += 1
    if interval == 50:
        interval=0
        小飞机诞生

        
    小飞机移动一个位置
    屏幕刷新

    if 用户鼠标产生了移动：
        我方飞机位置等于鼠标位置
        屏幕刷新

    if 我方飞机和小飞机砰
        我方飞机挂，放音乐
        修改我方飞机图案
        打印 gameover
        停止背景音乐