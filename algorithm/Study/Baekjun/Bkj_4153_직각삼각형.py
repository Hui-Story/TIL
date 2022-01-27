import sys
input = sys.stdin.readline

while True:
    tri = list(map(int, input().split()))
    tri.sort()
    if not tri[2]:
        break
    if ((tri[0] * tri[0]) + (tri[1] * tri[1])) == (tri[2] * tri[2]):
        print("right")
    else:
        print("wrong")