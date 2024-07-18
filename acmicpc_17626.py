def solution(n: int) -> int:
    if (n**.5).is_integer():
        return 1
    
    square_set = {i*i for i in range(1, int(n**.5)+1)}
    for i in square_set:
        if n - i in square_set:
            return 2
    
    # lagrange_theorem
    while n % 4 == 0:
        n //= 4
    return 4 if n % 8 == 7 else 3


print(solution(int(input())))