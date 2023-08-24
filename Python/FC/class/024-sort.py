list1 = [2, 4, 1, 4, 6, 7]
# 使用sort()排序，默认为从小到大
list1.sort()
print(list1)
# 可以使用reverse实现反转，即是从大到小
# list1.reverse()
# print(list1)
list1.sort(reverse=True)
print(f"倒叙{list1}")
