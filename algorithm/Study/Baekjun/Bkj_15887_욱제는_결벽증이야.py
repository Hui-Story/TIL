N = int(input())
cards = list(map(int, input().split()))

op_lst = []

idx = 0
while idx < N-1:
    if cards[idx] != (idx+1):
        R = cards.index(idx+1)
        op_lst.append([idx+1, R+1])
        cards[idx:R+1] = cards[idx:R+1][::-1]
    idx += 1

print(len(op_lst))
for op in op_lst:
    print(*op)