# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def similar(lst, lst_size):
    cnt = 0

    for start in range(lst_size - 1):
        for end in range(start + 1, lst_size):
            startUpper = sum(c.isupper() for c in lst[start])
            endUpper = sum(c.isupper() for c in lst[end])

            startTxt = ''.join(sorted(lst[start].upper()))
            endTxt = ''.join(sorted(lst[end].upper()))

            if startUpper == endUpper and startTxt == endTxt:
                cnt += 1

    return cnt

# ---------- Main ----------
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    words = list(map(str, input().split()))

    print(similar(words, N))