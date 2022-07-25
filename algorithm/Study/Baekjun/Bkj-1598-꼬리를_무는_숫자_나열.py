A, B = map(int, input().split())
A -= 1
B -= 1
print(abs(A // 4 - B // 4) + abs(A % 4 - B % 4))