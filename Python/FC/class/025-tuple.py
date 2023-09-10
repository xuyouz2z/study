tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple1)
# 元组的下标
print(tuple1[2])
# 元组的切片
print(tuple1[1:3])
# 元组的拷贝
tuple2 = tuple1[:]
print(tuple2)
# 查询tuple中包含了几次数字4
print(tuple1.count(4))
# 元组不能修改
# tuple1.append("123")
# tuple1[1] = 3
# 判断是否为元组的关键在于逗号(1,)
# 创建单个元组,不加逗号是int类型
print(type(tuple1))
# 空元组的创建
tuple2 = ()
print(type(tuple2))
# 重复操作符
print(5 * (4,))
# 拼接操作符，两边类型必须一致
print(tuple1[1:5] + tuple1[0:1] + ("python",))
# 删除整个元组
del tuple1
# 元组不支持修改和删除
# del tuple1[0:2]
# print(tuple1)
