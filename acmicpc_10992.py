from sys import stdin
input = stdin.readline


def print_star(n: int) -> None:
    star = [""] * n
    star[0] = " " * (n - 1) + "*"
    
    for i in range(1, n-1):
        length = n + i
        frt_white = n - 1 - i
        mid_white = length - frt_white - 2
        star[i] = (frt_white * " ") + "*" + (mid_white * " ") + "*"
        
    star[-1] = "*" * (n * 2 - 1)
    print(*star, sep="\n")
    return


n = int(input())
print_star(n)