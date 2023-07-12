list1 = ["apple", "banana", "orange", "shaddock"]
list1.append(88)
list1.insert(1, 88)
list1.insert(3, 90)
list1.insert(5, 85)
print(list1)
# for i in list1:
#     print(i,end='')

# count = 0
# lenth = len(list1)
# while count < lenth:
#     print(list1[count],list1[count+1])
#     count += 2

for i in range(len(list1)):
    if i % 2 == 0:
        print(list1[i], list1[i + 1])
