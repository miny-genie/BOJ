# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
dict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
total, tmp = 0.0, 0.0

for _ in range(20):
    name, score_num, score_eng = map(str, input().split())

    if score_eng == "P":
        continue

    total += dict[score_eng] * float(score_num)
    tmp += float(score_num)

print(total / tmp)