from bisect import bisect_left, bisect_right
from sys import stdin
input = stdin.readline


class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size + 2)]
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)
        self.parent[rootX] = rootY


card_count, pick_cards, k = map(int, input().split())
have_cards = sorted(map(int, input().split())) + [0]
submit_cards = list(map(int, input().split()))

uf = UnionFind(card_count)

for submit in submit_cards:
    idx = bisect_right(have_cards, submit)
    card = have_cards[idx]
    root = uf.find(card)
    print(root)
    
    idx = bisect_left(have_cards, root)
    uf.union(have_cards[idx], have_cards[idx+1])

# 25.01.01
# Platinum 1: 2162 > 2163 (+1pts)
# 승급까지 -38 > -37