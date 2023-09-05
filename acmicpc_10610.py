# ---------- Main ----------
num = sorted(list(input()), reverse=True)

if num[-1] == '0':
    if sum(map(int, num[:-1])) % 3 == 0:
        print(''.join(num))
    else:
        print(-1)
    
else:
    print(-1)