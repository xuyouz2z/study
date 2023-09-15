# 从右边开始查找
str1 = "  pyt Hon"

# 检测某参数是否在该字符串中，有则返回第一个元素的索引值，没有则返回-1
print(str1.rfind("y"))
# 检测某参数是否在该字符串中，有则返回第一个元素的索引值，没有则异常substring not found
print(str1.rindex("y"))

# 不带参数默认以空格为分隔符,返回一个列表
list1 = str1.split()
print(list1)

# 按照\n分割，返回一个列表
str2 = "p\nython"
list2 = str2.splitlines()
print(list2)

# 判断是否以该参数开头，是则返回True，否则返回False,可选范围
str3 = str1.startswith(" ")
print(str3)

# 删除前后空格， 中间空格不影响 可选删除内容
str_new = "xx  hello python   xx"
print(str_new.strip("x"))

# 反转字符中的大小写
str4 = str1.swapcase()
print(str4)
# 反转字符中小写换大写
str5 = str1.upper()
print(str5)

# 返回长度为20的字符串，原字符串右对齐，用0补充
str6 = str1.zfill(20)
print(str6)
