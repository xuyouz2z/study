def count(*param):
    length = len(param)
    for i in range(length):
        zimu = 0
        shuzi = 0
        kongge = 0
        qita = 0
        for each in param[i]:
            if each.isalpha():
                zimu += 1
            elif each.isdigit():
                shuzi += 1
            elif each == " ":
                kongge += 1
            else:
                qita += 1
        print(f"字母有{zimu}个，数字有{shuzi}个，空格有{kongge}个，其他有{qita}个")


count("i love you 123 .")
