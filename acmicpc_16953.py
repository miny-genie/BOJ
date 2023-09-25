# -------------------- Case 1 --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
before, after = map(int, input().split())
count = 1

while True:
    if after < before:
        print(-1); break
    
    if before == after:
        print(count); break
    
    if after % 10 == 1:
        after = (after - 1) // 10
        count += 1
        
    elif after % 2 == 0:
        after //= 2
        count += 1
        
    else:
        print(-1); break


# -------------------- Case 2 --------------------
# ---------- Function ----------
def cal(buf, depth):
    global answer
    
    if buf == B:
        answer = depth
    elif buf > B:
        return
    
    cal(buf * 2, depth+1)
    cal(buf * 10 + 1, depth + 1)
    
    return
        
# ---------- Main ----------
A, B = map(int, input().split())
answer = -1

cal(A, 1)
print(answer)