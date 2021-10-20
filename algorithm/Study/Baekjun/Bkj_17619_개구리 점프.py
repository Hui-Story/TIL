import sys
input = sys.stdin.readline

def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

def Find(ch):
    if parent[ch] != ch:
        parent[ch] = Find(parent[ch])
    return parent[ch]


N, Q = map(int, input().split())
parent = [i for i in range(N+1)]  # 부모 노드를 자기 자신으로 초기화
logs = []

# 통나무의 'x1, x2, 번호'를 logs에 추가
for num in range(1, N+1):
    x1, x2, y = map(int, input().split())
    logs.append((x1, x2, num))

# x1 이 작은 통나무부터 정렬
logs.sort(key=lambda x : x[0])

# 비교의 기준이 되는 통나무를 가장 앞에있는 통나무로 초기화
x1 = logs[0][0]
x2 = logs[0][1]
num = logs[0][2]

for log in logs:
    now_x1, now_x2, now_num = log
    # 이동이 가능한 경우 통나무를 집합으로 연결
    if now_x1 <= x2:
        Union(num, now_num)
    # 기준 통나무의 x2 보다 현재 통나무의 x1 이 큰 경우 (점프로 이동 불가능)
    else:
        # 연결하지 않고, 기준을 현재 통나무로 변경
        x1 = now_x1
        x2 = now_x2
        num = now_num
        continue
    # x2 의 크기가 가장 큰 통나무를 기준으로 변경
    if x2 < now_x2:
        x2 = now_x2
        num = now_num

for _ in range(Q):
    a, b = map(int, input().split())
    # 통나무를 점프해서 이동이 가능한 경우
    if Find(a) == Find(b):
        print(1)
    # 이동이 불가능한 경우
    else:
        print(0)