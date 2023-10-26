def hello():
    print("hello,python")


hello()
hi = hello()
print(hi)
print(type(hi))


def back():
    return [1, "哈哈", 1.1]


# return的返回值在vscode中需要使用print来输出
print(back())


# 不加方括号，默认返回一个元组（用逗号隔开就算是一个元组）
def backo():
    return 1, "哈哈", 1.1


print(backo())
