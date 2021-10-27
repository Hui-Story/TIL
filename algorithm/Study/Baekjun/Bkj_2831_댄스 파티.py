import sys
input = sys.stdin.readline

N = int(input())
man = list(map(int, input().split()))
woman = list(map(int, input().split()))
man.sort()  # 남자 리스트 오름차순 정렬
woman.sort()  # 여자 리스트 오름차순 정렬
result = 0

# 키가 작은 여자를 선호하는 남자와, 키가 큰 남자를 선호하는 여자 짝 탐색
# 남자는 왼쪽, 여자는 오른쪽부터 탐색
man_idx = 0
woman_idx = N-1
# 인덱스를 넘어가지 않고, 남자/여자의 값이 각각 음수/양수인 경우
while man_idx < N and woman_idx >= 0 and man[man_idx] < 0 and woman[woman_idx] > 0:
    # 조건에 부합하면 짝 카운트, 각각 인덱스 이동
    if abs(man[man_idx]) > abs(woman[woman_idx]):
        result += 1
        man_idx += 1
        woman_idx -= 1
    # 조건에 부합하지 않을 경우 여자 인덱스 이동
    else:
        woman_idx -= 1

# 키가 작은 남자를 선호하는 여자와, 키가 큰 여자를 선호하는 남자 짝 탐색
# 여자는 왼쪽, 남자는 오른쪽부터 탐색
woman_idx = 0
man_idx = N-1
# 인덱스를 넘어가지 않고, 여자/남자의 값이 각각 음수/양수인 경우
while woman_idx < N and man_idx >= 0 and woman[woman_idx] < 0 and man[man_idx] > 0:
    if abs(woman[woman_idx]) > abs(man[man_idx]):
        result += 1
        woman_idx += 1
        man_idx -= 1
    # 조건에 부합하지 않을 경우 남자 인덱스 이동
    else:
        man_idx -= 1

print(result)