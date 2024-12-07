from bisect import bisect_right
from sys import stdin
input = stdin.readline


class MergeSortTree:
    def __init__(self, n: int, arr: list):
        self.n = n
        self.arr = arr
        self.tree = [[] for _ in range(4 * n)]
        self.build(node=0, start=0, end=n-1)
    
    def build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = [self.arr[start]]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            self.build(left_child, start, mid)
            self.build(right_child, mid + 1, end)
            self.tree[node] = sorted(self.tree[left_child] + self.tree[right_child])
    
    def _query(self, node: int, start: int, end: int, l: int, r: int, k: int) -> int:
        if r < start or end < l:
            return 0
         
        if l <= start and end <= r:
            return len(self.tree[node]) - self.upper_bound(self.tree[node], k)
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_result = self._query(left_child, start, mid, l, r, k)
        right_result = self._query(right_child, mid + 1, end, l, r, k)
        return left_result + right_result
    
    def upper_bound(self, sorted_list: list, k: int) -> int:
        return bisect_right(sorted_list, k)
    
    def range_query(self, l, r, k):
        return self._query(node=0, start=0, end=self.n-1, l=l, r=r, k=k)


n = int(input())
nums = list(map(int, input().split()))
ms_tree = MergeSortTree(n, nums)

for _ in range(query_count := int(input())):
    l, r, k = map(int, input().split())
    upper_count = ms_tree.range_query(l-1, r-1, k)
    print(upper_count)


# 24.12.07
# Platinum 1: 2119 > 2122 (+3pts)
# 승급까지 -81 > -78