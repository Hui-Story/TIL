import sys
input = sys.stdin.readline

def setup(low, high):
    global C
    while True:
        middle = (low+high) // 2
        if low > high:
            return high
        elif check(middle) < C:
            high = middle - 1
        else:
            low = middle + 1
    return

def check(middle):
    global N, x
    cnt, now = 0, 0
    for i in x:
        if i >= now:
            cnt += 1
            now = i + middle
    return cnt

N, C = map(int, input().split())
x = [int(input()) for _ in range(N)]

x.sort()

print(setup(1, max(x)-min(x)))