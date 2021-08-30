for i in range(10):
    number = int(input())
    build = list(map(int, input().split()))
    result = 0
    for j in range(2, number-2):
        build_sort = sorted([build[j-2], build[j-1], build[j], build[j+1], build[j+2]])
        if build_sort[-1] == build[j] and build_sort.count(build_sort[-1]) == 1:
            result += (build_sort[-1] - build_sort[-2])
        else:
            continue
    print(f'#{i+1} {result}')