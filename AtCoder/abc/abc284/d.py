import sys

# import math


def input():
    return sys.stdin.readline().rstrip()


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


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    T = ii()
    buf = []
    for _ in range(T):
        buf.append(ii())

    primes = get_prime(int((max(buf)) ** (1 / 3)) + 20, True)

    for N in buf:
        for p in primes[::-1]:
            if N % p**2 == 0:
                print(p, N // p**2)
                break
            if N % p == 0:
                print(int((N // p) ** (1 / 2)), p)
                break
        else:
            raise RuntimeError


if __name__ == "__main__":
    main()
