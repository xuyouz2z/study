# 收集参数


def test(*str):
    print("参数的长度是", len(str))
    print("第二个参数是", str[1])


test(1, 2, 3, 4, 5, 6)


def test1(*str, name):
    print("参数的长度是", len(str))
    print("第二个参数是", str[1])
    print("定制参数？", name)


#! 如果收集参数后要加入定制参数，需要用关键字参数，不然全部列为收集参数
#! test1(1, 2, 3)
test1(1, 2, name=3)
