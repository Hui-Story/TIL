import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(A * B // gcd(A, B))