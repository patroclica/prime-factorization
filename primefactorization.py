""" def prime-factorization(n):
    for i < 2 to sqrt(n)
    if n%i == 0
    ct < 0
    while(n%i == 0)
    n = n/i
    ct++
    Print(i, ct)
    if(n! = 1)
    Print(n, 1)
    """

def generate_prime_factors(argnumber):
    """ Returns prime factors that compose argnumber """
    if type(argnumber) != int:
        raise ValueError
    else:
        if argnumber == 0:
            return []
    if argnumber == 1:
        return []
    n = argnumber
    b = []
    while n % 2 == 0:
        b.append(2)
        n /= 2
    while n % 3 == 0:
        b.append(3)
        n /= 3
    i = 5
    inc = 2
    while i*i <= n:
        while n % i == 0:
            b.append(i)
            n /= i
    i += inc
    inc = 6-inc
    if n != 1:
        b.append(n)
    return b
