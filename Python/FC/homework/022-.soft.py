import random

list1 = []
for i in range(10):
    random_int = random.randint(1, 30)
    list1.append(random_int)
print(f"默认10个随机数{list1}")
# 顺序排序
list1.sort()
print(f"顺序{list1}")
# 倒叙排序
list1.sort(reverse=True)
print(f"倒序{list1}")
