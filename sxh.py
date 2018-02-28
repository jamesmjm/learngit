for i in range(100,1000):
    x = i
    temp = 0
    while x:
        temp = (x % 10)**3 + temp
        x = x // 10
            
        if temp == i:
            print (temp)
