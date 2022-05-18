import sys, collections
input = sys.stdin.readline

N, M = map(int, input().split())
dict = collections.defaultdict(str)
for i in range(1, N + 1):
    pokemon = input().strip()
    dict[pokemon] = str(i)
    dict[str(i)] = pokemon
for _ in range(M):
    s = str(input().strip())
    print(dict[s])