# ---------- Import ----------
from collections import Counter
import sys
input = sys.stdin.readline

# ---------- Main ----------
DNA_len, sub_len = map(int, input().split())
DNA = "!" + input().rstrip()
A, C, G, T = map(int, input().split())

substr = Counter(DNA[:sub_len])

count = 0
for i in range(1, DNA_len - sub_len + 2):
    head = i - 1
    tail = i + sub_len - 1
    
    substr[DNA[head]] -= 1
    substr[DNA[tail]] = substr.get(DNA[tail], 0) + 1    
    
    if substr['A'] >= A and substr['C'] >= C\
    and substr['G'] >= G and substr['T'] >= T:
        count += 1
        
print(count)