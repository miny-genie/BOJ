# ---------- Function ----------
def BigO(a1, a0, c, n0):
    Fn = a1 * n0 + a0
    Gn = c * n0

    if Fn <= Gn and c - a1 >= 0:
        return 1
    else:
        return 0

# ---------- Main ----------
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

print(BigO(a1, a0, c, n0))

# ---------- Commnet ----------
# a1 * n + a0 <= c * n 조건에서 a0가 음수인 경우
# Ex) 5n - 2 <= 3n
# 이런 경우 5(a1)가 3(c)보다 작거나 같아야 식이 성립한다
# 고로 a1 <= c, c - a1 >= 0