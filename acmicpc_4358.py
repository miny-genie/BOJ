# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
cnt = 0
dict_ = {}

while True:
    tree = input().rstrip()
    if not tree: break
    
    dict_[tree] = dict_.get(tree, 0) + 1
    cnt += 1

for t, c in sorted(dict_.items()):
    ratio = round(c / cnt * 100, 4)
    print(f'{t} {ratio:.4f}')