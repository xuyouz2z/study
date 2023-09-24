list1 = [55, 34, 21, 1, 8, 5, 3, 2, 1, 1]
list1.append("xu")
sum_num = []
print(list1)
for i in list1:
    if type(i) == str:
        continue
    sum_num.append(i)
print(sum(sum_num))
# print(type(list1[10]))
