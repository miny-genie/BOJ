# -------------------- Case 1: Python3(WA), PyPy3(AC) --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
start = int(input())
end = int(input())
k = int(input())
count = 0

if k % 2:   # odd number
    for i in range(start, end + 1):
        if i % k == 0 and i > k and (i // k) - (k // 2) > 0:
            count += 1
    
else:   # even number
    if k == 2:
        count = end - max(start, 3) + 1

    else:
        for i in range(start, end + 1):
            if i % k == 0 and (i / k) - (k - 1) > 0:
                count += 1

            elif i % k != 0 and i % 2 == 0 and i / k - (k / 2 - 0.5) > 0:
                count += 1     
    
print(count)


# -------------------- Case 2: Python3(31120KB 44ms) AC --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
start = int(input())
end = int(input())
k = int(input())

if k == 2:
    # 1, 2 can not make
    print(max(end - max(start, 3) + 1, 0))
    
elif k == 3:
    # 6 = 1 + 2 + 3
    start = max(start, 6)
    
    # Out of bound
    if start > end:
        print(0)
        
    # The number of 'multiples of 3' within the range
    # is equal to the interval difference divided by 3
    else:
        answer = (end // 3) - (start // 3)
        print(answer+1) if start % 3 == 0 else print(answer)
    
elif k == 4:
    # 10 = 1 + 2 + 3 + 4
    start = max(start, 10)
    
    # Out of bound
    if start > end:
        print(0)
        
    # The number of 'multiples of 2' within the range
    # is equal to the interval difference divided by 2
    else:
        answer = (end // 2) - (start // 2)
        if start <= 12 <= end: answer -= 1  # 12 can not make
        print(answer+1) if start % 2 == 0 else print(answer)
    
else:
    # 15 = 1 + 2 + 3 + 4 + 5
    start = max(start, 15)
    
    # Out of bound
    if start > end:
        print(0)
        
    # The number of 'multiples of 5' within the range
    # is equal to the interval difference divided by 5
    else:
        answer = (end // 5) - (start // 5)
        print(answer+1) if start % 5 == 0 else print(answer)