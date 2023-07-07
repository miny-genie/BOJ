# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = input().rstrip()
length = len(N)

# Calculating 'comment equation' before plus
result = 0
for i in range(1, length):
    result += 9 * (10 ** (i-1)) * i

# Calculating 'comment equation' after plus
result += (int(N) - ((10 ** (length-1)) - 1)) * length

print(result)
    
# ---------- Comment ----------
# 1~9           0 = 9*0
# 0 + (N-0)*1

# 10~99         9 = 9*1 = 9*10^0*1
# 9 + (N-9)*2

# 100~999       180 = 90*2 = 9*10^1*2
# 189 + (N-99)*3

# 1000~9999     2700 = 900*3 = 9*10^2*3
# 2889 + (N-999)*4