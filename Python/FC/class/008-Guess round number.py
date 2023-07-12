import time 
import random
game = random.randint(1,100)
i = 3
while i:
    user = int(input('请输入1~100的整数：'))
    if user == game:
        print('答对啦~很不错嘛')
        break
    elif user > game:
        print('猜的有点大喔~')
    else:
        print('猜的有点小喔~')
    i -= 1
time.sleep(1)
print('游戏结束')

