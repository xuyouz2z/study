list1 = ["1.牛牛的", "2.帅帅的", "3.厉害的"]
list2 = ["3.篮球", "2.足球", "1.羽毛球"]
list3 = [
    name + "-" + slogan[2:]
    for slogan in list1
    for name in list2
    if slogan[0] == name[0]
]
for i in list3:
    print(i)
