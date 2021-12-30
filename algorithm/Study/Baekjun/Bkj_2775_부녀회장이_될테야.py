import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    apart = [i for i in range(n+1)]

    for _ in range(k):
        for i in range(1, n+1):
            apart[i] = apart[i-1] + apart[i]
    
    print(apart[-1])