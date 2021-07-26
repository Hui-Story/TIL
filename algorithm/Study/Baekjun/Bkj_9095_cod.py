T = int(input())
n = list(int(input()) for _ in range(T))

n_list = []
m_list = []
for i in n:
    for j in range(0, i):
        if j == 0:
            n_list.append(['1'*(j+1)])
        else:
            m_list.append('1'*(j+1))
            for k in n_list[j-1]:
                

        


# 4:
#  1+1+1+1
#  1+1+2
#  1+2+1
#  2+1+1
#  2+2
#  1+3
#  3+1

# 5:
#  1+1+1+1+1
#  1+1+1+2
#  1+1+2+1
#  1+2+1+1
#  2+1+1+1
#  2+2+1
#  2+1+2
#  1+2+2
#  1+1+3
#  1+3+1
#  3+1+1
#  2+3
#  3+2