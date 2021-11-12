import sys
input = sys.stdin.readline

N = int(input())
name_lst = []
place_lst = []
time_table = dict()

for _ in range(N):
    name, place, *time = map(str, input().strip().split())
    time = list(map(int, time))
    if name not in name_lst:
        name_lst.append(name)
        if place not in place_lst:
            place_lst.append(place)
            time_table[place] = [0] * 50001
        for i in range(time[0], time[1]):
            time_table[place][i] += 1

place_lst.sort(reverse=True)

max_cnt = 0
max_idx = 0
max_cnt_place = ''
for place in place_lst:
    for i in range(50001):
        if place != max_cnt_place and time_table[place][i] >= max_cnt:
            max_idx = i
            max_cnt = time_table[place][i]
            max_cnt_place = place
        if time_table[place][i] > max_cnt:
            max_idx = i
            max_cnt = time_table[place][i]

last_idx = 50001
for idx in range(max_idx, 50001):
    if time_table[max_cnt_place][idx] != max_cnt:
        last_idx = idx
        break

print(max_cnt_place, max_idx, last_idx)