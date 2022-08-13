word = input()
answer = ''

for w in word:
    if w.islower():
        answer += w.upper()
    else:
        answer += w.lower()

print(answer)