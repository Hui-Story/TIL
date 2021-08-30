T = int(input())
  
for case in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    total += lst[x][y]
            if total > max_total:
                max_total = total
                
    print('#{} {}'.format(case, max_total))