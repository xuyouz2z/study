list1 = ["apple", "banana", "orange"]
print(list1[0])
temp = list1[0]
list1[0] = list1[1]
list1[1] = temp
print(list1)
list1.remove("apple")
print(list1)
del list1[1]
print(list1)
list2 = ["max", "mix"]
list1.extend(list2)
print(list1)
list1
print(list1.pop(0))
p1 = list1.pop()
print(p1)
print(list1)
