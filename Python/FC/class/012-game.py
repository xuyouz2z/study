aircraft = 1
while True:
    if 用户是否点击关闭按钮:
        # 退出程序
        break
    aircraft += 1
    if aircraft == 50:
        aircraft = 0
    小飞机移动位置
    刷新界面
    elif 用户鼠标产生移动:
        我方飞机中心位置=鼠标位置
        屏幕刷新
    elif 发生冲突:
        我方挂，播放音乐
        修改飞机图案
        打印gave Over
        停止音乐（time=2s？）

