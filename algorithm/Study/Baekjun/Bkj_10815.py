import sys

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
find_lst = list(map(int, sys.stdin.readline().split()))

cards.sort()
result = []

# 재귀

# def binary(low, high, key):
#     global cards
#     if low > high:
#         return 0
#     else:
#         middle = (low + high) // 2
#         if key == cards[middle]:
#             return 1
#         elif key < cards[middle]:
#             return binary(low, middle-1, key)
#         elif key > cards[middle]:
#             return binary(middle+1, high, key)

# while

def binary(low, high, key):
    while low <= high:
        middle = (low + high) // 2
        if key == cards[middle]:
            return 1
        elif key < cards[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return 0

for key in find_lst:
    result.append(binary(0, len(cards)-1, key))

print(*result)