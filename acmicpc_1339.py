# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def how_many_alphabet(text):
    global score_dict
    
    for i, t in enumerate(text):
        score_dict[t] = score_dict.get(t, 0) + 10 ** (i+1)

# ---------- Main ----------
length = int(input())
text_list = [input().rstrip()[::-1] for _ in range(length)]

# Counting alphabet and give weights
score_dict = {}
for text in text_list:
    how_many_alphabet(text)

# Sorted by weights
sorted_list = sorted(score_dict.items(), key = lambda x: -x[1])

# Give number using ascii code
count = 57
score_dict = {}
for alphabet, _ in sorted_list:
    score_dict[alphabet] = chr(count)
    count -= 1
    
# Calculating max value
answer = 0
for text in text_list:
    for t in text:
        text = text.replace(t, score_dict[t])
    answer += int(text[::-1])

print(answer)