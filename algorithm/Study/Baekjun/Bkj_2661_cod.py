def good_seq(idx):
    global N, st, result
    if idx == N:
        numbers = ''.join(map(str, st))
        result.append(int(numbers))
        return
    for i in range(1, 4):
        if st:
            st.append(i)
            if check(i, idx):
                good_seq(idx+1)
                st.pop()
            else:
                st.pop()
                continue
        else:
            st.append(i)
            good_seq(idx+1)
            st.pop()
    return

def check(i, idx):
    global st
    for j in range(len(st)-2, int(idx/2)-1, -1):
        if i == st[j]:
            for k in range(idx-j):
                if (j-k) >= 0:
                    if st[idx-k] != st[j-k]:
                        break
                else:
                    continue
            else:
                return False
    return True


N = int(input())
st = []
result = []

good_seq(0)
print(min(result))