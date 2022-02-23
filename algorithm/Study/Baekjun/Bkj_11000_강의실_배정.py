import sys, heapq
input = sys.stdin.readline

N = int(input())
lectures = sorted([tuple(map(int, input().split())) for _ in range(N)])

room_cnt = 0
max_room = 0
min_heap = []

for S, T in lectures:
    while min_heap and S >= min_heap[0]:
        heapq.heappop(min_heap)
        room_cnt -= 1
    room_cnt += 1
    heapq.heappush(min_heap, T)
    max_room = max(max_room, room_cnt)

print(max_room)