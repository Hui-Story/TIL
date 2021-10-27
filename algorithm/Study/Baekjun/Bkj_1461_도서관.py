import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))
books.append(0)  # books에 중점인 0 을 추가
books.sort()  # books를 오름차순으로 정렬
result = 0

# 음수가 위치할 수 있는 좌측부터 값이 0인 지점까지 탐색
idx = 0
while books[idx] < 0:
    # tmp에 현재 위치의 절댓값을 저장
    tmp = abs(books[idx])
    # 한 번에 들 수 있는 책의 개수만큼 idx를 증가시키며 탐색
    for i in range(M):
        # 현재 idx의 값이 중점(0)인 경우 왕복 값을 합산하고 break
        if books[idx+i] == 0:
            result += 2 * tmp
            idx += i
            break
    # 음수 범위 내에서 M 만큼 순회한 경우, 왕복 값을 합산하고 idx 증가
    else:
        result += 2 * tmp
        idx += M
        continue
    break

# 양수가 위치할 수 있는 우측부터 값이 0인 지점까지 탐색
idx = N
while books[idx] > 0:
    tmp = abs(books[idx])
    # 한 번에 들 수 있는 책의 개수만큼 idx를 감소시키며 탐색
    for i in range(M):
        if books[idx-i] == 0:
            result += 2 * tmp
            idx -= i
            break
    # 양수 범위 내에서 M 만큼 순회한 경우, 왕복 값을 합산하고 idx 감소
    else:
        result += 2 * tmp
        idx -= M
        continue
    break

# 마지막 책을 나른 뒤에는 왕복할 필요가 없으므로
# 마지막 위치가 가장 멀리있는 경우 (좌 또는 우) 그 위치만큼 편도 값 감소
if abs(books[0]) >= abs(books[-1]):
    result -= abs(books[0])
else:
    result -= abs(books[-1])

print(result)