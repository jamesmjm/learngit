
number = int ( input ("请输入分数：") )

if (number < 0 or number > 100 ):
    print ("错误数据")
elif (100 >= number >= 90):
    print ("A")
elif (90 > number >= 80):
    print ("B")
elif (80 > number >= 70):
    print ("C")
elif (70 > number >= 60):
    print ("D")
else:
    print ("F")
