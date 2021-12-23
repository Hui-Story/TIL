import sys
input = sys.stdin.readline

T, W = map(int, input().split())
cnt_lst = []
pre = int(input())
cnt = 1
for _ in range(T-1):
    now = int(input())
    if pre == now:
        cnt += 1
    else:
        pre = now
        cnt_lst.append(cnt)
        cnt = 1
cnt_lst.append(cnt)
cnt_lst.sort(reverse=True)

print()