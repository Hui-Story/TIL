N = int(input())
string = input()

word_check = [0] * 26
word_check[ord(string[0]) - 97] = 1
s = e = 0
result = 1

while e < len(string) - 1:
    if word_check[ord(string[e + 1]) - 97]:
        word_check[ord(string[e + 1]) - 97] += 1
        e += 1
    else:
        word_cnt = 0
        for i in word_check:
            if i:
                word_cnt += 1
        if word_cnt == N:
            word_check[ord(string[s]) - 97] -= 1
            s += 1
        else:
            word_check[ord(string[e + 1]) - 97] += 1
            e += 1
    result = max(result, e - s + 1)

print(result)