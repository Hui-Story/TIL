import sys
input = sys.stdin.readline

N = int(input().rstrip())
room = [[0]*N for _ in range(N)]
student = [0]*(N**2 + 1)  # 각 학생이 좋아하는 학생
order = []  # 자리를 정하는 학생 순서

for _ in range(N**2):
    inp = list(map(int, input().rstrip().split()))
    order.append(inp[0])
    student[inp[0]] = inp[1:5]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 0

# 순서에 따라 자리 배치
for num in order:
    # '빈 공간 최대, 좋아하는 학생 최대' 초기화
    max_empty = max_friend = 0
    # 첫 탐색인지 확인
    search = False
    for x in range(N):
        for y in range(N):
            if room[x][y] == 0:
                # 첫 탐색인 경우
                if not search:
                    student_loca = [x, y]
                search = True
                # 델타탐색으로 현재 자리와 인접한 '빈 공간, 좋아하는 학생' 카운트
                empty = friend = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if room[nx][ny] == 0:
                            empty += 1
                        if room[nx][ny] in student[num]:
                            friend += 1
                # 최적의 조건인 경우 현재 자리를 저장
                if friend > max_friend:
                    max_friend = friend
                    max_empty = empty
                    student_loca = [x, y]
                elif friend == max_friend:
                    if empty > max_empty:
                        max_empty = empty
                        student_loca = [x, y]
    # 최종적으로 정해진 자리에 학생 위치
    room[student_loca[0]][student_loca[1]] = num

# 자리가 모두 정해진 뒤 만족도를 합산
for x in range(N):
    for y in range(N):
        cnt = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and room[nx][ny] in student[room[x][y]]:
                cnt += 1
        if cnt:
            result += 10**(cnt-1)

print(result)