list1 = [1, 3, 2, 9, 7, 8]
# 0-2不包含2
print(list1[0:2])
print(list1[-3:-1])
print(list1[0:5:3])
list2 = list1[0:]
print(f"two{list2}")
print(list2[:3])
# 拷贝list2到list3元素中
# list3 = list2[:]
# print(list3)
list3 = list1
print(list3)
