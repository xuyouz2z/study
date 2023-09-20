name = input("请输入要查找的用户名")
score = [["迷途", 85], ["昼夜", 89], ["小布丁", 65], ["福禄娃娃", 95], ["怡景", 90]]
for each in score:
    if name in name:
        print(name + "的得分是：", each[1])
    break
if name != score:
    print("您查找的数据不存在")
