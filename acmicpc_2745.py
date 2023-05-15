# ---------- Import ----------
import sys, string
input = sys.stdin.readline

# ---------- Main ----------
N, B = input().split()
lst = "0123456789" + string.ascii_uppercase

ans = 0
for i, num in enumerate(N[::-1]):
    ans += (int(B) ** i) * lst.index(num)

print(ans)

# ---------- Comment ----------
# EZ ver
# N, B = input().split()
# print(int(N, int(B)))

'''
N, B = input().split()
B, multiple, ans = int(B), 0, 0

for i in reversed(N):
    if ord(i) < 65:
        ans += int(i) * (B ** multiple)
    else:
        ans += (ord(i) - 55) * (B ** multiple)
    multiple += 1

print(ans)
'''