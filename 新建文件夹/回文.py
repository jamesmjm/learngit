
def check(strhui):
    lenhui = len(strhui)    
    tail = -1
    lentemp = lenhui // 2
    for each in range(lenhui):
        if lentemp == 0:
            return 1
        elif strhui[each] != strhui[tail]:
            return 0
        else:
            tail = tail - 1
            lentemp = lentemp - 1

strhui = input('输入一句话：')
if check(strhui) == 1:
    print('yes')
else:
    print('no')

    
def palindrome(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):
        return '是回文联!'
    else:
        return '不是回文联！'
print(palindrome('上海自来水来自海上'))
