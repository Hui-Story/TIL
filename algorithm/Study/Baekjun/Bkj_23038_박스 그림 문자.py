import sys
input = sys.stdin.readline

def connect_check(i, j):
    if 0 <= i < N*3 and 0 <= j < M*3 and grid[i][j] == '#':
        return True
    return False


N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(3*N)]

for i in range(0, N*3, 3):
    for j in range(0, M*3, 3):
        if grid[i+1][j+1] == '#':
            continue
        if connect_check(i-1, j+1):
            grid[i][j+1] = '#'
            grid[i+1][j+1] = '#'
        if connect_check(i+1, j-1):
            grid[i+1][j] = '#'
            grid[i+1][j+1] = '#'
        if connect_check(i+3, j+1):
            grid[i+2][j+1] = '#'
            grid[i+1][j+1] = '#'
        if connect_check(i+1, j+3):
            grid[i+1][j+2] = '#'
            grid[i+1][j+1] = '#'

for i in grid:
    print(''.join(i))