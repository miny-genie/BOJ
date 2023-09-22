# ---------- Main ----------
try:
    while True:
        N = int(input())

        isMulN = "1"

        while True:
            if int(isMulN) % N == 0:
                print(len(isMulN))
                break
                
            else:
                isMulN += "1"

except:
    exit()