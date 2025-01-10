from sys import stdin
input = stdin.readline


class SegmentTree:
    def __init__(self, max_flavor=1_000_000):
        self.root = 1
        self.max_flavor = max_flavor
        self.tree = [0] * (4 * max_flavor)

    def _update(self, node: int, start: int, end: int, idx: int, diff: int) -> None:
        if idx < start or idx > end:
            return
        self.tree[node] += diff
        if start != end:
            mid = (start + end) // 2
            self._update(2 * node, start, mid, idx, diff)
            self._update(2 * node + 1, mid + 1, end, idx, diff)
    
    def update(self, flavor: int, count: int):
        """Update the count of a specific candy flavor."""
        self._update(self.root, 1, self.max_flavor, flavor, count)
    
    def _query(self: int, node: int, start: int, end: int, rank: int) -> int:
        if start == end:
            return start
        mid = (start + end) // 2
        if self.tree[2 * node] >= rank:
            return self._query(2 * node, start, mid, rank)
        else:
            return self._query(2 * node + 1, mid + 1, end, rank - self.tree[2 * node])

    def query(self, rank: int) -> int:
        """Find the candy flavor at the given rank."""
        return self._query(self.root, 1, self.max_flavor, rank)


seg_tree = SegmentTree()

query_count = int(input())
for _ in range(query_count):
    cmd, *nums = map(int, input().split())
    
    # A가 1인 경우는 사탕상자에서 사탕을 꺼내는 경우
    if cmd == 1:
        rank, = nums
        flavor = seg_tree.query(rank=rank)
        seg_tree.update(flavor=flavor, count=-1)
        print(flavor)
    
    # A가 2인 경우는 사탕을 넣는 경우
    else:
        flavor, count = nums
        seg_tree.update(flavor=flavor, count=count)

# 25.01.10
# Platinum 1: 2174 > 2175 (+1pts)
# 승급까지 -26 > -25