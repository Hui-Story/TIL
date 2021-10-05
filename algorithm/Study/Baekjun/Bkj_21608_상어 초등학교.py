import sys
input = sys.stdin.readline

N = int(input().rstrip())
room = [[0]*N for _ in range(N)]
student = [0]*(N**2 + 1)
order = []

for _ in range(N**2):
    inp = list(map(int, input().rstrip().split()))
    order.append(inp[0])
    student[inp[0]] = inp[1:5]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 0

for num in order:
    max_empty = max_friend = cnt = 0
    for x in range(N):
        for y in range(N):
            if room[x][y] == 0:
                if not cnt:
                    friend_loca = [x, y]
                    empty_loca = [x, y]
                empty = friend = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if room[nx][ny] == 0:
                            empty += 1
                        if room[nx][ny] in student[num]:
                            friend += 1
                if friend > max_friend:
                    cnt = 1
                    max_friend = friend
                    max_empty = empty
                    friend_loca = [x, y]
                    empty_loca = [x, y]
                elif friend == max_friend:
                    cnt += 1
                    if empty > max_empty:
                        max_empty = empty
                        empty_loca = [x, y]
    if cnt == 1:
        room[friend_loca[0]][friend_loca[1]] = num
    else:
        room[empty_loca[0]][empty_loca[1]] = num

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