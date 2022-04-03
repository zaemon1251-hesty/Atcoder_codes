def f(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


def main():
    N = int(input())

    def b_s(x):
        ok = 10**6 + 1010
        ng = -1
        while ok - ng > 1:
            cen = (ok + ng) // 2
            if f(cen, x) >= N:
                ok = cen
            else:
                ng = cen
        return ok

    # a の推定
    ans = 10**18 + 1
    for a in range(10**6 + 1010):
        # b の推定
        b = b_s(a)
        ans = min(ans, f(a, b))
    print(ans)


if __name__ == '__main__':
    main()
