# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
row, col = map(int, input().split())
nums = [list(map(int, input().rstrip())) for _ in range(row)]
# ''.join(input().rstrip() for _ in range(row))

biggest = 0
for i in range(1 << row*col):
    total = 0
    
    # Calculating by row
    for r in range(row):
        row_sum = 0
        for c in range(col):
            idx = r * col + c
            if i & (1 << idx) != 0:
                row_sum = row_sum * 10 + nums[r][c]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum
        
    # Calculating by col
    for c in range(col):
        col_sum = 0
        for r in range(row):
            idx = r * col + c
            if i & (1 << idx) == False:
                col_sum = col_sum * 10 + nums[r][c]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum

    biggest = max(biggest, total)
    
print(biggest)