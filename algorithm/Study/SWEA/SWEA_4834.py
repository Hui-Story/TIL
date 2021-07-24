T = int(input())

N = []
ai = []
for i in range(T):
    N.append(input())
    ai.append(input())

for i in range(T):
    C = [0] * 10
    for a in range(int(N[i])):
        C[int(ai[i][a])] += 1
    count = 0
    num = 0
    for b in range(len(C)):
        if C[b] >= count:
            count = C[b]
            num = b
    print(f'#{i+1} {num} {max(C)}')