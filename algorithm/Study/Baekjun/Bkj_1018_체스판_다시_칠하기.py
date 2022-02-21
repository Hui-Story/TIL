import sys
input = sys.stdin.readline

def check(sx, sy):
    global result
    cnt_1 = 0
    for x in range(sx, sx + 8):
        for y in range(sy, sy + 8):
            if (x + y) % 2:
                if board[x][y] != 'W':
                    cnt_1 += 1
            else:
                if board[x][y] != 'B':
                    cnt_1 += 1
    cnt_2 = 0
    for x in range(sx, sx + 8):
        for y in range(sy, sy + 8):
            if (x + y) % 2:
                if board[x][y] != 'B':
                    cnt_2 += 1
            else:
                if board[x][y] != 'W':
                    cnt_2 += 1
    result = min(result, cnt_1, cnt_2)



N, M = map(int, input().split())
board = [str(input().strip()) for _ in range(N)]
result = 10000

for x in range(N - 7):
    for y in range(M - 7):
        check(x, y)

print(result)