import sys
input = sys.stdin.readline

N = int(input())
numbers = list(int(input()) for _ in range(N))

def divide(numbers):
    if len(numbers) < 2:
        return numbers
    left = numbers[:(len(numbers)//2)]
    right = numbers[(len(numbers)//2):]
    left = divide(left)
    right = divide(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while True:
        # 둘 다 같이 끝나면 종료
        if i == len(left) and j == len(right):
            break
        # left[i] & right[j] 비교
        # i, j가 인덱스를 넘어설 때
        if i == len(left):
            # right j인덱스 부터 끝까지 추가
            result.extend(right[j:])
            break
        if j == len(right):
            result.extend(left[i:])
            break
        # 둘 다 아닌 경우 크기 비교
        if left[i] >= right[j]:
            result.append(right[j])
            j += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
            
    # while left or right:
    #     if left and right:
    #         if left[0] < right[0]:
    #             result.append(left[0])
    #             # del left[0]
    #         else:
    #             result.append(right[0])
    #             # del right[0]
    #     elif left:
    #         result.append(left[0])
    #         # del left[0]
    #     else:
    #         result.append(right[0])
    #         # del right[0]
    return result

numbers_2 = divide(numbers)

for i in numbers_2:
    print(i)