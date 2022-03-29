import sys, math
input = sys.stdin.readline

N = int(input())
crane_loads = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
boxs = sorted(list(map(int, input().split())), reverse=True)

if max(boxs) > max(crane_loads):
    print(-1)
    exit()

