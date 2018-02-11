import random
范围 = int(input('输入整数范围：'))
次数 = int(input('输入次数：'))

answer = random.randint(1, 范围)
print(answer)

while 次数 > 0:
    guess = int(input('Guess Me:'))
    次数 = 次数 - 1
    if guess > answer:
        print('多了！')
    elif guess < answer:
        print('少了！')
    else:
        print('Bingo!!!')
        break
            
            
