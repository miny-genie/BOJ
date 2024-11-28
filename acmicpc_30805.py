from sys import stdin
input = stdin.readline


def find_lcs(A: list, B: list):
    numbers = set(A) & set(B)
    result = []
    
    while numbers:
        number = max(numbers)
        result.append(number)
        
        a_idx = A.index(number)
        b_idx = B.index(number)
        
        A = A[a_idx + 1:]
        B = B[b_idx + 1:]
        
        numbers = set(A) & set(B)
        
    return result


_ = int(input())
A = list(map(int, input().split()))
_ = int(input())
B = list(map(int, input().split()))

lcs = find_lcs(A, B)
print(len(lcs))
if lcs:
    print(*lcs)
