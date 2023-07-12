import time 
import random
game = random.randint(1,100)
i = 3
while i:
    user = input('请输入1~100的整数：')
    # isdigit判断字符串是否由数字组成
    while not user.isdigit():
        print('抱歉，操作不合法')
        user = input('请重新输入')
    guess = int(user)
    if guess == game:
        print('答对啦~很不错嘛')
        break
    elif guess > game:
        print('猜的有点大喔~')
    else:
        print('猜的有点小喔~')
    i -= 1
time.sleep(1)
print('游戏结束')

