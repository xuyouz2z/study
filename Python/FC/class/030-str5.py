# 转换字符串中的字符
temp_str = "this is a test"
print(temp_str.translate(str.maketrans("i", "n")))
# 返回i和n的ASCII码（字典类型）
print(str.maketrans("i", "n"))
