from sys import stdin
input = stdin.readline

MOD = 1_000_000_007


class SegmentTree:
    def __init__(self, data: list) -> None:
        self.n = len(data)
        self.tree = [1] * (self.n * 2)
        self.build(data)
        
    def build(self, data: list) -> None:
        # init leaf node
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # init parent node
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] * self.tree[2*i+1] % MOD
            
    def update(self, pos: int, value: int) -> None:
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2*pos] * self.tree[2*pos+1] % MOD
    
    def range_query(self, left: int, right: int) -> int:
        def is_odd(num):
            return num % 2
        
        left += self.n
        right += self.n
        answer = 1
        
        while left < right:
            if is_odd(left):
                answer *= self.tree[left]
                left += 1
            if is_odd(right):
                right -= 1
                answer *= self.tree[right]
            left //= 2
            right //= 2
        
        return answer


num_count, change_count, query_count = map(int, input().split())
nums = [int(input()) for _ in range(num_count)]

seg_tree = SegmentTree(nums)

for _ in range(change_count + query_count):
    op, a, b = map(int, input().split())
    
    if op == 1:
        seg_tree.update(a-1, b)
    else:
        answer = seg_tree.range_query(a-1, b) % MOD
        print(answer)