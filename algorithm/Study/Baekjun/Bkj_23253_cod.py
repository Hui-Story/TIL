import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = 'Yes'

for _ in range(M):
    k = int(input())
    books = list(map(int, input().split()))
    if k >= 2:
        for i in range(k-1):
            if books[i] < books[i+1]:
                result = 'No'
                break

print(result)