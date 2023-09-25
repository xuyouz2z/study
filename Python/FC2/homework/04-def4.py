#   a) 计算打印所有参数的和乘以基数（base=3）的结果
#   b) 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算。
def homework(*num, base=3):
    sum = 0
    for i in num:
        sum += i

    sum *= base

    print(f"结果是{sum}")


homework(1, 2, 3, base=5)
