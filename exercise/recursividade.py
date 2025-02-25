# Fibonacci algorithm
# Base case: F(0) -> Return 0
# Base case: F(1) -> Return 1
# Se n > 1:  F(n-1) + F(n-2)

def F(n):
    if n == 0: return 0

    elif n == 1: return 1

    else:
        return F(n-1) + F(n-2)