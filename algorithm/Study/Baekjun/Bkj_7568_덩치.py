import sys
input = sys.stdin.readline

N = int(input())
human_lst = [tuple(map(int, input().split())) for _ in range(N)]
rank = [1] * N

for i in range(N - 1):
    for j in range(i + 1, N):
        if human_lst[i][0] > human_lst[j][0] and human_lst[i][1] > human_lst[j][1]:
            rank[j] += 1
        elif human_lst[i][0] < human_lst[j][0] and human_lst[i][1] < human_lst[j][1]:
            rank[i] += 1

print(*rank)