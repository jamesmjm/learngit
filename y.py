
answer = 'test'
print(answer)
次数 = int(3)
guess = str(input('请输入密码：'))

while 次数 > 1:
    if '*' in guess:
        input('密码中不可有“*”号！你还有3次机会！请输入密码：')
    elif guess == answer:
        print('密码正确，进入程序......')
    else:
        次数 = 次数 - 1
        input('密码输入错误！还有%d次机会。请输入密码:' %(次数))
            
