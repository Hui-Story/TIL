
def binary_search(target):
    s, e = 0, N - 1
    cnt = 0
    while s <= e:
        mid = (s + e) // 2
        if cards[mid] < target:
            s = mid + 1
        elif cards[mid] > target:
            e = mid - 1
        else:
            cnt = 1
            l, r = mid - 1, mid + 1
            while l >= 0 and cards[l] == target:
                cnt += 1
                l -= 1
            while r < N and cards[r] == target:
                cnt += 1
                r += 1
            break
    result.append(cnt)


N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
targets = list(map(int, input().split()))
result = []

for target in targets:
    binary_search(target)

print(*result)