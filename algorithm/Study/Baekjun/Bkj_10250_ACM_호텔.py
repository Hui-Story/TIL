import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H:
        print(str(N % H) + str((N // H) + 1).zfill(2))
    else:
        print(str(H) + str(N // H).zfill(2))