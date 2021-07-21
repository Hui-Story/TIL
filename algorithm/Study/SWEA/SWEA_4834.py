T = int(input())

N = []
ai = []
for i in range(T):
    N.append(input())
    ai.append(input())

for i in range(T):
    C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for a in range(int(N[i])):
        C[int(ai[i][a])] = C[int(ai[i][a])] + 1
    print(f'#{i+1} {max(C)}')