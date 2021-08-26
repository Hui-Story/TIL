URL = str(input())

protocol = ''
host = ''
others = ''

for i in range(len(URL)):
    if URL[i] == ':':
        break
    else:
        protocol += URL[i]

for i in range(len(URL)):
    if URL[i] == '/':
        if URL[i+1] == '/':
            for j in range(i+2, len(URL)):
                if URL[j] == '/':
                    break
                else:
                    host += URL[j]
        elif URL[i-1] != '/':
            for j in range(i+1, len(URL)):
                others += URL[j]

print('protocol: {}'.format(protocol))
print('host: {}'.format(host))
print('others: {}'.format(others))