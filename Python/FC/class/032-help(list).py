# print(help(list))
a = list()
print(a)
b = "xuhaoran"
print(list(b))
# 斐波那契数列
c = (1, 1, 2, 3, 5, 8, 1, 21, 34, 55)
print(list(c))
# 返回参数里的最大值
print(max(c))
# ASCII的最大值
print(max(b))
# 返回参数里的最小值
print(min(c))
#! 要注意的是使用mix和min的前提是每个值都同一个类型
# 返回参数里的总和(6为可选值)
print(sum(c))
print(sum(c, 6))
# sorted默认从小到大
print(sorted(c))
# reversed返回的是一个迭代器对象
print(reversed(c))
# 也可以转换为一个对象
print(list(reversed(c)))
print(tuple(reversed(c)))
# enumerate 转换为元组，组合为一个索引序列，同时列出数据下标和数据
print(enumerate(c))
# 2下标起始位置
print(list(enumerate(c, 2)))
# zip 将两个对象打包为为一个元组类型
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [3, 7, 9, 5, 6]
print(tuple(zip(list1, list2)))
