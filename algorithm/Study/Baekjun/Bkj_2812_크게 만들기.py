import sys
input = sys.stdin.readline

N, K = map(int, input().split())
number = str(input().strip())
result = ''

idx = 0  # 탐색을 시작할 인덱스
cnt = 0  # 찾은 숫자 개수

# N-K 개의 숫자를 골라서 최대를 만드는 방식으로 접근
# 탐색할 범위가 골라낼 숫자의 개수보다 크고, 골라낼 숫자가 남아있을 때까지 탐색
while idx < (K+cnt) and cnt < (N-K):
    # 큰 숫자부터 탐색
    for num in range(9, -1, -1):
        # idx 부터 골라내야 하는 숫자의 첫 자리(뒤에서부터 남은 자리수 카운트)까지 탐색
        for i in range(idx, K+cnt+1):
            # 동일한 수를 찾으면 (가장 큰 수)
            if number[i] == str(num):
                result += number[i]
                idx = i+1  # idx를 찾은 수의 바로 뒤 인덱스로 업데이트
                cnt += 1
                break
        else:
            continue
        break

# 골라낼 숫자가 남아있을 경우 (idx 부터 끝까지는 모두 골라야하는 경우)
if cnt < (N-K):
    # 모두 결과에 추가
    result += number[idx:]

print(result)