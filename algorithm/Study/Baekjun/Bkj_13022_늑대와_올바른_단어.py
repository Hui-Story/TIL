string = input()

idx = 0
while idx < len(string):
    for i in range(1, 14):
        if string[idx : idx + i * 4] == 'w' * i + 'o' * i + 'l' * i + 'f' * i:
            idx += i * 4
            break
    else:
        print(0)
        exit()
print(1)