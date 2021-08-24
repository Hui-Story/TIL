import sys
input = sys.stdin.readline

def chicken(low, high):
    global C
    while True:
        middle = (low+high) // 2
        if low > high:
            return high
        elif cal(middle) >= C:
            low = middle + 1
        else:
            high = middle - 1

def cal(middle):
    global L
    cnt = 0
    for i in L:
        cnt += i // middle
    return cnt

S, C = map(int, input().split())
L = [int(input().strip()) for _ in range(S)]

length = chicken(1, max(L))

print(sum(L) - length*C)