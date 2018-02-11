
password = 'test'
count = 3

while count > 0:
    answer = input('输入密码：')
    count = count -1
    if answer == password:
        print('密码正确，进入程序...')
        break
    else:
        if count < 1:
            break
        else:        
            print('密码错误，你还有%d次机会，请重新输入密码：' %count)
    
    
