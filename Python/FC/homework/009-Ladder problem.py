i = 1
while i:
    if i%2==1 and i%3==2 and i%5==4 and i%6==5 and i%7==0:
        print(f'一共有{i}阶梯')
        break
    i += 1
