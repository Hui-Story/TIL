import sys

N, M = map(int, input().split())
lst = [int(sys.stdin.readline()) for _ in range(N)]

def cost(low, high):
    global N, M, lst
    while True:
        middle = (low + high) // 2
        money = middle
        cnt = 1

        for i in lst:
            if middle < i:
                low = middle
                break
            elif money >= i:
                money -= i
            else:
                money = middle - i
                cnt += 1
        else:
            if (high - low) <= 1:
                print(low)
                return
            elif cnt < M:
                high = middle
            else:
                low = middle

cost(1, 10000)