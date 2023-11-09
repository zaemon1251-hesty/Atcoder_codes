def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# return [g, x, y]
# g = gcd(a, b)
# x, y satisfies a x + b y = g
def extgcd(a, b):
    if b == 0:
        return [a, 1, 0]
    g, x, y = extgcd(b, a % b)
    return [g, y, x - a // b * y]


# eq0: x = a0 (mod m0)
# eq1: x = a1 (mod m1)
# returns [xt, mod] such that x = xt + k mod for integer k.
def crt(eq0, eq1):
    a0, m0 = eq0
    a1, m1 = eq1

    g = gcd(m0, m1)

    if a0 % g != a1 % g:
        return [-1, 0]

    if g > 1:
        m0 //= g
        m1 //= g

        while True:
            gt = gcd(m0, g)
            if gt == 1:
                break
            m0 *= gt
            g //= gt

        m1 *= g

        a0 %= m0
        a1 %= m1

    g, p, q = extgcd(m0, m1)

    x = a0 * q * m1 + a1 * p * m0
    mod = m0 * m1
    x = x % mod

    return [x, mod]


def main():
    T = int(input())
    ans = []
    for _ in range(T):
        n, s, k = map(int, input().split())
        x, mod = crt((0, k), (-s, n))
        if x == -1:
            ans.append(-1)
        else:
            ans.append(x // k)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
