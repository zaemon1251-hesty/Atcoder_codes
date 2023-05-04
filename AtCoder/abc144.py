def mainc():
    N = int(input())
    # 約数列挙

    def make_divisors(n):
        lower_divisors, upper_divisors = [], []
        i = 1
        while i*i <= n:
            if n % i == 0:
                lower_divisors.append(i)
                if i != n // i:
                    upper_divisors.append(n//i)
            i += 1
        return lower_divisors, upper_divisors[::-1]

    l, d = make_divisors(N)
    ans = N - 1
    for ll in l:
        ans = min(ans, ll - 1 + N//ll - 1)
    print(ans)


def maind():
    import math
    a, b, x = map(int, input().split())

    def angle(x):
        return math.atan(x) * 180 / math.pi
    pre = 2 * (a**2 * b - x) / a**3
    pro = a * b * b / x / 2
    jd = 2 * x / a**3
    if jd > b / a:
        print(angle(pre))
    else:
        print(angle(pro))


def maine():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    F = list(map(int, input().split()))
    A.sort()
    F.sort(reverse=True)

    def check(x, K):
        cnt = 0
        for i in range(N):
            ok = 0
            ng = A[i] + 1
            while ng-ok > 1:
                cen = (ok + ng) // 2
                if cen * F[i] <= x:
                    ok = cen
                else:
                    ng = cen
            cnt += A[i] - ok
        return cnt <= K

    ok = 10**18
    ng = -1
    while ok - ng > 1:
        cen = (ok + ng) // 2
        if check(cen, K):
            ok = cen
        else:
            ng = cen
    print(ok)


if __name__ == "__main__":
    maine()
