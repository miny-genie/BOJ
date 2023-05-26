# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
treeCnt, treeLength = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
while start <= end:
    mid = (start + end) // 2

    totalLength = 0
    for tree in trees:
        if tree > mid:
            totalLength += tree - mid

    # length is enough, so cut higher
    if totalLength >= treeLength:
        start = mid + 1

    # length is not enough, so cut lower
    else:
        end = mid - 1

# not mid
print(end)