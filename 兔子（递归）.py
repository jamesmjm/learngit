def yf(n):
    a = 1
    b = 1
    c = 1
    if n < 1:
        print('wrong input!')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return yf(n-1) + yf(n-2)

number = int(input('输入整数：'))
result = yf(number)
if result != -1:
    print('共有%d对兔子！' % result)
    
    
    
