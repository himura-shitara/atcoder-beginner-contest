import math

A, B, C, D = map(int, input().split())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def takahashi_wins(i: int):
    for j in range(C, D + 1):
        if is_prime(i + j):
            return False
    return True


for i in range(A, B + 1):
    if takahashi_wins(i):
        print("Takahashi")
        exit()
print("Aoki")
