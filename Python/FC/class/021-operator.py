list1 = [679]
list2 = [123]
list3 = [456]
print(list1 > list2 < list3)

list4 = [123, "111"]
# 当列表有多个元素，只比第一个元素
print(list4 > list1)

# and有一方为错则结果为错
print((list1 > list2) and (list2 > list3))

#! 列表只能拼接列表
#! print(list5=list1 + "hi")
list4 = list1 + list2
print(list4)
print(list1 * 3)

# 判断679是否在list1中，有则返回True，否则返回False
print(679 in list1)
# 判断123是否不在list1中，不在则返回True，否则返回False
print(123 not in list1)

# 当列表里有列表时，in只能判断一层
# 需要自己引入进去
test = ["123", ["徐浩冉"], "456"]
print("徐浩冉" in test)
print("徐浩冉" in test[1])
