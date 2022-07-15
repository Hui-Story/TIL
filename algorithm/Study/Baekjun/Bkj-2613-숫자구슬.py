from typing import List

MIIS = lambda: map(int, input().split())
Groups = List[int]

def binary_solve(l: int, r: int) -> None:
    
    answer: int = 0
    groups: Groups = []

    while l <= r:
        mid: int = (l + r) // 2
        current_groups: Groups = count_group(mid)
        groups_count: int = len(current_groups)
        if groups_count < M:
            r = mid - 1
            new_groups = check(current_groups, groups_count)
            if len(new_groups) == M:
                answer = mid
                groups = new_groups[:]
        elif groups_count > M:
            l = mid + 1
        else:
            r = mid - 1
            answer = mid
            groups = current_groups[:]
    
    print(answer)
    print(*groups)

def count_group(mid: int) -> Groups:

    groups: Groups = []
    total: int = 0
    count: int = 0

    for marble in marbles:
        if total + marble <= mid:
            total += marble
            count += 1
            continue
        groups.append(count)
        total = marble
        count = 1
    
    groups.append(count)
    
    return groups

def check(groups: Groups, groups_count: int) -> Groups:
    
    new_groups: Groups = []

    for group in groups:
        count: int = group
        while count > 1 and groups_count < M:
            count -= 1
            groups_count += 1
            new_groups.append(1)
        new_groups.append(count)

    return new_groups


N, M = MIIS()
marbles: Groups = list(MIIS())

l: int = max(marbles)
r: int = sum(marbles)

binary_solve(l, r)