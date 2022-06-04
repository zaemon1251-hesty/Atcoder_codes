# 素数列挙
def get_prime(n, get_sieve=False):
    prime = [False] * 2 + [True] * (n - 2)
    for i in range(2, n):
        if prime[i]:
            for j in range(i * 2, n, i):
                prime[j] = False
    if get_sieve:
        return [i for i in range(2, n) if prime[i]]
    else:
        return prime


# 約数列挙
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


# 素因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
