# -------------------- Case 1 --------------------
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


# -------------------- Case 2 --------------------
# ---------- Main ----------
try:
    while True:
        N = int(input())

        isMulN = 1
        length = 1
        
        while True:
            if isMulN % N == 0:
                print(length)
                break
                
            else:
                isMulN = (isMulN * 10) % N + 1
                length += 1

except:
    exit()