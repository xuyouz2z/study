x, y, z = 6, 5, 4
if x < y:
    small = x
    if z < small:
        small = z
elif y < z:
    small = y
else:
    small = z
# 当x小于y小于z时 返回x 
# 当y小于z时返回y 不然返回z
result = x if (x < y and x < z) else (y if y < z else z)
print(result)