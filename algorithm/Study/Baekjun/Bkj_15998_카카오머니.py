import sys, math
input = sys.stdin.readline

N = int(input())
logs = [tuple(map(int, input().split())) for _ in range(N)]
balance = 0
max_balance = 0
charge_lst = []

for a, b in logs:
    if a < 0:
        if -a > balance:
            max_balance = max(max_balance, b)
            diff = b - balance
            charge_lst.append(diff - a)
        else:
            if b != balance - (-a):
                print(-1)
                exit()
    else:
        if (a + balance) != b:
            print(-1)
            exit()
    balance = b

if not charge_lst:
    print(1)
else:
    charge_gcd = math.gcd(*charge_lst)
    if (9 * (10 ** 18) < charge_gcd):
        while charge_gcd > max_balance:
            num = 2
            while not (charge_gcd % num) and num < charge_gcd:
                num += 1
            charge_gcd //= num
    if charge_gcd > max_balance:
        print(charge_gcd)
    else:
        print(-1)