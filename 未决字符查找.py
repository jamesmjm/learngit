

def find(desstr,substr):
    lendes = len(desstr)
    lensub = len(substr)
    account = 0
    if substr not in desstr:
        print('not in!')
    else:
        for eachdes in range(lendes):

            if desstr[eachdes] == substr[0]:
                for eachsub in range(lensub):

                    if desstr[eachdes] == substr[eachsub] and eachsub == lensub - 1:

                        account = account + 1
                        eachdes = eachdes + 1
                    if desstr[eachdes] == substr[eachsub] and eachsub != lensub - 1:
                        eachdes = eachdes + 1

                    else:
                        break

        print (account)       

                    




desstr = input('des=:')
substr = input('sub=:')
find(desstr,substr)
