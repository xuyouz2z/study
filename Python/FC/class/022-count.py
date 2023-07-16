import random

# python内置函数dir(list)
list1 = []
for i in range(10):
    random_number = random.randint(0, 100)
    print(random_number)
    list1.append(random_number)
print(list1)
print(list1.count(10))
