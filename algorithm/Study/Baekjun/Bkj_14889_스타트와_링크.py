import sys
input = sys.stdin.readline

def make_team(idx, members, others, score):
    global result
    if idx == N:
        result = min(abs(score), result)
        return
    if len(members) < N // 2:
        new_score = score
        for i in members:
            new_score += (S[i][idx] + S[idx][i])
        make_team(idx + 1, members + [idx], others, new_score)
    if len(others) < N // 2:
        new_score = score
        for i in others:
            new_score -= (S[i][idx] + S[idx][i])
        make_team(idx + 1, members, others + [idx], new_score)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
result = 10000000

make_team(0, [], [], 0)

print(result)