from sys import stdin, setrecursionlimit
setrecursionlimit(int(1e6))
input = stdin.readline


def make_sub_tree_dp(current: int, parent: int) -> dict:
    sub_tree[current] += 1
    for child in connect_info[current]:
        if child != parent:
            make_sub_tree_dp(child, current)
            sub_tree[current] += sub_tree[child]


# First line input
vertex_count, root, query_count = map(int, input().split())

# Generate vertex connect info
connect_info = [[] for _ in range(vertex_count + 1)]
for _ in range(vertex_count - 1):
    u, v = map(int, input().split())
    connect_info[u].append(v)
    connect_info[v].append(u)

# Count sub_tree vertices using dp
sub_tree = [0] * (vertex_count + 1)
make_sub_tree_dp(current=root, parent=-1)

# Do query
for _ in range(query_count):
    sub_root = int(input())
    print(sub_tree[sub_root])

# 24.12.19
# Platinum 1: 2151 > 2151 (+0pts)
# 승급까지 -49 > -49