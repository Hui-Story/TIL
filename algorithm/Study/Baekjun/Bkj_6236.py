import sys

N, M = map(int, input().split())
lst = [int(sys.stdin.readline()) for _ in range(N)]

low = 1
# low = max(lst)
high = 10000*N

while True:
    middle = (low + high) // 2
    money = middle
    cnt = 1

    for i in lst:
        if money >= i:
            money -= i
        elif middle < i:
            low = middle + 1
            break
        else:
            money = middle - i
            cnt += 1
    else:
        if low == high:
            print(low)
            break
        elif cnt <= M:
            high = middle
        else:
            low = middle + 1