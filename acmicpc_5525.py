# # -------------------- Case 1: Python3 Subtask --------------------
# # ---------- Import ----------
# import sys
# input = sys.stdin.readline

# # ---------- Function ----------
# def makePn(n: int) -> str:
#     length = 2 * n + 1
#     Pn = list("I" * length)
    
#     for i in range(length):
#         if i % 2 != 0: Pn[i] = "O"
    
#     return ''.join(Pn), length

# # ---------- Main ----------
# N = int(input())
# length = int(input())
# text = input().rstrip()

# compareText, compareLength = makePn(N)
# count = 0

# for i in range(length - compareLength + 1):
#     if text[i:i+compareLength] == compareText:
#         count += 1
        
# print(count)


# -------------------- Case 2: Python3 AC --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
S_length = int(input()) + 1
S = list(input().rstrip()); S += S[-1]

START = S[0]
Pn_length, result = 1, 0

for i in range(1, S_length):
    if S[i-1] != S[i]:
        Pn_length += 1
        
    else:
        END = S[i-1]
        
        # Calculating
        O_count = (START, END).count("O")
        Pn_length -= O_count
        
        Pn_length = (Pn_length + 1) // 2
        if Pn_length > N: result += Pn_length - N 
        
        START = S[i]
        Pn_length = 1
        
print(result)

# ---------- Comment ----------
# L38 int(input()) > int(input()) + 1
# L39 getting out dummy data by else condition

# Counter Example
# 2 41 IOOIIOIOIOIOIOIOIOIOOOIOIOIIOIOIOIOIOIOIO > 12(AC)


# -------------------- Case 3: cpp reference --------------------
# # ---------- Import ----------
# import sys
# input = sys.stdin.readline

# # ---------- Main ----------
# N = int(input())
# S_length = int(input())
# S = list(input().rstrip())

# count, answer, beforeI, beforeO = 0, 0, False, False

# for c in S:
#     if c == "I":
#         if beforeI: count = 0
#         if count == N: answer += 1; count -= 1
#         beforeI, beforeO = True, False
    
#     else:
#         if beforeI: count += 1
#         elif beforeO: count = 0
#         beforeO, beforeI = True, False
        
# print(answer)