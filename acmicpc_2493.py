# # -------------------- Case 1: TLE --------------------
# # ---------- Import ----------
# import sys
# input = sys.stdin.readline

# # ---------- Main ----------
# _ = int(input())
# buildings = list(map(int, input().split()))

# stack = []

# for now in buildings:
#     while True:
#         if stack and stack[-1] < now:
#             stack.pop()
        
#         else:
#             break
        
#     print(buildings.index(stack[-1])+1, end=" ") if stack else print(0, end=" ")
#     stack.append(now)
    
# # ---------- Comment ----------
# # TLE: L20 index, can raise linear time complex; O(N)


# -------------------- Case 2: AC --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
_ = int(input())
buildings = list(map(int, input().split()))

stack = []

for idx, now in enumerate(buildings):
    while stack and stack[-1][0] < now:
        stack.pop()
        
    if stack:
        print(stack[-1][1], end=" ")
    else:
        print(0, end=" ")
        
    stack.append((now, idx + 1))
