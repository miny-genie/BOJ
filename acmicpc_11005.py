# ---------- Import ----------
import sys, string
input = sys.stdin.readline

# ---------- Main ----------
num, B = map(int, input().split())
string = "0123456789" + string.ascii_uppercase
ans = ""

while num != 0:
    ans += string[num % B]
    num //= B

print(ans[::-1])