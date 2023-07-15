# ---------- Import ----------
# from itertools import product
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
answer = bin(N+1)[3:]
print(answer.replace("0", "4").replace("1", "7"))

# # -------------------- Case 1: TLE --------------------
# N = int(input())
# result, digit = 0, 0

# # digit자릿수, N번째
# while True:
#     digit += 1
#     result += 2 ** digit
#     if N <= result: break
    
# N -= result - 2 ** (digit)

# for i, num in enumerate(product(["4", "7"], repeat=digit)):
#     if i == N-1:
#         print(int(''.join(num)))
#         break

# # -------------------- Case 2: AC --------------------
# N = int(input())
# result, digit = 0, 0

# while True:
#     digit += 1
#     result += 2 ** digit
#     if N <= result: break
    
# N -= result - 2 ** (digit)

# # 자릿수에 해당하는 숫자 만들기
# answer = list("4" * digit)
# digits = bin(N-1)[2:].zfill(digit)

# for i, v in enumerate(digits):
#     if v == "1": answer[i] = "7"
        
# print(''.join(answer))

# # -------------------- Case 3: AC --------------------
# N = int(input())
# result, digit = 0, 0

# while True:
#     digit += 1
#     result += 2 ** digit
#     if N <= result: break
    
# N -= result - 2 ** (digit)

# # 자릿수에 해당하는 숫자 만들기
# digits = bin(N-1)[2:].zfill(digit)
# print(digits.replace("0", "4").replace("1", "7"))

# # -------------------- Case 4: Test Code --------------------
# for N in range(1, 11):
#     print(str(bin(N)), end=" ")
#     print(str(bin(N))[3:], end=" ")
#     print(str(bin(N + 1)), end=" ")
#     print(str(bin(N + 1))[3:])
    
# # -------------------- Case 5: AC, Using Case 4 theory --------------------
# # Main