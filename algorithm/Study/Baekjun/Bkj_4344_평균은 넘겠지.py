import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    N, *scores = map(int, input().split())
    score_avg = sum(scores) / N
    cnt = 0
    for score in scores:
        if score > score_avg:
            cnt += 1
    print(f'{(cnt/N)*100:0.3f}%')