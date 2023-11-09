from functools import reduce
from math import gcd


def get_prime(n, get_sieve=False):
    prime = [False] * 2 + [True] * (n - 2)
    for i in range(2, n):
        if prime[i]:
            for j in range(i * 2, n, i):
                prime[j] = False
    if get_sieve:
        return {i: False for i in range(2, n) if prime[i]}
    else:
        return prime


def main():
    N = int(input())
    (*A,) = map(int, input().split())
    primes = get_prime(10**6, get_sieve=True)

    def prime_factorize(n):
        # 素因数分解
        a = []
        divided = False
        while n % 2 == 0:
            if primes[2]:
                return False
            divided = True
            n //= 2
        if divided:
            primes[2] = True
        f = 3
        while f * f <= n:
            divided = False
            if n % f == 0:
                if primes[f]:
                    return False
                divided = True
                n //= f
            else:
                if divided:
                    primes[f] = True
                f += 2
        if n != 1:
            if primes[n]:
                return False
            primes[n] = True
        return True

    flg = True
    for a in A:
        if not prime_factorize(a):
            flg = False
            break
    if flg:
        print("pairwise coprime")
    else:
        setwise_coprime = reduce(lambda x, y: gcd(x, y), A)
        if setwise_coprime == 1:
            print("setwise coprime")
        else:
            print("not coprime")


if __name__ == "__main__":
    main()
