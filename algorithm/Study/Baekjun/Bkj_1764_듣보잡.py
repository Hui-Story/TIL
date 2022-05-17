import sys, collections
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
dict = collections.defaultdict(int)

for _ in range(N):
    word = str(input().strip())
    dict[word] = 1

for _ in range(M):
    word = str(input().strip())
    if dict[word]:
        result.append(word)

result.sort()
print(len(result))
for i in result:
    print(i)