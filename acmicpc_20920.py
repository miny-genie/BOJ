# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, M = map(int, input().split())
words = {}

for _ in range(N):
    word = input().rstrip()

    if len(word) < M: continue

    if not word in words:
        words[word] = 1
    else:
        words[word] += 1

words = sorted(words.items(),\
               key = lambda k: (-k[1], -len(k[0]), k[0]))

for item, value in words:
    print(item)