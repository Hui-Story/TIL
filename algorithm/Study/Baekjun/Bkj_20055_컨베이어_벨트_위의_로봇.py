from collections import deque

def work():
    global K, belt, robots, cnt
    while True:
        belt.rotate(1)
        robots.rotate(1)
        robots[-1] = 0
        for i in range(N - 2, 0, -1):
            if robots[i] and belt[i + 1] and not robots[i + 1]:
                if belt[i + 1] == 1:
                    K -= 1
                    if not K:
                        return
                belt[i + 1] -= 1
                robots[i] = 0
                if i != N - 2:
                    robots[i + 1] = 1
        if belt[0]:
            if belt[0] == 1:
                K -= 1
                if not K:
                    return
            belt[0] -= 1
            robots[0] = 1
        cnt += 1


N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([0] * N)

cnt = 1
work()

print(cnt)