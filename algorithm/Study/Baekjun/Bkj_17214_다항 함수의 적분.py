poly = str(input())

result = []
now = ''
for i in poly:
    if i in ['+', '-']:
        if now:
            result.append(now)
            now = ''
        result.append(i)
    elif i == 'x':
        if now.isdigit():
            if now != '2':
                result.append(str(int(now)//2))
            result.append('xx')
            now = ''
        else:
            result.append('xx')
    else:
        now += i

if now != '0' and now.isdigit():
    if now != '1':
        result.append(now)
    result.append('x')

if result:
    print(''.join(result)+'+W')
else:
    print('W')