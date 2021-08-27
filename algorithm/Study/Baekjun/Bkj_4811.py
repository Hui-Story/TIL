import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    result = 1
    for i in range(N-1):
        result = result*3 - 1
    
    print(result)