T = int(input())
 
for case in range(T):
    N = int(input())
    a = input()
    lst = [0] * 10
    for number in a:
        lst[int(number)] += 1
    max_num = 0
    for i in range(len(lst)):
        if lst[i] >= lst[max_num]:
            max_num = i
    print(f'#{case+1} {max_num} {lst[max_num]}')