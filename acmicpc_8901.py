# # -------------------- Case 1: TLE --------------------
# # ---------- Import ----------
# from itertools import product
# import sys
# input = sys.stdin.readline

# # ---------- Function ----------
# def natural_number_divide(num: int):
#     possible = [i for i in range(num+1)]
#     divide = []
    
#     for isDivide in product(possible, repeat = 3):
#         if sum(isDivide) == num:
#             divide.append(isDivide)
            
#     return divide

# # ---------- Main ----------
# caseT = int(input())

# for _ in range(caseT):
#     max_answer = -1e9
    
#     A, B, C = map(int, input().split())
#     price_AB, price_BC, price_CA = map(int, input().split())

#     total_case = (A + B + C) // 2
#     listup = natural_number_divide(total_case)
    
#     for AB, BC, CA in listup:
#         current_price = 0
        
#         if (AB + CA <= A) and (AB + BC <= B) and (BC + CA <= C):
#             current_price += price_AB * AB
#             current_price += price_BC * BC
#             current_price += price_CA * CA
            
#             max_answer = max(max_answer, current_price)
            
#     print(max_answer)


# -------------------- Case 2: AC --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT = int(input())

for _ in range(caseT):
    max_answer = -1e9
    
    A, B, C = map(int, input().split())
    price_AB, price_BC, price_CA = map(int, input().split())
    
    for AB in range(min(A, B)+1):
        BC = min(B - AB, C)
        CA = min(C - BC, A - AB)

        current_price = (price_AB * AB) + (price_BC * BC) + (price_CA * CA)
        max_answer = max(max_answer, current_price)
        
        CA = min(A - AB, C)
        BC = min(B - AB, C - CA)

        current_price = (price_AB * AB) + (price_BC * BC) + (price_CA * CA)
        max_answer = max(max_answer, current_price)
            
    print(max_answer)
    
    