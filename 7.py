

def yf(n):
    if n < 1:
        print('输入错误！')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return yf(n - 1) + yf(n - 2)
    

number = int(input('输入整数：'))
result = yf(number)
print('共有%d对兔子！' % result)
    

