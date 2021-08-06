S = input()

num_0 = 0
num_1 = 0
num_data = int(S[0])

for number in S:
    if number == '0' and num_data == 0:
        num_data += 1
        num_0 += 1
    elif number == '1' and num_data == 1:
        num_data -= 1
        num_1 += 1

print(min(num_0, num_1))