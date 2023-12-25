# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
holes, _ = map(int, input().split())
items = list(map(int, input().split()))

count = 0
using = set()
empty = holes
for idx, item in enumerate(items):
    if item in using:
        continue
    
    if empty:
        empty -= 1
        using.add(item)
        
    else:
        will_use = items[idx+1:]
        no_more = using - set(will_use)
        
        if len(no_more) == 0:
            tmp, pull = 0, 0
            tmp_plug = set()
            for use in will_use:
                if use in using and use not in tmp_plug:
                    pull = use
                    tmp_plug.add(use)
                    tmp += 1
                    
                if tmp == holes:
                    using.remove(pull)
                    count += 1
                    using.add(item)
                    break
            
        else:
            using.remove(no_more.pop())
            count += 1
            using.add(item)
            
print(count)