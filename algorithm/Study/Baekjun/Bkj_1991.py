import sys
input = sys.stdin.readline

def func1(start):
    global dic, result
    result += start
    for i in dic[start]:
        if i != '.':
            func1(i)
    return

def func2(start):
    global dic, result
    cnt = 0
    for i in dic[start]:
        if cnt == 1:
            result += start
        else:
            cnt += 1
        if i != '.':
            func2(i)
    return

def func3(start):
    global dic, result
    for i in dic[start]:
        if i != '.':
          func3(i)
    result += start
    return

N = int(input())

dic = {}

for _ in range(N):
    i, j, k = map(str, input().split())
    dic[i] = [j]
    dic[i].append(k)

result = ''
func1('A')
print(result)

result = ''
func2('A')
print(result)

result = ''
func3('A')
print(result)