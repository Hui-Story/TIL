import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sounds = list(map(str, input().split()))

    other_sound = []
    result = []

    while True:
        S = list(map(str, input().split()))
        if S[-1] == 'say?':
            break
        other_sound.append(S[-1])
    
    for sound in sounds:
        if sound not in other_sound:
            result.append(sound)

    print(*result)