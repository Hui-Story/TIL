def overlap(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    print(result)

lst = [12,24,35,24,88,120,155,88,120,155]

overlap(lst)