import sys, collections
input = sys.stdin.readline

N, M = map(int, input().split())
dict = collections.defaultdict(int)
result = 0

for _ in range(N):
    word = str(input().strip())
    dict[word] = 1

for _ in range(M):
    word = str(input().strip())
    if dict[word]:
        result += 1

print(result)