from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(200000)


def build_preorder(
        inorder: list,
        postorder: list,
        inorder_start: int,
        postorder_start: int,
        postorder_end: int,
    ):
    if postorder_start > postorder_end:
        return

    # last node of postorder is root node of current sub tree
    root_val = postorder[postorder_end]
    preorder.append(root_val)

    # find root node index in inorder tree
    root_index = inorder_index_map[root_val]

    # left sub tree size
    left_size = root_index - inorder_start

    # recursive left sub tree
    build_preorder(
        inorder,
        postorder,
        inorder_start,
        postorder_start,
        postorder_start + left_size - 1
    )
    
    # recursive right sub tree
    build_preorder(
        inorder,
        postorder,
        root_index + 1,
        postorder_start + left_size,
        postorder_end - 1
    )


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_index_map = {value: idx for idx, value in enumerate(inorder)}

preorder = []
build_preorder(inorder, postorder, 0, 0, n - 1)
print(*preorder)

# ---------- Comment ----------
# 17
# 13 10 14 7 4 8 2 1 11 9 17 15 12 16 5 3 6
# 13 14 10 7 8 4 2 11 17 15 16 12 9 5 6 3 1
# >>> 1 2 4 7 10 13 14 8 3 5 9 11 12 15 17 16 6