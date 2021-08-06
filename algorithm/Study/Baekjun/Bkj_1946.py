T = int(input())

for case in range(T):
    N = int(input())
    score = {}
    for Person in range(N):
        input_score = list(map(int,input().split()))
        score[input_score[0]] = input_score[1]
    for i in range(1, N+1):
        for j in range(1, i+1):
            