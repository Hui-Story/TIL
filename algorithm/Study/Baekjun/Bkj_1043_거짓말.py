import sys
input = sys.stdin.readline

def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

def Find(ch):
    if parent[ch] == ch:
        return ch
    ret = Find(parent[ch])
    parent[ch] = ret
    return parent[ch]

def my_func():
    global all_party, result

    for i in range(M):
        all_party.append(list(map(int, input().split())))
        if people_who_knows[0] != 0:
            if all_party[i][0] >= 2:
                for idx in range(1, all_party[i][0]):
                    Union(all_party[i][idx], all_party[i][idx+1])

    if people_who_knows[0] == 0:
        print(len(all_party))
        return

    for party in all_party:
        if Find(party[1]) != Find(people_who_knows[1]):
            result += 1
    
    print(result)


N, M = map(int, input().split())

parent = dict()
for ch in range(1, N+1):
    parent[ch] = ch

all_party = []
result = 0

people_who_knows = list(map(int, input().split()))
for i in range(1, len(people_who_knows)):
    parent[people_who_knows[i]] = people_who_knows[1]

my_func()