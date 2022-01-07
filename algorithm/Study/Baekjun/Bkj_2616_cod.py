from itertools import accumulate

N = int(input())
passengers = list(map(int, input().split()))
max_train = int(input())

passengers = list(accumulate(passengers))
prefix_sum = passengers[:]

for i in range(max_train, N):
    passengers[i] -= prefix_sum[i - max_train]

print(passengers)