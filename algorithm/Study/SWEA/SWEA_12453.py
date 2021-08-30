T = int(input())
 
for i in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    max_num = max(a)
    min_num = min(a)
    result = max_num - min_num
    print(f'#{i+1} {result}')