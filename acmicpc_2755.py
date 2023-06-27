# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
GPA = 0
totalPoint = 0

point = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7, "F": 0.0
}

for _ in range(N):
    className, credit, grade = map(str, input().split())
    
    GPA += int(credit) * point[grade]
    totalPoint += int(credit)
    
# Round half of even(python3) > Round half up
print(f'{(GPA+0.000001) / totalPoint:.2f}')