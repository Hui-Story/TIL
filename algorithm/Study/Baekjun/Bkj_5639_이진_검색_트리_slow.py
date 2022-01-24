import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def search(now_tree):
    if not len(now_tree):
        return
    if len(now_tree) == 1:
        print(now_tree[0])
        return
    for i in range(1, len(now_tree)):
        if now_tree[i] > now_tree[0]:
            search(now_tree[1:i])
            search(now_tree[i:])
            print(now_tree[0])
            return
    search(now_tree[1:])
    print(now_tree[0])


tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

search(tree)