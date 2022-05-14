import sys
input = sys.stdin.readline

N, W, H = map(int, input().split())
for _ in range(N):
    s = int(input())
    if s * s <= W * W + H * H:
        print('DA')
    else:
        print('NE')