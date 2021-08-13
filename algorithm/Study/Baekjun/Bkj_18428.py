import copy

N = int(input())
lst = [list(map(str, input().split())) for _ in range(N)]

result = 'NO'

def wall(lst, count, now_i, now_j):
    global N, result
    wall_lst = copy.deepcopy(lst)
    if count == 3:
        if check(wall_lst) == True:
            result = 'YES'
            return
        else:
            return
    for i in range(now_i, N):
        for j in range(now_j, N):
            if j+1 >= N and i+1 < N:
                now_i_2, now_j_2 = i+1, 0
                now_j = 0
            elif count < 2 and j+1 >= N and i+1 >= N:
                return
            else:
                now_i_2, now_j_2 = i, j+1
            if wall_lst[i][j] == 'X':
                wall_lst[i][j] = 'O'
                count += 1
                wall(wall_lst, count, now_i_2, now_j_2)
                wall_lst[i][j] = 'X'
                count -= 1

def check(lst):
    global N
    now_check = 'X'
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 'S' and now_check == 'T':
                return False
            elif lst[i][j] == 'T' and now_check == 'S':
                return False
            elif lst[i][j] != 'X':
                now_check = lst[i][j]
        now_check = 'X'
    for j in range(N):
        for i in range(N):
            if lst[i][j] == 'S' and now_check == 'T':
                return False
            elif lst[i][j] == 'T' and now_check == 'S':
                return False
            elif lst[i][j] != 'X':
                now_check = lst[i][j]
        now_check = 'X'
    return True


wall(lst, 0, 0, 0)
print(result)