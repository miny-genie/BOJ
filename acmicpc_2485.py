# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a

# ---------- Main ----------
N = int(input())
tree, interval = [], []

# INPUT tree location
for _ in range(N):
    tree.append(int(input()))

# Calculate tree interval
for index in range(len(tree) - 1):
    interval.append(tree[index+1] - tree[index])

# Calculate Interval's GCD
GCD = 0
for index in interval:
    GCD = gcd(GCD, index)

cnt = 0
for index in interval:
    cnt += index // GCD - 1

print(cnt)