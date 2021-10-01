def box_fill(l, w, h, size):
    if size < 0:
        return
    if 2**size <= l and 2**size <= w:
        x = l // (2**size)
        y = w // (2**size)
        z = h // (2**size)
        cube_cnt[size] += x*y*z
        if l % (2**size):
            box_fill(l-(2**size)*x, (2**size)*y, h, size-1)
        if w % (2**size):
            box_fill(l, w-(2**size)*y, h, size-1)
    else:
        box_fill(l, w, h, size-1)
    

l, w, h = map(int, input().split())
N = int(input())
cube = [0]*20
cube_cnt = [0]*20

for _ in range(N):
    A, B = map(int, input().split())
    cube[A] = B

for i in range(19, -1, -1):
    if h > 0:
        if (2**i) <= l and (2**i) <= w and (2**i) <= h:
            height = h % (2**i)
            box_fill(l, w, h-height, i)
            h = height

for i in range(19, 0, -1):
    if cube_cnt[i] > cube[i]:
        cube_cnt[i-1] += (cube_cnt[i] - cube[i]) * 8
        cube_cnt[i] = cube[i]

if cube_cnt[0] > cube[0]:
    print(-1)
else:
    print(sum(cube_cnt))