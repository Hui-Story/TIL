
def merge_sort(arr):
    global result

    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    if low_arr[-1] > high_arr[-1]:
        result += 1

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


T = int(input())

for case in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    result = 0

    print('#{} {} {}'.format(case, merge_sort(a)[N//2], result))