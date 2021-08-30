T = int(input())
 
for case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
 
    for i in range(0, 10):
        number = i
        for j in range(i+1, len(lst)):
            if i % 2 == 0 and lst[j] > lst[number]:
                number = j
            elif i % 2 == 1 and lst[j] < lst[number]:
                number = j
        lst[i], lst[number] = lst[number], lst[i]
    print('#{}'.format(case), end=' ')
    print(*lst[0:10])