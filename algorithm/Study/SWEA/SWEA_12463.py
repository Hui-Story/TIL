T = int(input())
 
for case in range(T):
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    max_sum = 0
    min_sum = 2e+10
    for i in range(0, len(a_list)-M+1):
        num_sum = 0
        for j in range(i, i+M):
            num_sum += a_list[j]
        if num_sum > max_sum:
            max_sum = num_sum
        if num_sum < min_sum:
            min_sum = num_sum
    print(f'#{case+1} {max_sum-min_sum}')