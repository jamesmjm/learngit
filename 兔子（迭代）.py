def yf(n):
    a = 1
    b = 1
    c = 1
    if n < 1:
        print('wrong input!')
        return -1
    while (n - 2) > 0:
        c = a + b
        a = b
        b = c
        n = n - 1
    return c

number = int(input('输入整数：'))
result = yf(number)
if result != -1:
    print('共有%d对兔子！' % result)
    
    
    
