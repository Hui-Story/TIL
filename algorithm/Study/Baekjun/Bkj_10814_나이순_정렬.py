import sys
input = sys.stdin.readline

N = int(input())

members = [[] for _ in range(201)]
for _ in range(N):
    age, name = map(str, input().strip().split())
    members[int(age)].append(name)

for age in range(1, 201):
    for name in members[age]:
        print(age, name)