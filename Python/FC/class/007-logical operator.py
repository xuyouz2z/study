# and 两边都对则为True 一边为错则返回False 两边都错也是False
print((1>=1) and (2>=1))
print((1>=1) and (2==1))
print((1>1) and (2==1))
print('-'*20)
# or 两边都对则为True 一边为对则返回True 两边都错则返回False
print((1>=1) or (2>=1))
print((1>=1) or (2==1))
print((1>1) or (2==1))
print('-'*20)
# not 1==1是错 1>3是对 返回结果和实际相反
print(not 1>3)
print(not 1==1)

print('-'*20)
cost = 30
print(cost > 10 and cost < 50)