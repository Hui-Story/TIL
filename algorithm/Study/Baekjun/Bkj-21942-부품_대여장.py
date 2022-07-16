import sys
from datetime import datetime

input = sys.stdin.readline
MSISS = lambda: map(str, input().strip().split())

N, L, F = MSISS()
N, F = int(N), int(F)
period: int = int(L[:3]) * 1440 + int(L[4:6]) * 60 + int(L[7:])
data = dict()
penalty = dict()

for _ in range(N):
    day, time, item, member = MSISS()
    key: str = item + '.' + member
    current_date: str = day + '.' + time
    if data.get(key) and data[key] != '.':
        rent_date = datetime.strptime(data[key], "%Y-%m-%d.%H:%M")
        return_date = datetime.strptime(current_date, "%Y-%m-%d.%H:%M")
        diff = return_date - rent_date
        minute_diff = (diff.days * 1440 + diff.seconds / 60) - period
        if minute_diff > 0:
            if penalty.get(member):
                penalty[member] += minute_diff * F
            else:
                penalty[member] = minute_diff * F
        data[key] = '.'
    else:
        data[key] = current_date

sorted_penalty = sorted(penalty.items())

if sorted_penalty:
    for member, value in sorted_penalty:
        print(member, int(value))
else:
    print(-1)