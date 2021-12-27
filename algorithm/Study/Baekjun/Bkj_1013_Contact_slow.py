import sys
input = sys.stdin.readline

for _ in range(int(input())):
    word = str(input().strip())

    while word:
        if word[:2] == '01':
            word = word[2:]
        elif word[:3] == '100':
            word = word[2:]
            idx_1100, idx_10 = word.find('1100'), word.find('10')
            if idx_10 != -1:
                if idx_1100 + 1 == idx_10:
                    word = word[idx_10:]
                else:
                    word = word[idx_10 + 1:]
            else:
                idx_01 = word.find('01')
                if idx_01 != -1:
                    print('YES')
                else:
                    print('NO')
                break
        else:
            print('NO')
            break
    else:
        print('YES')