def love(var):
    var = 1314
    print(var, end="")


var = 520
love(var)
print(var)

varr = "hi"


def fun1():
    global varr
    varr = "baby "
    return fun2(varr)


def fun2(varr):
    varr += "i love you"
    fun3(varr)
    return varr


def fun3(varr):
    varr = "xhr"


print(fun1())
