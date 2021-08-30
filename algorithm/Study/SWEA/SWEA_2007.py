T = int(input())

for case in range(1, T+1):
    words = str(input())

    pattern = str(words[0])
    idx = 0

    for i in range(20):
        if words[i] == pattern[idx]:
            idx += 1
            if idx == len(pattern):
                idx = 0
        else:
            idx = 0
            if len(pattern) <= 10:
                pattern = str(words[:i+1])
    
    print('#{} {}'.format(case, len(pattern)))