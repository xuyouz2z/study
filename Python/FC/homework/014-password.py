count = 3
password = '888'

while count:
    user = input('请输入密码：')
    if user == password:
        print('密码正确！')
        break
    elif '*' in user:
        print('密码中不能含有"*"号！您还有', count, '次机会！')
        continue
    elif count == 1:
        print('请稍后再试')
    else:
        print('密码输入错误！您还有', count-1, '次机会！')   
    count -= 1
