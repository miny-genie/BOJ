# ---------- Import ----------
from collections import Counter
import sys
input = sys.stdin.readline


# ---------- Function ----------
def Initialization(words):
    for word in words:
        # how many upper alphabet
        count = 0
        for char in word:
            if char.isupper():
                count += 1
        upper_cnt[word] = count
        
        # what kind of alphabet
        counter = Counter(word.upper())
        alpha_cnt[word] = counter
    return


def findSimilarPair(words):
    count = 0
    
    while words:
        A = words.pop()
        pair = set([A])
        
        for B in words:
            if upper_cnt[A] == upper_cnt[B] and alpha_cnt[A] == alpha_cnt[B]:
                pair.add(B)
                
        if len(pair) > 1:
            length = len(pair)
            count += length * (length-1) // 2
            
        words -= pair
    
    return count


# ---------- Main ----------
for _ in range(int(input())):
    word_cnt, word_len = map(int, input().split())
    words = set(input().rstrip().split())

    upper_cnt = dict()
    alpha_cnt = dict()
    
    Initialization(words)
    answer = findSimilarPair(words)
    print(answer)