from math import ceil, sqrt

G = int(input())

l, h = 1, ceil(sqrt(G))
h_max = (G // 2) + 1
is_exist = False

while h <= h_max:
    gap = h * h - l * l
    if gap < G:
        h += 1
    elif gap > G:
        l += 1
    else:
        print(h)
        is_exist = True
        h += 1

if not is_exist:
    print(-1)