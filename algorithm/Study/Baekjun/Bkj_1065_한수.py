
def check(n):
    gap = 0
    for i in range(len(n)):
        if i == 1:
            gap = int(n[i]) - int(n[i-1])
        elif i >= 2:
            if int(n[i]) - int(n[i-1]) == gap:
                gap = int(n[i]) - int(n[i-1])
                continue
            return False
    else:
        return True

N = int(input())

result = 0
for n in range(1, N+1):
    if check(str(n)):
        result += 1
print(result)