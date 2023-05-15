# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
while True:
    try:
        hypen = "-"
        for _ in range(int(input())):
            hypen = hypen + (" " * len(hypen)) + hypen
            
        print(hypen)
        
    except EOFError:
        break
    
# ---------- Comment ----------
# 백준에 제출할 때는 ValueError
# Import 구문을 제외하든, int(input().rstrip()) 처리하든