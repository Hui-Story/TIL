import sys
input = sys.stdin.readline

n = int(input())
paper = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[y+i][x+j] = 1

arr = [[[0, 0] for _ in range(100)] for _ in range(100)]

# for i in range(100):
#     for j in range(100):
#         if paper[i][j] == 1:
#             if j == 0:
#                 arr[i][j][1] = 1
#             else:
#                 arr[i][j][1] = arr[i][j-1][1] + 1

for j in range(100):
    for i in range(100):
        if paper[i][j] == 1:
            if i == 0:
                arr[i][j][0] = 1
            else:
                arr[i][j][0] = arr[i-1][j][0] + 1

result = 0

for i in range(100):
    for j_s in range(100):
        cnt = 0
        min_len = 100
        for j in range(j_s, 100):
            if arr[i][j][0]:
                cnt += 1
                min_len = min(min_len, arr[i][j][0])
                area = cnt * min_len
                result = max(result, area)
            if cnt and arr[i][j][0] == 0:
                cnt = 0
                min_len = 100
#         if cnt:
#             area = cnt * min_len
#             result = max(result, area)

# for j in range(100):
#     for i_s in range(100):
#         cnt = 0
#         min_len = 100
#         for i in range(i_s, 100):
#             if arr[i][j][1]:
#                 cnt += 1
#                 min_len = min(min_len, arr[i][j][1])
#                 area = cnt * min_len
#                 result = max(result, area)
#             if cnt and arr[i][j][1] == 0:
#                 area = cnt * min_len
#                 result = max(result, area)
#                 cnt = 0
#                 min_len = 100
#         if cnt:
#             area = cnt * min_len
#             result = max(result, area)

print(result)