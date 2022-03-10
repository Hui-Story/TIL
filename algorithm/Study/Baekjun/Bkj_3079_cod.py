import sys
input = sys.stdin.readline

N, M = map(int, input().split())
examiner_lst = [int(input()) for _ in range(N)]
examiner_lst.sort()

