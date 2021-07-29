blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_count = {}
for i in blood:
    if i in blood_count:
        blood_count[i] += 1
    else:
        blood_count[i] = 1

print(blood_count)