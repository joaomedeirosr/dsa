def recursive_number(n):
    if n < 0:
        return False

    elif n > 10:
        return False
    
    else:
        print(n)
        return recursive_number(n + 1)

print(recursive_number(-3))
recursive_number(1)
print(recursive_number(11))