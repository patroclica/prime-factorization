"""
Factors in an integer


def factorize(n1):
    if n1==0: return []
    if n1==1: return []
    n=n1
    b=[]
    while n % 2 ==0 : b.append(2);n/=2
    while n % 3 ==0 : b.append(3);n/=3
    i=5
    inc=2
    while i*i<=n:
     while n % i ==0 : b.append(i); n/=i
     i+=inc
     inc=6-inc
    if n !=1:b.append(n)
    return b

def factors(n):
    if n == 0: return []
    if n == 1: return []
    sqrt = int(n ** .5)
    half_factors = [i for i in range(1, sqrt + 1) if n % i == 0]
    return half_factors + [n // i for i in half_factors[n%sqrt == 0::-1]]
"""
