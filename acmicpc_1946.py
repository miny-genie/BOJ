# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT = int(input())

for _ in range(caseT):
    people = int(input())
    grade = [list(map(int, input().split())) for _ in range(people)]
    
    grade = sorted(grade, key = lambda x: x[0])
    
    answer = 0
    compare = people + 1
    
    for _, v in grade:
        if v < compare:
            answer += 1
        compare = v
        
    print(answer)