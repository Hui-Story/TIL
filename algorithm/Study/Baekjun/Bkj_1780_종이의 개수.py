import sys
input = sys.stdin.readline

def cut(i_s, j_s, n, k):
    for i in range(i_s, i_s+n, k):
        for j in range(j_s, j_s+n, k):
            now = paper[i][j]
            if check(i, j, k, now):
                continue
            else:
                cut(i, j, k, k//3)

def check(i, j, k, now):
    global check_lst
    for k_i in range(i, i+k):
        for k_j in range(j, j+k):
            if paper[k_i][k_j] != now:
                return False
    check_lst[now+1] += 1
    return True


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

check_lst = [0]*3

k = N
cut(0, 0, N, k)

for i in check_lst:
    print(i)