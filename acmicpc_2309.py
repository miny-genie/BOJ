# ---------- Import ----------
from itertools import combinations
import sys
input = sys.stdin.readline

# ---------- Main ----------
lst = []
for _ in range(9):
    lst.append(int(input()))
lst.sort()

SUM = sum(lst)  # lst 합계
checkNum = list(combinations(lst, 2))   # 뺄 항목을 구하기 위한 list

# 9명 중 2명만 거짓쟁이, 2명을 빼서 100이 되도록 확인
for one, two in checkNum:
    if SUM - (one + two) == 100:
        lst.remove(one)
        lst.remove(two)
        break

# lst 출력
for i in lst:
    print(i)