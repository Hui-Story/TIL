N = [list(map(int, input().split())) for _ in range(19)]

def func1(N):
    for y in range(19):
        for x in range(19):
            for player in range(1, 3):
                if N[y][x] == player:
                    count = 1
                    if x == 0 and N[y][x+1] == player:
                        count += 1
                        for i in range(2, 6):
                            if N[y][x+i] == player:
                                count += 1
                            else:
                                break
                        if count == 5:
                            print(player)
                            print(y+1, x+1)
                            return
                    elif 0 < x < 15 and N[y][x-1] != player and N[y][x+1] == player:
                        count += 1
                        if x < 14:
                            for i in range(2, 6):
                                if N[y][x+i] == player:
                                    count += 1
                                else:
                                    break
                        elif x == 14:
                            for i in range(2, 5):
                                if N[y][x+i] == player:
                                    count += 1
                                else:
                                    break
                        if count == 5:
                            print(player)
                            print(y+1, x+1)
                            return
                    count = 1
                    if (x == 0 or y == 0) and x < 15 and y < 15 and N[y+1][x+1] == player:
                        count += 1
                        if x < 14 and y < 14:
                            for i in range(2, 6):
                                if N[y+i][x+i] == player:
                                    count += 1
                                else:
                                    break
                        elif x == 14 or y == 14:
                            for i in range(2, 5):
                                if N[y+i][x+i] == player:
                                    count += 1
                                else:
                                    break
                        if count == 5:
                            print(player)
                            print(y+1, x+1)
                            return
                    elif 0 < x < 15 and 0 < y < 15 and N[y-1][x-1] != player and N[y+1][x+1] == player:
                        count += 1
                        if x < 14 and y < 14:
                            for i in range(2, 6):
                                if N[y+i][x+i] == player:
                                    count += 1
                                else:
                                    break
                        elif x == 14 or y == 14:
                            for i in range(2, 5):
                                if N[y+i][x+i] == player:
                                    count += 1
                                else:
                                    break
                        if count == 5:
                            print(player)
                            print(y+1, x+1)
                            return
                    count = 1
                    if y == 0 and N[y+1][x] == player:
                        count += 1
                        for i in range(2, 6):
                            if N[y+i][x] == player:
                                count += 1
                            else:
                                break
                        if count == 5:
                            print(player)
                            print(y+1, x+1)
                            return
                    elif 0 < y < 15 and N[y-1][x] != player and N[y+1][x] == player:
                        count += 1
                        if y < 14:
                            for i in range(2, 6):
                                if N[y+i][x] == player:
                                    count += 1
                                else:
                                    break
                        elif y == 14:
                            for i in range(2, 5):
                                if N[y+i][x] == player:
                                    count += 1
                                else:
                                    break
                        if count == 5:
                            print(player)
                            print(y+1, x+1)
                            return
                    count = 1
                    if (x == 18 or y == 0) and N[y+1][x-1] == player:
                        count += 1
                        if y < 14 or x > 4:
                            for i in range(2, 6):
                                if N[y+i][x-i] == player:
                                    count += 1
                                else:
                                    break
                        elif y == 14 or x == 4:
                            for i in range(2, 5):
                                if N[y+i][x-i] == player:
                                    count += 1
                                else:
                                    break
                        if count == 5:
                            print(player)
                            print(y+5, x-3)
                            return
                    elif 18 > x > 3 and 0 < y < 15 and N[y-1][x+1] != player and N[y+1][x-1] == player:
                        count += 1
                        if y < 14 or x > 4:
                            for i in range(2, 6):
                                if N[y+i][x-i] == player:
                                    count += 1
                                else:
                                    break
                        elif y == 14 or x == 4:
                            for i in range(2, 5):
                                if N[y+i][x-i] == player:
                                    count += 1
                                else:
                                    break
                        if count == 5:
                            print(player)
                            print(y+5, x-3)
                            return
    else:
        print(0)

func1(N)