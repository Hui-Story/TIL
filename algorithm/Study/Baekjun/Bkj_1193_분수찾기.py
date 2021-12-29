X = int(input())

idx = 1
cnt = 0

while True:
    if cnt + idx < X:
        cnt += idx
        idx += 1
        continue
    temp = X - cnt
    if idx % 2:
        print(f'{idx + 1 - temp}/{temp}')
    else:
        print(f'{temp}/{idx + 1 - temp}')
    break