import sys
input = sys.stdin.readline

N, M = map(int, input().split())
examiner_lst = [int(input()) for _ in range(N)]
examiner_lst.sort()

start, end = 1, M * examiner_lst[0]

while True:
    if start >= end:
        print(start)
        break
    mid = (start + end) // 2
    examined_people = 0
    for time in examiner_lst:
        examined_people += (mid // time)
    if examined_people < M:
        start = mid + 1
    else:
        end = mid