# red = 3
# yellow = 3
# green = 6
sum = 0
for red in range(1,4):
    for yellow in range(1,4):
        for green in range(1,7):
            if red + yellow + green == 8:
                sum += 1
                print(red,yellow,green)
print(f'一共有{sum}种颜色搭配')