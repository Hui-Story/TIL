import sys

input = sys.stdin.readline

while True:
    name, age, weight = input().rstrip().split()
    age, weight = int(age), int(weight)

    if name == '#' and age == 0 and weight == 0:
        break

    if age > 17 or weight >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')