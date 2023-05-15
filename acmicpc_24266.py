# ---------- Function ----------
'''
def MenOfPassion(lst, N):
    sum = 0

    for i in range(N-1):
        for j in range(i+1, N):
            for k in range(j+1, N):
                sum += lst[i] * lst[j] * lst[k]

    return sum
'''

# ---------- Main ----------
N = int(input())

print(N * (N-1) * (N-2) // 6)
print(3)