x,y,z = 1,2,3
print(x,y,z)
i = x
x = z
z = i
print(x,y,z)

# 作者还没有为 Python 加入三元操作符之前 社区的小伙伴们灵活的使用
(x < y and [x] or [y])[0]