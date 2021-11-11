import sys
input = sys.stdin.readline

# 계수 정렬 (counting sort)
count = {}

N = int(input())

for _ in range(N):
    count[int(input())] = 1

for num in sorted(count.keys()):
    print(num)


# # 병합 정렬 (Merge Sort)

# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
    
#     mid = len(arr) // 2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])

#     merged_arr = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])
#             h += 1
#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     return merged_arr

# N = int(input())
# arr = [int(input()) for _ in range(N)]

# for i in merge_sort(arr):
#     print(i)