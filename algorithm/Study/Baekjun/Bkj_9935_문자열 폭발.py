string = str(input())
bomb = str(input())

st = []  # 문자열 저장을 스택으로 구현

for s in string:
    # 새로운 문자마다 'bomb'의 끝자리와 동일한지 판별
    if s == bomb[-1] and len(st)+1 >= len(bomb) :
        # 'bomb'의 뒤에서부터 처음까지 동일하면 스택에서 그만큼 제외
        for idx in range(1, len(bomb)):
            if st[-idx] != bomb[-1-idx]:
                st.append(s)
                break
        else:
            del st[len(st)-len(bomb)+1:]
    else:
        st.append(s)

if st:
    print(''.join(st))
else:
    print('FRULA')