word = str(input())

for i in range(len(word)//2+1):
    if word[i] != word[len(word)-i-1]:
        print(word)
        break
else:
    print(word)
    print('입력하신 단어는 회문(Palindrome)입니다.')