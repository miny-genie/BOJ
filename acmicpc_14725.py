from sys import stdin
input = stdin.readline


def add_to_trie(trie, food_chain):
    node = trie
    for food in food_chain:
        if food not in node:
            node[food] = dict()
        node = node[food]
        
        
def print_trie(trie, depth=0):
    for food in sorted(trie):
        print("--" * depth + food)
        print_trie(trie[food], depth + 1)
        
        
trie = dict()
for _ in range(int(input())):
    _, *food_chain = list(input().rstrip().split())
    add_to_trie(trie, food_chain)
    
print_trie(trie)