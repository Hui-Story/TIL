import sys, math
from typing import List

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

class SegmentTree:
    def __init__(self, N: int, A: List[int]) -> None:
        self.N = N
        self.A = A
        h = math.ceil(math.log2(N))
        tree_size = 1 << (h + 1)
        self.tree = [[0, 0] for _ in range(tree_size)]
        self.sum_tree = [0] * tree_size
        self.find_node(1, 1, N)
    
    def find_node(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node][0] = self.A[start]
            self.tree[node][1] = self.A[start]
            self.sum_tree[node] = self.tree[node][0] * self.tree[node][1]
            self.update(node // 2)
        else:
            mid = (start + end) // 2
            self.find_node(node * 2, start, mid)
            self.find_node(node * 2 + 1, mid + 1, end)
    
    def update(self, node: int) -> None:
        while node:
            self.tree[node][0] = self.tree[node * 2][0] + self.tree[node * 2 + 1][0]
            self.tree[node][1] = min(self.tree[node * 2][1], self.tree[node * 2 + 1][1])
            self.sum_tree[node] = self.tree[node][0] * self.tree[node][1]
            node //= 2


N = int(input())
A = [0] + list(MIIS())
segment_tree = SegmentTree(N, A)

print(max(segment_tree.sum_tree))