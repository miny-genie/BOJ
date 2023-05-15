# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())

company = {}
for _ in range(N):
    name, condition = input().split()

    if condition == "enter":
        company[name] = condition
    else:
        del company[name]

company = sorted(company.items(), reverse=True)
for name, condition in company:
    print(name)