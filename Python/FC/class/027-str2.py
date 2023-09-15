str1 = "ABC"

# 如果字符串中只包含十进制数则返回True，否则返回False
str2 = str1.isdecimal()
print(str2)

# 如果字符串中只包含数字则返回True，否则返回False
str3 = str1.isdigit()
print(str3)

# 如果字符串中包含一个区分大小写的，并且该字符串都是小写则返回True，否则返回False
str4 = str1.islower()
print(str4)

# 如果字符串中只包含数字‘字符’则返回True，否则返回False
str5 = str1.isnumeric()
print(str5)

# 如果字符串中只包含空格则返回True，否则返回False
str6 = str1.isspace()
print(str6)

# 如果字符是标题化（开头字母大写，其余都是小写）则返回True，否则返回False
str7 = str1.istitle()
print(str7)
# 返回标题化（开头字母大写，其余都是小写）字符串
str8 = str1.title()
print(str8)
