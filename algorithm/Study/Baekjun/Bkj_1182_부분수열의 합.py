def sub(i):
    global sub_arr, result
    if i == N:
        if sub_arr and sum(sub_arr) == S:
            result += 1
        return
    sub_arr.append(arr[i])
    sub(i+1)
    sub_arr.pop()
    sub(i+1)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
sub_arr = []
result = 0

sub(0)

print(result)