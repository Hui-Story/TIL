def check(i, j, i_2, j_2):
    global lst
    for i_p in range(i_2 + 1):
        for j_p in range(j_2 + 1):
            if lst[i+i_p][j+j_p] == 0:
                return False
    return True
 
def cal(i, j, i_2, j_2):
    global lst, max_result
    result = 0
    for i_p in range(i_2+1):
        for j_p in range(j_2+1):
            result += lst[i+i_p][j+j_p]
    if result > max_result:
        max_result = result
 
 
T = int(input())
 
for case in range(1, T+1):
    H, W = map(int, input().split())
 
    lst = [list(map(int, input().split())) for _ in range(H)]
 
    max_result = 0
 
    for i in range(H):
        for j in range(W):
            for i_2 in range(H-i):
                for j_2 in range(W-j):
                    if check(i, j, i_2, j_2):
                        cal(i, j, i_2, j_2)
 
    print('#{} {}'.format(case, max_result))