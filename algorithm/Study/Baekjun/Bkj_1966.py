import sys
from collections import deque

T = int(input())

for i in range(T):
    N_M = sys.stdin.readline().split()
    list_input = sys.stdin.readline().split()
    print_list = deque(list(list_input))
    print_list_2 = deque(range(int(N_M[0])))
    count = 0
    while print_list:
        if max(print_list) == print_list[0]:
            print_list.popleft()
            print_num = print_list_2.popleft()
            count += 1
            if print_num == int(N_M[1]):
                print(count)
                break
        else:
            print_list.append(print_list.popleft())
            print_list_2.append(print_list_2.popleft())