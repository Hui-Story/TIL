T = int(input())

for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    result = 0

    for idx in range(N):
        if idx == 1:
            result = max(result, L[idx]-L[idx-1])
        elif idx > 1:
            result = max(result, L[idx]-L[idx-2])
        if idx == N-1:
            reseult = max(result, L[idx]-L[idx-1])
    
    print(result)