N, K = map(int, input().split())
students = list(map(int, input().split()))
diff = []

for i in range(1, N):
    diff.append(students[i] - students[i - 1])

diff.sort(reverse=True)

print(sum(diff) - sum(diff[:K - 1]))