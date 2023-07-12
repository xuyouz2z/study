# 数据类型转换

# 整型转字符串类型
a = 1
print(type(str(a)))
print(type(a))

# 浮点转换为整数，会采取截断处理，小数点后的直接砍掉（不是四舍五入）
b = 1.9
print(int(b))

c = 520
# 整型转浮点型则会添加小数点
print(float(c))

# 转换字符串类型
print(str(5e19))
print(str(5e-19))

print(type(False))

# False是否属于bool类型
print(isinstance(False,bool))
print(isinstance(1,str))