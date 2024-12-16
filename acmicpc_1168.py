from sys import stdin
input = stdin.readline


class SegmentTree:
    def __init__(self, n: int):
        self.tree_size = 1 << n.bit_length()
        self.tree = [0] * (self.tree_size << 1)
        
        # Init leaf node
        for i in range(self.tree_size + 1, self.tree_size + n + 1):
            self.tree[i] = 1
        
        # Init parent node
        for cur in range(self.tree_size - 1, 0, -1):
            left = cur << 1
            self.tree[cur] = self.tree[left] + self.tree[left + 1]
    
    def update(self, noed_index: int):
        while noed_index:
            self.tree[noed_index] -= 1
            noed_index >>= 1
    
    def delete(self, i: int):
        '''Remove i-th element and return index'''
        node_index = 1
        while node_index < self.tree_size:
            node_index <<= 1    # move to left child
            # is need to move right child
            if self.tree[node_index] < i:
                i -= self.tree[node_index]
                node_index += 1 # move to right child
        self.update(node_index)
        return node_index - self.tree_size

def get_josephus_permutation(n: int, k: int) -> list[int]:
    seg_tree = SegmentTree(n)
    result = []
    pos = 0
    step = k - 1
    
    for remain_element in range(n, 0, -1):
        pos = (pos + step) % remain_element
        pop = seg_tree.delete(pos + 1)
        result.append(str(pop))
        
    return result


n, k = map(int, input().split())
josephus_permutation = get_josephus_permutation(n, k)
print(f"<{', '.join(josephus_permutation)}>")

# 24.12.16
# Platinum 1: 2141 > 2144 (+3pts)
# 승급까지 -59 > -56