H = int(input())
Y = int(input())

invest_product = {0 : 1.05, 1 : 1.20, 2 : 1.35}
def invest(cost, date):
    now_cost = 0
    for i in range(len(invest_product)):
        now_cost = cost * invest_product[i]

    return invest(now_cost)
    
print(invest(H, Y))