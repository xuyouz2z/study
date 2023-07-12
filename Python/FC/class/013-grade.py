i = 1
while i <= 33:
    user = int(input('请输入成绩（输入888退出）：'))
    if 100 > user >= 90:
        print(f'您的成绩{user}为A（优秀）')
    elif 90 > user >= 80:
        print(f'您的成绩{user}为B（良好）')
    elif 80 > user >= 60:
        print(f'您的成绩{user}为C（合格）')
    elif 60 > user >= 0:
        print(f'您的成绩{user}为D（不合格）')
    elif user == '888':
        break
    else:
        user = input('输入有误，请重新输入：')
i += 1