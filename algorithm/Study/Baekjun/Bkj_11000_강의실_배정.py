import sys, heapq
input = sys.stdin.readline

N = int(input())
# 수업 시작과 끝이 빠른 순으로 정렬
lectures = sorted([tuple(map(int, input().split())) for _ in range(N)])

room_cnt = 0
max_room = 0
min_heap = []  # 수업이 끝나는 시간 저장

for S, T in lectures:
    # 현재 수업이 시작하기 전에 끝나는 수업 빼기
    while min_heap and S >= min_heap[0]:
        heapq.heappop(min_heap)
        room_cnt -= 1
    # 현재 수업을 추가한 뒤 최대 강의실 갱신
    room_cnt += 1
    heapq.heappush(min_heap, T)
    max_room = max(max_room, room_cnt)

print(max_room)