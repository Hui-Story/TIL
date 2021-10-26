import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))
books.append(0)
books.sort()
result = 0

idx = 0
while books[idx] < 0:
    tmp = abs(books[idx])
    for i in range(M):
        if books[idx+i] == 0:
            result += 2 * tmp
            idx += i
            break
    else:
        result += 2 * tmp
        idx += M
        continue
    break

idx = N
while books[idx] > 0:
    tmp = abs(books[idx])
    for i in range(M):
        if books[idx-i] == 0:
            result += 2 * tmp
            idx -= i
            break
    else:
        result += 2 * tmp
        idx -= M
        continue
    break

if abs(books[0]) >= abs(books[-1]):
    result -= abs(books[0])
else:
    result -= abs(books[-1])

print(result)