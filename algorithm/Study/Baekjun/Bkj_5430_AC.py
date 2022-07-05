import sys, collections

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    array = input().strip()[1:-1].split(",")

    if n == 0:
        array = []

    queue = collections.deque(array)
    turn = 0

    for cmd in p:
        if cmd == "R":
            turn += 1
        else:
            if len(queue) == 0:
                print("error")
                break
            if turn % 2 == 0:
                queue.popleft()
            else:
                queue.pop()
    else:
        if turn % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")