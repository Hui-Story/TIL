import sys, collections

input = sys.stdin.readline
Board = list[list[int]]

def play2048(N: int, board: Board) -> int:

    answer: int = max(max(b) for b in board)

    deq = collections.deque([])
    deq.append((1, board))
    
    while deq:
        step, _board = deq.popleft()
        # 좌
        current_board: Board = [[0] * N for _ in range(N)]
        for x in range(N):
            y_idx: int = 0
            for y in range(N):
                if (current_number := _board[x][y]) != 0:
                    board_number: int = current_board[x][y_idx]
                    if current_number == board_number:
                        current_board[x][y_idx] += current_number
                        answer = max(answer, current_number * 2)
                        y_idx += 1
                        continue
                    if board_number != 0:
                        y_idx += 1
                    current_board[x][y_idx] = current_number
        if step < 10:
            deq.append((step + 1, current_board))

        # 우
        current_board: Board = [[0] * N for _ in range(N)]
        for x in range(N):
            y_idx: int = N - 1
            for y in range(N - 1, -1, -1):
                if (current_number := _board[x][y]) != 0:
                    board_number: int = current_board[x][y_idx]
                    if current_number == board_number:
                        current_board[x][y_idx] += current_number
                        answer = max(answer, current_number * 2)
                        y_idx -= 1
                        continue
                    if board_number != 0:
                        y_idx -= 1
                    current_board[x][y_idx] = current_number
        if step < 10:
            deq.append((step + 1, current_board))

        # 위
        current_board: Board = [[0] * N for _ in range(N)]
        for y in range(N):
            x_idx: int = 0
            for x in range(N):
                if (current_number := _board[x][y]) != 0:
                    board_number: int = current_board[x_idx][y]
                    if current_number == board_number:
                        current_board[x_idx][y] += current_number
                        answer = max(answer, current_number * 2)
                        x_idx += 1
                        continue
                    if board_number != 0:
                        x_idx += 1
                    current_board[x_idx][y] = current_number
        if step < 10:
            deq.append((step + 1, current_board))

        # 아래
        current_board: Board = [[0] * N for _ in range(N)]
        for y in range(N):
            x_idx: int = N - 1
            for x in range(N - 1, -1, -1):
                if (current_number := _board[x][y]) != 0:
                    board_number: int = current_board[x_idx][y]
                    if current_number == board_number:
                        current_board[x_idx][y] += current_number
                        answer = max(answer, current_number * 2)
                        x_idx -= 1
                        continue
                    if board_number != 0:
                        x_idx -= 1
                    current_board[x_idx][y] = current_number
        if step < 10:
            deq.append((step + 1, current_board))

    return answer


N: int = int(input())
board: Board = [list(map(int, input().split())) for _ in range(N)]

print(play2048(N, board))