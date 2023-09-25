# 十进制转二进制
def ten2two(x):
    result = ""
    list1 = list()
    while x // 2 != 0:
        list1.append(x % 2)
        x //= 2
    else:
        list1.append(x % 2)
    while list1:
        result += str(list1.pop())
    return result


print(ten2two(5))
