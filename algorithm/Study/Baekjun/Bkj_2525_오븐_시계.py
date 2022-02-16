A, B = map(int, input().split())
C = int(input())

B += C
A += B // 60

print(A % 24, B % 60)