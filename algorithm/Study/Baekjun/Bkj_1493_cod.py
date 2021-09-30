l, w, h = map(int, input().split())
N = int(input())
cube = [0]*20

for _ in range(N):
    A, B = map(int, input().split())
    cube[A] = B

for i in range(19, -1, -1):
    if cube[i]:
        if cube[i] <= l and cube[i] <= w and cube[i] <= h:
            pass