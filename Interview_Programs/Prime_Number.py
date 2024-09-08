"""def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 and n % 3 == 0:
        return False
    i = 5
    while """
"""n = 24
prime_factors = []
for i in range(1,n):
    if n % i == 0:
        prime_factors.append(i)
print(prime_factors)"""


def is_armstrong(n):
    sum = 0
    for i in range