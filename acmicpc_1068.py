from sys import stdin
input = stdin.readline


class TreeNode:
    def __init__(self, current):
        self.current = current
        self.children = []
        
    def register_child(self, child):
        self.children.append(child)
        

def count_leaf_node(node):
    if not tree[node].children:
        global leaf_node
        leaf_node += 1
        return
    
    for child in tree[node].children:    
        count_leaf_node(child)
        

node_count = int(input())
tree = [TreeNode(i) for i in range(node_count)]
parents = list(map(int, input().split()))
remove_node = int(input())

for node, parent in enumerate(parents):
    if node == remove_node:
        continue
    if parent == -1: root_node = node
    else: tree[parent].register_child(node)
    
try:
    leaf_node = 0
    count_leaf_node(root_node)
except NameError:
    pass

print(leaf_node)