
def check():
    global numbers
    for i in range(len(inp2)):
        inp2[i] = str(1 - int(inp2[i]))
        numbers.append(int(''.join(inp2), 2))
        inp2[i] = str(1 - int(inp2[i]))
    
    for i in range(len(inp3)):
        for _ in range(2):
            inp3[i] = str((int(inp3[i]) + 1) % 3)
            num = int(''.join(inp3), 3)
            if num in numbers:
                print('#{} {}'.format(case, num))
                return
        inp3[i] = str((int(inp3[i]) + 1) % 3)


T = int(input())

for case in range(1, T+1):
    inp2 = list(input())
    inp3 = list(input())

    numbers = []

    check()