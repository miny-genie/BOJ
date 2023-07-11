# ---------- Import ----------
from itertools import combinations
import sys
input = sys.stdin.readline

# ---------- Main ----------
makeLength, inputLength = map(int, input().split())
text = input().rstrip().split()
text.sort()

for isRight in list(combinations(text, makeLength)):
    aeiou = 0
    aeiouNOT = 0
    
    for check in isRight:
        if check in ["a", "e", "i", "o", "u"]:
            aeiou += 1
        else:
            aeiouNOT += 1
            
    if aeiou > 0 and aeiouNOT > 1:
        print(''.join(isRight)) 
        
# ---------- Comment ----------
# 조건: 3글자 이상이고, 모음이 최소 1개 이상
# 따라서 자동으로 자음 2개 이상을 충족하리라 생각
# 하지만 모음 2개, 3개인 경우에는 미충족, 따라서 자음도 세줘야 함