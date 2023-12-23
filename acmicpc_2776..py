# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
for _ in range(int(input())):
    _ = int(input())
    notepad_one = set(map(int, input().split()))
    
    _ = int(input())
    notepad_two = list(map(int, input().split()))
    
    for two in notepad_two:
        print(1) if two in notepad_one else print(0)