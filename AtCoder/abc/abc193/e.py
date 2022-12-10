inf = 1 << 60


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def extgcd(a, b):
    if b == 0:
        return [a, 1, 0]
    g, x, y = extgcd(b, a % b)
    return [g, y, x - a // b * y]


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
        X, Y, P, Q = map(int, input().split())
        mod1 = 2 * X + 2 * Y
        mod2 = P + Q
        res = inf
        for stp in range(X, X + Y):
            for awk in range(P, P + Q):
                x, mod = crt([stp, mod1], [awk, mod2])
                if mod == 0:
                    continue
                if x < 0:
                    x += mod
                res = min(res, x)
        ans.append(str(res) if res < inf else "infinity")
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
