T = int(input())
 
for case in range(1, T+1):
    N = int(input())
    lst = [[0] * 10 for _ in range(10)]
    count = 0
    for paint in range(N):
        color = list(map(int, input().split()))
        for i in range(color[1], color[3]+1):
            for j in range(color[0], color[2]+1):
                if color[4] == 1:
                    if lst[i][j] == 0:
                        lst[i][j] = 1
                    elif lst[i][j] == 2:
                        lst[i][j] = 3
                        count += 1
                elif color[4] == 2:
                    if lst[i][j] == 0:
                        lst[i][j] = 2
                    elif lst[i][j] == 1:
                        lst[i][j] = 3
                        count += 1
    print('#{} {}'.format(case, count))