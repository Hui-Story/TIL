
def binary_search(target):
    s = 0
    e = N - 1
    check = -1

    while s <= e:
        mid = (s + e) // 2

        if A[mid] == target:
            return True
        elif A[mid] < target:
            s = mid + 1
            if check == 1:
                return False
            check = 1
        else:
            e = mid - 1
            if check == 0:
                return False
            check = 0
    
    return False


T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    result = 0

    for num in B:
        if binary_search(num):
            result += 1

    print('#{} {}'.format(case, result))