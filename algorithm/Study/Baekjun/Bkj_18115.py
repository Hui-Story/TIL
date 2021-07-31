from collections import deque

N = int(input())
skill = input().split()

num_list = deque([i for i in range(1, N+1)])

# for i in range(1, N+1):
#     num_list.append(i)

result = deque()

for i in range(N-1, -1, -1):
    if skill[i] == '1':
        result.appendleft(num_list.popleft())
    elif skill[i] == '2':
        first = result.popleft()
        result.appendleft(num_list.popleft())
        result.appendleft(first)
    else:
        result.append(num_list.popleft())

# for i in range(0, N):
#     print(int(result[i]), end = ' ')

print(*result)