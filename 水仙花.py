
for i in range(100,10000):
    sum = 0
    temp = i
    while temp != 0:
        sum = sum + (temp%10) ** 3
        temp = temp // 10
    if sum == i:
        print(i)
        
    
