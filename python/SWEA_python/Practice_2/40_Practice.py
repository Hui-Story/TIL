arr = []

while True:
    try:
        arr.append(input())
    except:
        break

for word in arr:
    print('>> {}'.format(word.upper()))