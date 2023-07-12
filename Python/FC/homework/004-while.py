user = int(input('请输入一个整数'))
i = 1
while i <= user:
    print(user*' ',end='')
    while i:
        print(user*'*')
        i -= 1
    i += 1
    user -= 1
    