
def merge_sort(s, e):
    global A, result
    if s == e - 1:
        return
    
    mid = (s + e) // 2
    l = s
    r = mid
    merge_sort(s, mid)
    merge_sort(mid, e)

    merged_arr = []
    while l < mid and r < e:
        if A[l] > A[r]:
            merged_arr.append(A[r])
            r += 1
            result += mid - l
        else:
            merged_arr.append(A[l])
            l += 1
    
    merged_arr.extend(A[l:mid])
    merged_arr.extend(A[r:e])
    A[s:e] = merged_arr[:]


T = int(input())

for case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    result = 0

    merge_sort(0, N)
    
    print('#{} {}'.format(case, result))