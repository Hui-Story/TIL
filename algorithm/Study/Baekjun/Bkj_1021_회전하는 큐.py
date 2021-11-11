import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))

deq = deque()
for i in range(1, N+1):
    deq.append(i)

result = 0

for num in num_lst:
    idx = deq.index(num)
    # 중심을 기준으로 왼쪽에 위치 (2. 연산)
    if idx <= len(deq)-idx:
        deq.rotate(-idx)
        result += idx
        deq.popleft()
    # 중심을 기준으로 오른쪽에 위치 (3. 연산)
    else:
        deq.rotate(len(deq)-idx)
        result += (len(deq)-idx)
        deq.popleft()

print(result)