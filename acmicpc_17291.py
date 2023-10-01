# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
total = [0] * 21
new = [0] * 21

new[1], new[2], new[3] = 1, 1, 2
total[1], total[2], total[3] = 1, 2, 4

year = int(input())
for i in range(4, year+1):
    new[i] = total[i-1]
    total[i] = new[i] + total[i-1]
    
    if (i-3) % 2 == 1:
        total[i] -= new[i-3]
        
    if (i-4) % 2 == 0:
        total[i] -= new[i-4]
        
print(total[year])