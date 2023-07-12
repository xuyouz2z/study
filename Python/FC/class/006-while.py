import time
i = 0
while i!=3:
    guess = int(input('猜猜我是那个数？'))
    if guess==8:
        print('猜对了~挺不错的嘛!')
        break
    elif guess>8:
        print('猜大啦宝贝~')
    else:
        print('猜小咯~，下次努力！')
    i+=1
time.sleep(1)
print('游戏结束')

