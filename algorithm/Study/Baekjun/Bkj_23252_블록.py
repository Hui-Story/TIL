import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    
    if A < C:
        print('No')
        continue
    A -= C
    if not C and B % 2:
        if A < 2:
            print('No')
            continue
        else:
            A -= 2
    if A % 2:
        print('No')
        continue

    print('Yes')