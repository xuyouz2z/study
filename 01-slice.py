# [起始位置:结束位置:步长]
# 步长表示选取间隔，也可以选择不使用


str1 = "xuyouz2z"
# 0=>2  x=>u
print(str1[0:2])
# 选取xuyouz2z中的0=x   =>5=z   间隔2
print(str1[0:5:2])
# 结果为 0 2 4 ~ 也就是xyu
#! 切片是包头不包尾
#! 结束位不包含结束位本身
print(str1[0:7])

# 其他方法
# 全部
print(str1[0:])
# 取出z2z
print(str1[5:8])
