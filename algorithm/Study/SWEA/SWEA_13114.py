def quick_sort(s, e):
    if s >= e:
        return

    pivot = arr[s]
    l = s + 1
    r = e

    while l <= r:
        while l <= r and arr[l] <= pivot:
            l += 1
        while s < r and arr[r] >= pivot:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]

    arr[s], arr[r] = arr[r], arr[s]
    
    quick_sort(s, r - 1)
    quick_sort(r + 1, e)


T = int(input())

for case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, N-1)

    print('#{} {}'.format(case, arr[N//2]))