A = int(input())
B = str(input())

for i in range(2, -1, -1):
    print(A * int(B[i]))
print(A * int(B))