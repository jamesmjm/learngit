print("...........工作室............")

guess = int
account = 5

import random

secret = random.randint(1,10)
#print (secret)

while guess != secret and account > 0:
    
    print ('还有%s次机会' % account)
    account = account - 1
    temp = input ("猜:")
    guess = int(temp)

    if guess == secret:
        print("yes")
        print("good!")
    else:
        if guess < secret:
            print("more")
        else:
            print("less")

print("over!")
