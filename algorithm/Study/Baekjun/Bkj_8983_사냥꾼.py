import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

def find_station_idx(target: int) -> int:
    start, end = 0, M - 1
    while True:
        if start >= end:
            return start

        mid = (start + end) // 2

        if target > stations[mid]:
            start = mid + 1
        else:
            end = mid


M, N, L = MIIS()
stations = sorted(list(MIIS()))
animals = [tuple(MIIS()) for _ in range(N)]
result = 0

for a, b in animals:
    station_idx = find_station_idx(a)
    if station_idx >= 1:
        if abs(stations[station_idx] - a) <= abs(stations[station_idx - 1] - a):
            station = stations[station_idx]
        else:
            station = stations[station_idx - 1]
    else:
        station = stations[station_idx]
    
    if abs(station - a) + b <= L:
        result += 1

print(result)