N, K = map(int, input().split())

num = 1
while True:
    temp = N - num
    if K > temp:
        K -= temp
        num += 1
        continue
    result = list(range(num + 1, min(num + 1 + K, N+1))) + [num] + list(range(num + 1 + K, N+1)) + list(range(num-1, 0, -1))
    print(*result)
    break