import sys
input = sys.stdin.readline

T = int(input())

decimals = [1] * 10001
decimals[1] = 0

for num in range(2, 5001):
    for i in range(num * 2, 10001, num):
        decimals[i] = 0

for _ in range(T):
    n = int(input())
    s = l = n // 2
    while True:
        if decimals[s] and decimals[l]:
            print(s, l)
            break
        s -= 1
        l += 1