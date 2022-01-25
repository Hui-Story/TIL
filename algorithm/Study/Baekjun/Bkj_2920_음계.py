sounds = list(map(int, input().split()))

ascending = False
descending = False

if sounds[0] == 1:
    ascending = True
elif sounds[0] == 8:
    descending = True

for i in range(1, 8):
    if ascending:
        if sounds[i] <= sounds[i-1]:
            ascending = False
            break
    if descending:
        if sounds[i] >= sounds[i-1]:
            descending = False
            break

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
    