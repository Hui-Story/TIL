import sys, itertools
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

def play():
    global NMAP, max_cnt, cnt, step
    NMAP = [row[:] for row in MAP]
    cnt = 0
    step = 1

    while True:
        attack_turn()
        move_turn()
        if not sum(sum(row) for row in NMAP[step:]):
            max_cnt = max(max_cnt, cnt)
            break
        step += 1

def attack_turn():
    global NMAP, cnt
    remove = []
    for a in archers:
        remove_target = archer_attack(a)
        if remove_target:
            remove.append(remove_target[0][:2])
    remove = set(remove)
    for i, j in remove:
        cnt += 1
        NMAP[i][j] = 0

def archer_attack(a):
    remove_target = []
    for i in range(N - 1, step - 2, -1):
        if (N - i) > D:
            break
        for j in range(M):
            dist = (N - i) + abs(a - j)
            if dist > D:
                continue
            if NMAP[i][j]:
                remove_target.append((i, j, dist))
    remove_target.sort(key=lambda x : (x[2], x[1]))
    return remove_target

def move_turn():
    global NMAP
    for i in range(N - 1, step - 2, -1):
        if not i:
            NMAP[i] = [0] * M
        else:
            NMAP[i] = NMAP[i - 1][:]

N, M, D = MIIS()
MAP = [list(MIIS()) for _ in range(N)]
NMAP = []
max_cnt = 0
cnt = 0
step = 1
archers_comb = list(itertools.combinations(range(M), 3))
archers = []

for i in range(len(archers_comb)):
    archers = archers_comb[i]
    play()

print(max_cnt)