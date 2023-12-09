# ---------- Import ----------
from itertools import combinations
import sys
input = sys.stdin.readline

# ---------- Function ----------
def word2bit(word):
    bit = 0
    for char in word:
        bit |= 1 << (ord(char) - ord('a'))
    return bit

# ---------- Main ----------
length, teaching = map(int, input().split())
words = [input().rstrip() for _ in range(length)]
words2bit = list(map(word2bit, words))
must = word2bit('acint')

if teaching < 5:
    print(0)
    
else:
    alphabet = [1 << i for i in range(26) if not (must & 1 << i)]
    answer = 0
    
    for combination in combinations(alphabet, teaching-5):
        possible = sum(combination) | must
        
        count = 0
        for bit in words2bit:
            if bit & possible == bit:
                count += 1
                
        answer = max(answer, count)
    
    print(answer)