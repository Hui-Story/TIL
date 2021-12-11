word = str(input())

check = [0] * 27

for i in word:
    check[ord(i) % 32] += 1

max_cnt = 0
many_check = False
for i in range(len(check)):
    if check[i] > check[max_cnt]:
        max_cnt = i
        many_check = False
    elif check[i] == check[max_cnt]:
        many_check = True

if many_check:
    print('?')
else:
    print(chr(max_cnt + 64))