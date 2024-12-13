from sys import stdin
input = stdin.readline


class SegmentTree:
    def __init__(self, n: int, arr: list):
        self.n = n
        self.arr = arr
        self.tree = [float('inf') for _ in range(4 * n)]
        self.post_init(node=0, start=0, end=n-1)
    
    def post_init(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            self.post_init(left_child, start, mid)
            self.post_init(right_child, mid + 1, end)
            self.tree[node] = min(self.tree[left_child], self.tree[right_child])
    
    def query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        if r < start or end < l:
            return float('inf')
        
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        left_min = self.query(left_child, start, mid, l, r)
        right_min = self.query(right_child, mid + 1, end, l, r)
        
        return min(left_min, right_min)
    
    def range_query(self, l: int, r: int) -> int:
        return self.query(node=0, start=0, end=self.n-1, l=l, r=r)


num_count, query_count = map(int, input().split())
nums = [int(input()) for _ in range(num_count)]

st = SegmentTree(num_count, nums)

for _ in range(query_count):
    l, r = map(lambda x: int(x)-1, input().split())
    min_value = st.range_query(l, r)
    print(min_value)

# 24.12.14
# Platinum 1: 2141 > 2141 (+0pts)
# 승급까지 -59 > -59