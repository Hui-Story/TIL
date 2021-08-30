for case in range(1, 11):
    N = int(input())
    arr = [str(input()) for _ in range(8)]

    result = 0

    for i in range(8):
        for j in range(8-N+1):
            if arr[i][j] == arr[i][j+N-1]:
                for k in range((N+1)//2):
                    if arr[i][j+k] != arr[i][j+N-1-k]:
                        break
                else:
                    result += 1
    
    for j in range(8):
        for i in range(8-N+1):
            if arr[i][j] == arr[i+N-1][j]:
                for k in range((N+1)//2):
                    if arr[i+k][j] != arr[i+N-1-k][j]:
                        break
                else:
                    result += 1
    
    print('#{} {}'.format(case, result))