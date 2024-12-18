from sys import stdin
input = stdin.readline

MAX = 524_288   # 2 ** 19


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class PersistentSegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.versions = []
        self.versions.append(self.post_init(0, n-1))
    
    def post_init(self, start: int, end: int) -> Node:
        if start == end:
            return Node()
        
        mid = (start + end) // 2
        left_child = self.post_init(start, mid)
        right_child = self.post_init(mid + 1, end)
        
        return Node(0, left_child, right_child)
    
    def update(self, prev_root: Node, start: int, end: int, index: int, value: int) -> Node:
        if start == end:
            return Node(value + 1)
        
        mid = (start + end) // 2
        if index <= mid:
            value = prev_root.left.value
            left_child = self.update(prev_root.left, start, mid, index, value)
            right_child = prev_root.right
        else:
            left_child = prev_root.left
            value = prev_root.right.value
            right_child = self.update(prev_root.right, mid + 1, end, index, value)
        
        v = left_child.value + right_child.value
        return Node(v, left_child, right_child)
    
    def create_version(self, index: int):
        prev_root = self.versions[-1]
        new_root = self.update(prev_root, 0, self.n-1, index, 0)
        self.versions.append(new_root)
    
    def delete_version(self):
        self.versions.pop()
    
    def query(self, root: Node, start: int, end: int, l: int, r: int) -> int:
        if r < start or end < l:
            return 0
        
        if l <= start and end <= r:
            return root.value
        
        mid = (start + end) // 2
        left_result = self.query(root.left, start, mid, l, r)
        right_result = self.query(root.right, mid + 1, end, l, r)
        return left_result + right_result
    
    def range_query(self, version: int, l: int, r: int) -> int:
        return self.query(self.versions[version], 0, self.n-1, l, r)
    
    def xor_query(self, next_node: Node, prev_node: Node, start: int, end: int, x: int) -> int:
        if start == end:
            return start
        
        mid = (start + end) // 2
        lsz = next_node.left.value - prev_node.left.value
        rsz = next_node.right.value - prev_node.right.value
        if (end - start + 1) // 2 & x and lsz or not rsz:
            return self.xor_query(next_node.left, prev_node.left, start, mid, x)
        else:
            return self.xor_query(next_node.right, prev_node.right, mid + 1, end, x)
    
    def get_kth(self, next_node: Node, prev_node: Node, start: int, end: int, k: int) -> int:
        if start == end:
            return start
        
        # lsz: left_size
        lsz = next_node.left.value - prev_node.left.value
        mid = (start + end) // 2
        if lsz >= k:
            return self.get_kth(next_node.left, prev_node.left, start, mid, k)
        else:
            return self.get_kth(next_node.right, prev_node.right, mid + 1, end, k - lsz)


query_count = int(input())
pst = PersistentSegmentTree(MAX)

for _ in range(query_count):
    cmd, *query = list(map(int, input().split()))
    
    # 1 x: 배열 A의 끝에 x를 추가한다.
    if cmd == 1:
        x, = query
        pst.create_version(x)
    
    # 2 L R x: A의 L번째 수부터 R번째 수까지 중에서 x와 xor한 값이 가장 큰 y를 찾아 출력한다.
    elif cmd == 2:
        l, r, x = query
        next_node = pst.versions[r]
        prev_node = pst.versions[l-1]
        xor = pst.xor_query(next_node, prev_node, 0, MAX-1, x)
        print(xor)
    
    # 3 k: 배열 A의 마지막 k개를 제거한다.
    elif cmd == 3:
        k, = query
        for _ in range(k):
            pst.delete_version()
            
    # 4 L R x: A의 L번째 수부터 R번째 수까지 중에서 x보다 작거나 같은 원소의 개수를 출력한다.
    elif cmd == 4:
        l, r, x = query
        upper = pst.range_query(r, 1, x)
        lower = pst.range_query(l-1, 1, x)
        print(upper - lower)
    
    # 5 L R k: A의 L번째 수부터 R번째 수까지 중에서 k번째로 작은 수를 출력한다.
    else:
        l, r, k = query
        next_node = pst.versions[r]
        prev_node = pst.versions[l-1]
        kth = pst.get_kth(next_node, prev_node, 0, MAX-1, k)
        print(kth)

# 24.12.18
# Platinum 1: 2144 > 2151 (+7pts)
# 승급까지 -56 > -49