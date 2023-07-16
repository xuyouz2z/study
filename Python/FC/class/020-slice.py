list1 = [1, 2, 3, 4, 5, 6]
print(list1[0:3])

# 切片是单独取出，不影响原列表
# 取出0-3的下标-运行结果:123

# 起始位置-截至位置-步长
print(list1[0:1:2])

# 0-~全部列表
list2 = list1[0:]
print(f"two{list2}")
# ~-3取到下标=3
print(list2[:3])

# 拷贝list2到list3元素中
# list3 = list2[:]
# print(list3)
list3 = list1
print(list3)
