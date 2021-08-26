import sys
from collections import deque
input = sys.stdin.readline

Cpt = int(input())
Cpt_set = int(input())

dic = {}
used = [0] * (Cpt+1)
used[1] = 1
q = deque()
q.append(1)
result = 0

dic = {}
for i in range(1, Cpt+1):
    dic[i] = []

for _ in range(Cpt_set):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

while q:
    a = q.popleft()
    for i in dic[a]:
        if used[i] == 0:
            used[i] = 1
            q.append(i)
            result += 1

print(result)