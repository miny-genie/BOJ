from sys import stdin
input = stdin.readline

INF = float('inf')


class SegmentTree:
    def __init__(self, data: list) -> None:
        self.n = len(data)
        self.tree = [[INF, -INF]] * (2*self.n)    # min_value, max_value
        self.build(data)
    
    def build(self, data: list) -> None:
        # init leaf node
        for i in range(self.n):
            self.tree[i + self.n] = [data[i], data[i]]
        # init parent node
        for i in range(self.n-1, 0, -1):
            even_min, even_max = self.tree[2*i]
            odd_min, odd_max = self.tree[2*i+1]
            self.tree[i] = [
                min(even_min, odd_min),
                max(even_max, odd_max)
            ]
            
    def range_query(self, left: int, right: int) -> tuple:
        def is_odd(num):
            return num % 2
        
        left += self.n
        right += self.n
        min_value, max_value = INF, -INF
        
        while left < right:
            if is_odd(left):
                comp_min, comp_max = self.tree[left]
                min_value = min(min_value, comp_min)
                max_value = max(max_value, comp_max)
                left += 1
                
            if is_odd(right):
                right -= 1
                comp_min, comp_max = self.tree[right]
                min_value = min(min_value, comp_min)
                max_value = max(max_value, comp_max)
            
            left //= 2
            right //= 2
        
        return min_value, max_value


num_count, query_count = map(int, input().split())
nums = [int(input()) for _ in range(num_count)]

seg_tree = SegmentTree(nums)
for _ in range(query_count):
    start, end = map(int, input().split())
    answer = seg_tree.range_query(start-1, end)
    print(*answer)