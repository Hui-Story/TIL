from collections import deque

N, M, V = map(int, input().split())

road_list = []
road_list_2 = []
num_list = [0] * (N+1)
num_list_2 = [0] * (N+1)

for i in range(N+1):
    road_list.append([])
    road_list_2.append([])

for i in range(M):
    a, b = map(int, input().split())
    road_list[a] += [b]
    road_list[b] += [a]
    road_list_2[a] += [b]
    road_list_2[b] += [a]

result = []
result_2 = []

stack = [V]

while stack:
    now_num = stack[-1]
    if num_list[now_num] == 0:
        num_list[now_num] += 1
        result.append(now_num)
    if road_list[now_num] and num_list[min(road_list[now_num])] == 0:
        stack.append(min(road_list[now_num]))
        road_list[now_num].remove(min(road_list[now_num]))
    elif road_list[now_num] and num_list[min(road_list[now_num])] == 1:
        road_list[now_num].remove(min(road_list[now_num]))
    else:
        stack.pop()

print(*result)

my_deque = deque([V])

while my_deque:
    now_num = my_deque.popleft()
    if num_list_2[now_num] == 0:
        num_list_2[now_num] += 1
        result_2.append(now_num)
    while road_list_2[now_num]:
        if num_list_2[min(road_list_2[now_num])] == 0:
            my_deque.append(min(road_list_2[now_num]))
            road_list_2[now_num].remove(min(road_list_2[now_num]))
        elif num_list_2[min(road_list_2[now_num])] == 1:
            road_list_2[now_num].remove(min(road_list_2[now_num]))

print(*result_2)