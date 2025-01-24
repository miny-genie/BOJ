from sys import stdin
input = stdin.readline

MAX = 100_005


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class PersistentSegmentTree:
    def __init__(self, n: int, arr: list):
        self.n = n
        self.arr = arr
        self.versions = []  # 각 버전의 루트 노트 저장
        self.versions.append(self.build(0, n-1))
    
    def build(self, start: int, end: int) -> Node:
        if start == end:
            return Node(self.arr[start])
        
        mid = (start + end) // 2
        left_child: Node = self.build(start, mid)
        right_child: Node = self.build(mid + 1, end)
        
        return Node(left_child.value + right_child.value, left_child, right_child)
    
    def update(self, prev_root: Node, start: int, end: int, index: int, value: int) -> Node:
        if start == end:
            return Node(value)
        
        mid = (start + end) // 2
        if index <= mid:
            left_child = self.update(prev_root.left, start, mid, index, value)
            right_child = prev_root.right
        else:
            left_child = prev_root.left
            right_child = self.update(prev_root.right, mid + 1, end, index, value)
        
        v = left_child.value + right_child.value
        return Node(v, left_child, right_child)
    
    def create_version(self, index: int, value: int):
        prev_root = self.versions[-1]
        new_root = self.update(prev_root, 0, self.n-1, index, value)
        self.versions.append(new_root)
    
    def query(self, root: Node, start: int, end: int, l: int, r: int):
        if r < start or end < l:
            return 0
        
        if l <= start and end <= r:
            return root.value
        
        mid = (start + end) // 2
        left_result = self.query(root.left, start, mid, l, r)
        right_result = self.query(root.right, mid + 1, end, l, r)
        return left_result + right_result
    
    def range_query(self, version: int, l: int, r: int):
        return self.query(self.versions[version], 0, self.n-1, l, r)


num_count = int(input())
nums = list(map(int, input().split()))

pst = PersistentSegmentTree(num_count, nums)

query_count = int(input())
for _ in range(query_count):
    cmd, *rem = list(map(int, input().split()))
    
    if cmd == 1:
        index, value = rem
        pst.create_version(index-1, value)
    
    else:
        version, left, right = rem
        answer = pst.range_query(version, left-1, right-1)
        print(answer)

# 25.01.25
# Platinum 1: 2188 > 2189 (+1pts)
# 승급까지 -12 > -11