import sys
input = sys.stdin.readline

NA, NB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A ^ B))