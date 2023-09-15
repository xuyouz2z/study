print(r"C:\windows\temp\readme.txt", "r")

str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
str2 = "www.fishc.com"
str3 = str1.index("www.fishc.com")
print(f"该网址的初始下标是第{str3}位")
len_fishc = len(str2)
print(f"该网址的下标有{len_fishc}位")
print(str1[16 : (16 + len_fishc)])

print(str1[-45:-32])

# 左边位置在右边的位置的左侧，否则输出为空
print(str1[-5:59])

str1 = "i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99"
# 从0下标开始输出，不包含第三个
print(str1[::3])
