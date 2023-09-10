list1 = [1, 2, 1, 9, 7, 4, 6, 11, 99]
list1.append(5)
print(list1)

list2 = [1, 2, 3]
list1.extend(list2)

print(list1)
print(list1.count(0))

list1.remove(1)
print(list1)

list1.pop(6)
print(list1)
# 默认顺序，reverse=True倒叙
list1.sort()
print(list1)

list1.insert(0, 1000)
print(list1)

list2 = list1.copy()
# list2 = list[:]
print(list2)

list2.clear()
print(list2)

list1.reverse()
print(list1)

print(list1.index(1))
