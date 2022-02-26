N, K = map(int, input().split())
students = list(map(int, input().split()))
diff = []  # 원생들의 키 차이

for i in range(1, N):
    diff.append(students[i] - students[i - 1])

# 키 차이가 큰 순서대로 나열
diff.sort(reverse=True)

# 키 차이가 큰 순서대로 (K - 1)개를 제외한 합 출력
print(sum(diff[K - 1:]))