str1 = "python"
str2 = "PYTHON"
print(str1[:2])
str_new = str1[:2] + "插入" + str1[2:]
print(str_new)


# 将字符串第一个字符串变为大写
str1A = str1.capitalize()
print(str1A)

# 将字符串全部字符换为小写
str2A = str2.casefold()
print(str2A)

# 查找该字符串中某些元素出现的次数
str3 = str1.count("pyth")
print(str3)

# 检查该字符串是否以y结尾，是返回True否则返回False
print(str1.endswith("y", 1, 2))

# 检测某参数是否在该字符串中，有则返回第一个元素的索引值，没有则返回-1
str4 = str1.find("y", 0, 2)
print(str4)
print(str1[str4:])

# 检测某参数是否在该字符串中，有则返回第一个元素的索引值，没有则异常substring not found
str4 = str1.index("t")
print(str4)

# 如果字符串中有一个字符，并且所有字符都是字母或数字，返回True，否则返回Fals
# 如果字符串中有一个字符，并且所有字符都是字母，返回True，否则返回Fals
str5 = str1.isalnum()
print(str5)
str6 = str1.isalpha()
print(str6)
