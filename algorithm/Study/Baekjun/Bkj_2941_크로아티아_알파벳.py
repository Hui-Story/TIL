word = str(input())

result = 0
for i in range(len(word)):
    if word[i-2:i+1] == 'dz=':
        result -= 1
    elif word[i-1:i+1] == 'c=' or word[i-1:i+1] == 's=' or word[i-1:i+1] == 'z=' or word[i-1:i+1] == 'c-' or word[i-1:i+1] == 'd-' or word[i-1:i+1] == 'lj' or word[i-1:i+1] == 'nj':
        continue
    else:
        result += 1
print(result)