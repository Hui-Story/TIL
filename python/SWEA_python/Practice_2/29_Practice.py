a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

result = set()

for key, value in a.items():
    if value >= 3000:
        result.add((key, value))

for key, value in b.items():
    if value >= 3000 and key not in a.keys():
        result.add((key, value))

print(result)