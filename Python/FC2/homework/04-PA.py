def MyFirstFunction(name):
    """函数定义过程中的name叫做形参,因为他只是一个形式，占据一个参数"""
    print(f"传递进来的{name}是实参")


MyFirstFunction("徐某")
# 查看函数文档
print(MyFirstFunction.__doc__)
# 也可以使用help来查看
help(MyFirstFunction)


def xu(name, tel):
    print(name + tel)


xu("徐某", "123456")
# 可以使用关键字
xu(tel="123456", name="徐某")


def x(name="徐", tel="123456"):
    print(name + tel)


x()
x(name="徐某人")
