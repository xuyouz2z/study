def discounts(item, dis):
    num = item * dis
    # print(f"试图访问全局变量{num_num}")
    #! 这里的属于局部变量，和函数外的全局变量num_num是互相存在的，即使变量名一样但存储空间不同
    num_num = 100
    print(f"修改后的num_num的值{num_num}")
    return num


num_num = float(input("请输入原价："))
dis = float(input("请输入折扣"))
newnum = discounts(num_num, dis)
print(f"打折后的价格是{newnum:.2f}")
print(f"修改后的num_num的值是{num_num}")
# print(f"修改局部变量？{num}")
