# find函数 str.find('x')
# 检测字符串中是否包含x数据，如果有则返回对应索引值（下标？）
# 没有则返回-1


str1 = "xuyouz2z"
# 检测str1是否包含z2z,包含则返回对应索引值
str2 = str1.find("z2z")
print(str1[str2:])
# 检测str1是否包含str,不包含则返回-1
print(str1.find("str"))
print(str1.find("z2z", 0, 2))
