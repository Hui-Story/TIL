import sys

T = sys.stdin.readline()

for case in range(int(T)):
    N = sys.stdin.readline()
    score = {}
    for Person in range(int(N)):
        score_1, score_2 = sys.stdin.readline().split()
        score[int(score_1)] = int(score_2)
    total = 1
    left_score = score[1]
    for i in range(2, int(N)+1):
        if score[i] < left_score:
            left_score = score[i]
            total += 1
    print(total)