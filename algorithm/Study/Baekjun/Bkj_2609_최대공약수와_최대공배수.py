N, M = map(int, input().split())
min_num = min(N, M)

while True:
    if not N % min_num and not M % min_num:
        print(min_num)
        break
    min_num -= 1

print(N * M // min_num)