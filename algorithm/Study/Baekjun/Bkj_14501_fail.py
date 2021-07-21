N = int(input())

a = []
b = []
for i in range(N):
    a_input, b_input = input().split()
    a.append(a_input)
    b.append(b_input)

profit = 0
for i in range(N):
    for j in range(N):
