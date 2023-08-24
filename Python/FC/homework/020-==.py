list1 = [3, 7, 9, 4, 5]
list1.sort(reverse=True)
print(f"list1的元素有{list1}")
# 进行备份
list2 = list1[:]
print(f"list2的元素备份{list2}")
# 墙头草list3~
list3 = list1
print(list3)
list1.sort()
print(
    f"""此时list1等于{list1}
list2[:]的元素有{list2}
list3的备份？{list3}"""
)
