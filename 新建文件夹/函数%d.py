#打印指数幂
def power(x,y):
    mi = x**y
    print('%d的%d次方等于:'%(x,y),mi)
    
#打印最大公约数

def divisor(x,y):
    listx = []
    listy = []
    listz = []
    temp = 1
    for a in range(1,x+1):
        if x % a == 0:
            listx.append(a)
    for b in range(1,y+1):
        if y % b == 0:
            listy.append(b)
    print (listx)
    print (listy)

    for d in listx:
        for f in listy:
            if d == f:
                listz.append(d)
    print (listz)
    print(max(listz))
    
    
        
