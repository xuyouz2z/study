def shuixianhua(max):
    print("请输入100-xxx的水仙花数量")
    for i in range(100, max):
        a = int(i / 100)
        b = int(i % 100 / 10)
        c = int(i % 10)
        # 计算a,b,c的三次方的和
        if i == (a**3 + b**3 + c**3):
            print(i)


shuixianhua(int(input("请输入最大值的水仙花数量100-?")))
