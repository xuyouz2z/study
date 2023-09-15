fuhao = r"""`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>"""
zimu = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
shuzi = "0123456789"
passwd = input("请输入要检测的密码组合：")
passwd_len = len(passwd)
#
while passwd.isspace() or passwd == 0:
    passwd = input("您输入的密码为空，请重新输入：")
# 初级密码
if passwd_len <= 8:
    passwd_len = 1
# 中级密码
elif 8 < passwd_len < 16:
    passwd_len = 2
# 高级密码
else:
    passwd_len = 3
con = 0

# 遍历符号、字母以及数字。
for i in passwd:
    if i in fuhao:
        con += 1
        break
for i in passwd:
    if i in zimu:
        con += 1
        break
for i in passwd:
    if i in shuzi:
        con += 1
        break
# 判断条件
while 1:
    if passwd_len == 1 or con == 1:
        print("您的安全级别评定为：低")
    elif passwd_len == 3 and con == 3 and (passwd[0] in zimu):
        print("您的安全级别评定为：高")
    else:
        print("您的安全级别评定为：中")
    print(
        """请按照一下方式提升您的密码安全级别：
        1.密码必须由数字、字母以及符号组成
        2.密码只能以字母开头
        3.密码长度不能低于16位"""
    )
    break
