str1 = "  pytHon"
x = "1", "2", "3", "5"

# 以字符串为分隔符，插入到x中
str_new = str1.join(x)
print(str_new)

# 使用-来填充一个长度为20的居中新字符串
print(str1.center(20, "-"))
# 使用-来填充一个长度为20的左对齐新字符串
print(str1.ljust(20, "-"))
# 使用-来填充一个长度为20的右对齐新字符串
print(str1.rjust(20, "-"))

# 转换字符串中的大写变小写
print(str1.lower())

# 去除该字符串左边的所有空格
# print(str1.lstrip())
str__ = str1.lstrip()

# 去除该字符串末尾的所有空格
str_nnew = str1 + "666   "
str__ = str_nnew.rstrip()
print(str__)

# 把该字符串分为3个元组('  p', 'y', 'tHon')
str_ = str1.partition("y")
print(str_)

# 从右边查找
# 把该字符串分为3个元组('  p', 'y', 'tHon')
str_ = str1.rpartition("y")
print(str_)

# 将is替换为IS，如果有count指定，则替换不超过count次
# 注意 replace 不会改变原 string 的内容
temp_str = "this is a test"
print(temp_str.replace("is", "IS"))
print(temp_str)
