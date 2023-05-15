# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
A, B, C = 300, 60, 10
second = int(input())

if second % 10:
    print(-1)
else:
    print(second // A, end=" ")
    second %= A
    
    print(second // B, end=" ")
    second %= B
    
    print(second // C)