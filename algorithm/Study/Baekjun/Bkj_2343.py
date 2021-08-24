import sys
input = sys.stdin.readline

def blu_ray(low, high):
    global M
    while True:
        middle = (low+high) // 2
        if low > high:
            return low
        elif record(middle) <= M:
            high = middle - 1
        else:
            low = middle + 1

def record(middle):
    global lesson
    cnt = 1
    n = middle
    for i in lesson:
        if n >= i:
            n -= i
        else:
            n = middle - i
            cnt += 1
    return cnt

N, M = map(int, input().split())
lesson = list(map(int, input().split()))

print(blu_ray(max(lesson), sum(lesson)))