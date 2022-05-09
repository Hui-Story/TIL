import sys, itertools, collections
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

def game(perm):
    global deq
    deq = collections.deque([0, 1, 2])
    gesture_idx = [0, 0, 0]
    win_cnt = [0, 0, 0]

    while True:
        a = deq.popleft()
        b = deq.popleft()
        if not a:
            i = perm[gesture_idx[0]]
        else:
            i = gestures[a - 1][gesture_idx[a]]
        if not b:
            j = perm[gesture_idx[0]]
        else:
            j = gestures[b - 1][gesture_idx[b]]
        gesture_idx[a] += 1
        gesture_idx[b] += 1
        if table[i - 1][j - 1] == 2:
            win_cnt[a] += 1
            deq.append(a)
            deq.append(b)
        elif table[i - 1][j - 1] == 1:
            win_cnt[max(a, b)] += 1
            deq.append(max(a, b))
            deq.append(min(a, b))
        else:
            win_cnt[b] += 1
            deq.append(b)
            deq.append(a)
        for c in range(3):
            if win_cnt[c] == K:
                if c == 0:
                    return True
                else:
                    return False
        if gesture_idx[0] >= N:
            return False

N, K = MIIS()
table = [list(MIIS()) for _ in range(N)]
gestures = [list(MIIS()) for _ in range(2)]
perms = itertools.permutations(range(1, N + 1), N)

for perm in perms:
    if game(perm):
        print(1)
        break
else:
    print(0)