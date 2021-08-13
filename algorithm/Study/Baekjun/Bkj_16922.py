N = int(input())
Numbers = [1, 5, 10, 50]

result = []

def Rome_num(count, total, used):
    global N, result, Numbers
    if count == 3:
        total += Numbers[3] * (N-used)
        if total in result:
            return
        else:
            result.append(total)
            return
    for i in range(0, N+1-used):
        total += Numbers[count] * i
        used += i
        count += 1
        Rome_num(count, total, used)
        used -= i
        count -= 1
        total -= Numbers[count] * i


Rome_num(0, 0, 0)
print(len(result))