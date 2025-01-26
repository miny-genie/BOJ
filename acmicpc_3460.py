for _ in range(int(input())):
    num = int(input())
    digit = 0
    
    bits = []
    for _ in range(num.bit_length()):
        if num & (1 << digit):
            bits.append(digit)
        digit += 1
    
    print(*bits)

# 25.01.26
# Platinum 1: 2189 > 2189 (+0pts)
# 승급까지 -11 > -11