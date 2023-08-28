# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
IPv6 = list(input().rstrip().split(":"))

# Exception handling
if IPv6[0] == "": IPv6.pop(0)
if IPv6[-1] == "": IPv6.pop()

# Run back condition 2
if len(IPv6) < 8:
    start = IPv6.index("")
    while len(IPv6) < 8:
        IPv6.insert(start, "")

# Run back condition 1
for i, v in enumerate(IPv6):
    if len(v) != 4:
        IPv6[i] = v.zfill(4)

# Print with colons
print(':'.join(IPv6))

# ---------- Comment ----------
# Counter example
# 1:2:3:4:5:6:7::
# ::1:2:3:4:5:6:7
# ::