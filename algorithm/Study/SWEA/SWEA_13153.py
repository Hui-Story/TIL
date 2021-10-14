import heapq

def find_ugly_numbers():
    global ugly_numbers, heap
    while len(ugly_numbers) < 1501:
        num = heapq.heappop(heap)
        if num != ugly_numbers[-1]:
            ugly_numbers.append(num)
            for i in [2, 3, 5]:
                heapq.heappush(heap, num*i)

ugly_numbers = [0]
heap = []
heapq.heappush(heap, 1)
find_ugly_numbers()

T = int(input())

for case in range(1, T+1):
    N = int(input())
    inp = list(map(int, input().split()))
    result = []
    for i in range(N):
        result.append(ugly_numbers[inp[i]])
    print('#{} '.format(case), end='')
    print(*result)