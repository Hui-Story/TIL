words = list(map(str, input().split(', ')))

def long(words):
    result = ''
    for word in words:
        if len(word) > len(result):
            result = word
    print(result)

long(words)