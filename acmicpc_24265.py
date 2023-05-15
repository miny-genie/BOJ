# ---------- Function ----------
'''
def MenOfPassion(lst, N):
    sum = 0

    for i in range(N):
        for j in range(i+1, N):
            #sum += lst[i] * lst[j]
            sum += 1

    return sum
'''

# ---------- Main ----------
N = int(input())

print(N*(N-1)//2)
print(2)