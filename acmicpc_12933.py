# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
INPUT = list(input().rstrip())
checkList = [0] * len(INPUT)
QUACK = ["q", "u", "a", "c", "k"]

# 'quack' len is 5, so INPUT must be multiply 5
if len(INPUT) % 5 != 0:
    print(-1); exit()

result = 0
for start in range(len(INPUT)):
    index, isFirst = 0, 1
        
    for i in range(start, len(INPUT)):
        if INPUT[i] == QUACK[index] and not checkList[i]:
            checkList[i] = 1
            
            if INPUT[i] == "k":
                index = 0
                
                # First visit 'k'
                if isFirst:
                    result += 1
                    isFirst = 0
                
            else:
                index += 1
        
print(result) if result and all(checkList) else print(-1)