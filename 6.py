def cj(x):
	result = x
	for i in range(1,x):
		result = result * i
	return result

number = int(input('输入整数：'))
result = cj(number)
print('%d的阶乘是：%d' %(number,result))



def dg (n):
    if n == 1:
        return 1
    else:
        return n * dg(n-1)

number = int(input('输入整数：'))
result = cj(number)
print('%d的阶乘是：%d' %(number,result))  
