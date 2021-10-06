
def ticket_3(vacation, idx, coupon):
    global result
    while idx < N-2:
        if sum(vacation[idx:idx+3]) == 30000:
            vacation[idx] = 25000
            vacation[idx+1] = vacation[idx+2] = 0
            coupon += 1
            idx += 3
        elif vacation[idx] == 10000 and vacation[idx+1] == 10000:
            vacation[idx] = 25000
            vacation[idx+1] = 0
            ticket_3(vacation, idx+3, coupon+1)
            vacation[idx] = 10000
            vacation[idx+1] = 10000
            idx += 1
        elif vacation[idx] == 10000 and vacation[idx+2] == 10000:
            vacation[idx] = 25000
            vacation[idx+2] = 0
            ticket_3(vacation, idx+3, coupon+1)
            vacation[idx] = 10000
            vacation[idx+2] = 10000
            idx += 1
        else:
            idx += 1
        if coupon >= 3:
            for i in range(idx, N):
                if vacation[i] == 10000:
                    vacation[i] = 0
                    ticket_3(vacation, idx+1, coupon-3)
                    vacation[i] = 10000
    ticket_5()

def ticket_5():
    pass


N, M = map(int, input().split())
vacation = [10000] * (N)

for i in list(map(int, input().split())):
    vacation[i-1] = 0

result = 2e+10
ticket_3(vacation, 0, 0)

print(result)