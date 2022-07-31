import sys

input = sys.stdin.readline

vowel = 'aeiouAEIOU'

while True:
    sentence = input().strip()
    if sentence == '#':
        break
    answer = 0
    
    for s in sentence:
        if s in vowel:
            answer += 1
    
    print(answer)