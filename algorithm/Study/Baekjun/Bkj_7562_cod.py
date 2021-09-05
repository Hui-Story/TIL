import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs():

T = int(input())

for case in range(T):
    knight = list(map(int, input().split()))
    target = list(map(int, input().split()))

    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    