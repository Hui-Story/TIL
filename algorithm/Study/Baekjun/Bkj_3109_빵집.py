import sys
input = sys.stdin.readline

# 오른쪽 위부터 아래쪽으로 탐색하면서 파이프라인을 카운트
def dfs(x, y):
    global MAP, result
    # 현재 위치가 원웅이의 빵집이라면
    if y == C-1:
        # 파이프라인 개수를 추가, 현재 위치를 'o'로 표시하고 True 리턴
        result += 1
        MAP[x][y] = 'o'
        return True
    # 오른쪽 위 대각선 탐색
    if x != 0 and MAP[x-1][y+1] == '.':
        # 파이프라인이 끝까지 연결될 수 있을 경우
        if dfs(x-1, y+1):
            # 현재 위치를 'o'로 표시
            MAP[x][y] = 'o'
            return True
    # 오른쪽 탐색
    if MAP[x][y+1] == '.':
        if dfs(x, y+1):
            MAP[x][y] = 'o'
            return True
    # 오른쪽 아래 대각선 탐색
    if x != R-1 and MAP[x+1][y+1] == '.':
        if dfs(x+1, y+1):
            MAP[x][y] = 'o'
            return True
    # 이어질 수 있는 파이프라인이 없으면, 현재 위치를 'x'로 표시하고 False 리턴
    MAP[x][y] = 'x'
    return False

R, C = map(int, input().split())
MAP = [list(str(input().strip())) for _ in range(R)]
result = 0

# 모든 행의 첫째 열부터 dfs 탐색
for x in range(R):
    dfs(x, 0)

print(result)