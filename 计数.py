
def count(*param):
    lenshu = len(param)
    for i in range(lenshu):
        letter = 0
        digit = 0
        space = 0
        other = 0
        for each in param[i]:
            if each.isalpha():
                letter += 1
            elif each.isdigit():
                digit += 1
            elif each == ' ':
                space += 1
            else:
                other += 1
        print('第%d个字符串有%d个字符，%d个数字，%d个空格，%d个其他字符' %(i+1,letter,digit,space,other))


str1 = input('输入字符串1：')
str2 = input('输入字符串2：')
str3 = input('输入字符串3：')

count(str1,str2,str3)
