# ---------- Import ----------
from collections import defaultdict
import sys
input = sys.stdin.readline

# ---------- Main ----------
text = list(input().rstrip())

dict_ = defaultdict(int)
for t in text:
    dict_[t] += 1

odd_cnt = 0
FLAG = ""
            
answer = ""
for k, v in sorted(dict_.items()):
    answer += k * (v // 2)
    
    if v % 2 == 1:
        odd_cnt += 1
        FLAG = k
        
        if odd_cnt > 1:
            print("I'm Sorry Hansoo")
            exit()
            
print(answer + FLAG + answer[::-1])