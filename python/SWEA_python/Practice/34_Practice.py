word = input()

def palindrome(word):
    new_word = ''
    for i in word:
        new_word = i + new_word
    return new_word

print(palindrome(word))

if word == palindrome(word):
    print('입력하신 단어는 회문(Palindrome)입니다.')