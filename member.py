list = []
for a in range(10):
    for b in range(10):
        if a%2 == 0:
            if b%2 != 0:
                list.append((a,b))

print(list)
