from string import ascii_uppercase, ascii_lowercase
index = "!" + ascii_lowercase + ascii_uppercase


def isPrime(num: int) -> bool:
    if num == 1: return True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


word   = input()
score  = sum(index.index(w) for w in word)
answer = isPrime(score)
print("It is a prime word.") if answer else print("It is not a prime word.")