fuhao = r"""`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>"""
zimu = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
shuzi = "0123456789"
passwd = input("请输入要检测的密码：")
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
        print("低级密码")
    elif passwd_len == 3 and con == 3 and (passwd[0] in zimu):
        print("高级密码")
    else:
        print("中级密码")
    break
