odd = []
for i in range(1, 101, 2):
    odd += [i]

for i in range(len(odd)):
    if i == len(odd)-1:
        print(odd[i], end='')
    else:
        print(odd[i], end=', ')