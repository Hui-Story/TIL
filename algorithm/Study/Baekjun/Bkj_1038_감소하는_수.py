N = int(input())

cnt = 0
result = [0]
idx = 0
while True:
    if cnt == N:
        result.sort(reverse=True)
        print(''.join(list(map(str, result))))
        break
    if idx < len(result) - 1:
        if result[idx] + 1 < result[idx+1]:
            result[idx] += 1
        else:
            idx += 1
            continue
    else:
        if result[idx] < 9:
            result[idx] += 1
        else:
            if idx == 9:
                print(-1)
                break
            idx += 1
            result.append(idx)
    for i in range(idx):
        result[i] = i
    idx = 0
    cnt += 1