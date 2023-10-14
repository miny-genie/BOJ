# -------------------- Python3(31120ms, 44ms) AC --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def divide_section(node_list, depth):
    if not node_list:
        return
    
    mid = len(node_list) // 2
    level[depth].append(node_list[mid])

    divide_section(node_list[:mid], depth+1)
    divide_section(node_list[mid+1:], depth+1)
    
    return

# ---------- Main ----------
K = int(input())
level = [[] for _ in range(K)]
node_list = list(map(int, input().split()))

divide_section(node_list, 0)

for line in level:
    print(*line)