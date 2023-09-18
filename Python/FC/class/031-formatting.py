print("{0} {1} you".format("i", "love"))
print("{a} {b} you".format(a="i", b="love"))
print("\ta and \\")
print("{{0}}".format("不打印"))
# 保留一位小数点(四舍五入)
print(f"{27.658:.1f}GB")
#
print(f"hello\npython")

# 用指定字符填充（^居中 <左填充 >右填充）
name = "遥遥领先"
print(f"{name:-^20}")
print(f"{name:-<20}")
print(f"{name:->20}")

# 格式化字符及其ASCII码
print("%c" % 97)
print("%c %c %c" % (97, 98, 99))
# 格式化字符串
print("%s" % "xuhaorna")
# 格式化整数
print("%d +%d =%d" % (1.2, 3, 1.2 + 3))
# 格式化无符号八进制数
print("%o" % 10)
# 格式化无符号十六进制数
print("%x" % 12)
# 格式化无符号十六进制数（大写）
print("%X" % 10)
# 格式化定点数，可指定小数点后的精度(默认6位)
print("%f" % 27.658)
# m.n(m是最小总宽度，n是小数点后边的位数)
print("%.2f" % 27.658)
print("%12.1f" % 27.658)
# 用科学计数法格式化定点数
print("%e" % 27.658)
# 作用同%e，用科学计数法格式化定点数
print("%E" % 27.658)
# 根据值的大小决定使用%f或者%e
print("%g" % 274898498.658)
# 根据值的大小决定使用%F或者%E
print("%e" % 27.658)
# "+"在正数前边增加+号
print("%+d" % 10)
#! 助记符#
print("%#o" % 10)
print("%#x" % 10000)
# 用0取代空格
print("%010d" % 20)
