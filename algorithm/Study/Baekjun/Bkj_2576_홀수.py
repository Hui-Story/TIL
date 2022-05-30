import sys
input = sys.stdin.readline

lst = []

for _ in range(7):
    num = int(input())
    if num % 2:
        lst.append(num)

if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)