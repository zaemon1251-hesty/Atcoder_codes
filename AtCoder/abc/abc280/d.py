import sys
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


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


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    K = ii()
    ps = prime_factorize(K)
    primes = Counter(ps)
    ans = -1 << 60
    for p, v in primes.items():
        tmp = 0
        while v > 0:
            tmp += p
            tmp2 = tmp
            while tmp2 % p == 0:
                tmp2 //= p
                v -= 1
        ans = max(ans, tmp)
    print(ans)


if __name__ == '__main__':
    main()
