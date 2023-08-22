# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
positive = []
negative = []

length, limit = map(int, input().split())
books = list(map(int, input().split()))

for v in books:
    if v > 0: positive.append(v)
    else: negative.append(-v)
    
positive = sorted(positive, reverse=True)[::limit]
negative = sorted(negative, reverse=True)[::limit]

if not positive: MAX = negative[0]
elif not negative: MAX = positive[0]
else: MAX = max(positive[0], negative[0])

print(2 * (sum(positive) + sum(negative)) - MAX)

    
# ---------- Comment ----------
# 7 2
# -37 2 -6 -39 -29 11 -28
# 131 

# 8 3
# -18 -9 -4 50 22 -26 40 -45
# 158

# 6 2
# 3 4 5 6 11 -1
# 29

# 1 50
# 1
# 1