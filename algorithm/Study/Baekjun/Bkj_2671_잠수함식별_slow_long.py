string = str(input())

state = 0
idx = 0
while idx < len(string):
    if state == 0:
        if len(string) - idx >= 2:
            if string[idx:idx+2] == '10':
                idx += 2
                state = 1
            elif string[idx:idx+2] == '01':
                idx += 2
            else:
                break
        else:
            break
    elif state == 1:
        if len(string) - idx >= 1:
            if string[idx] == '0':
                idx += 1
            elif string[idx] == '1' and string[idx-2] == '0':
                idx += 1
                state = 2
            else:
                break
        else:
            break
    elif state == 2:
        if len(string) - idx >= 1:
            if string[idx] == '0':
                if len(string) - idx >= 2:
                    if string[idx:idx+2] == '00' and string[idx-2] == '1':
                        idx += 2
                        state = 1
                    elif string[idx:idx+2] == '01':
                        idx += 2
                        state = 0
                    else:
                        break
                else:
                    break
            elif string[idx] == '1':
                idx += 1
            else:
                break
        else:
            break

if idx != len(string) or state == 1:
    print('NOISE')
else:
    print('SUBMARINE')