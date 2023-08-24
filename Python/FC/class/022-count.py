import random

# 查看python内置函数dir(list)
list1 = []
for i in range(10):
    random_number = random.randint(0, 30)
    # print(random_number)
    list1.append(random_number)
print(list1)
# 判断10在list1列表中出现了几次（count）
print(list1.count(10))
list2 = list1.index(1, 0, 10)
# 0是起始位置，10是末尾，查询1（index）
print(list2)
