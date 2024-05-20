from sys import stdin
input = stdin.readline


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)
    
    def build(self, data):
        # init leaf node
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # init inner node
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
    
    def range_query(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left < right:
            if left % 2:
                result += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result


number_count, change_count, prefix_count = map(int, input().split())
numbers = [int(input()) for _ in range(number_count)]

seg_tree = SegmentTree(numbers)
for _ in range(change_count + prefix_count):
    trigger, a, b = list(map(int, input().split()))
    
    if trigger == 1:
        seg_tree.update(a-1, b)
        
    else:
        answer = seg_tree.range_query(a-1, b)
        print(answer)