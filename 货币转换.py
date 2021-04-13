A = input()
#记录用户输入值并对变量进行赋值
if A[-3:] == "RMB":
#如果变量后三位数值等于RMB折执行下列算式
    print("{:2f}USD".format(eval(A[:-3])/6.78))
#保留小数点后两位并返回计算结果值
elif A[-3:] in ['USD', 'usd']:
    print("{:2f}RMB".format(eval(A[:-3])*6.78))
else:
    print("输入格式错误")