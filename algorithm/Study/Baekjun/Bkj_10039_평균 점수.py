result = 0

for _ in range(5):
    N = int(input())
    result += max(N, 40)

print(result // 5)