N = int(input())
inner = 0
outer = 0
check = [0]*6
for _ in range(N):
    a, b = map(int, input().split())
    if 1 < abs(a-b) < 4:
        inner += 1
        check[a] += 1
        check[b] += 1
    else:
        outer += 1

if inner <= 1:
    print(0)
elif inner <= 2:
    for i in check:
        if i == 2:
            print(0)
            break
    else:
        print(1)
elif inner <= 4:
    print(1)
elif inner == 5:
    if outer <= 4:
        print(2)
    elif outer == 5:
        print(-1)