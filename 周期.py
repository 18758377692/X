def dayUP(df):
#定义dayup占位符未df
    dayUP = 1
#初始值为1
    for i in range(365):
#从0到365之间循环
        if i % 7 in[6,0]:
#如果I与7之间的商余为6或者0折执行下列算式
            dayUP = dayUP*(1 - 0.01)
        else:
            dayUP = dayUP*(1 + df)
    return dayUP
#结果返回初始值
dayfavtor = 0.01
while dayUP(dayfavtor) < 37.78:
#循环执行dayup+dayfavtor，直到与37.78相近
    dayfavtor += 0.001
#dayfavtor等于dayfavtor加0.001
print("工作的:{:3f}".format(dayfavtor))
#打印