# ---------- Import ----------
import re
import sys
input = sys.stdin.readline


# ---------- Function ----------
def makeSubSet(words):
    subset = []
    
    for word in words:
        for sub in subset:
            if re.match(word, sub):
                break
        else:
            subset.append(word)
    
    return subset


# ---------- Main ----------
words = [input().rstrip() for _ in range(int(input()))]

answer = makeSubSet(sorted(words, key=lambda x: -len(x)))
print(len(answer))