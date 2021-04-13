TempsTr = input()
# 双向赋值，input  记录用户输入值由TempsTr保存
if TempsTr[-1] in ['F', 'f']:
#如果变量最后一位数值包括F或者f折执行下列算式
    C = (eval(TempsTr[0:-1]) - 32)/1.8
#需转换值等于变量第一位到倒数第二位的数值-32/1.8
    print("{:0.2f}C".format(C))
#打印结果小数点2位的数值
elif TempsTr[-1] in ['C', 'c']:
    F = eval(TempsTr[0:-1])*1.8 + 32
    print("{:.2f}F".format(F))
else:
#第二判断值
    print("输入格式错误")
#打印