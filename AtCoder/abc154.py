from typing import AnyStr


def maina():
    s, t = map(str, input().split())
    a, b = map(int, input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1

    print(a, b)


def mainb():
    print('x'*len(input()))


def mainc():
    n = int(input())
    A = set(list(map(int, input().split())))
    print('YES' if len(A) == n else 'NO')


def maind():
    N, K = map(int, input().split())
    P = list(map(lambda x: (int(x) * (int(x) + 1) // 2) / int(x), input().split()))
    tmp = sum(P[:K])
    ans = tmp
    for i in range(N - K):
        tmp += P[K + i] - P[i]
        ans = max(ans, tmp)

    print(ans)


def maine():
    from functools import lru_cache
    N = int(input())
    K = int(input())

    @lru_cache(maxsize=128, typed=False)
    def digitDP(n, k):
        if n < 10:
            if k == 0:
                return 1
            elif k == 1:
                return n
            return 0
        else:
            ret = digitDP(n // 10, k)
            if k >= 1:
                ret += digitDP(n // 10, k-1) * (n % 10)
                ret += digitDP(n // 10 - 1, k-1) * (9 - n % 10)
            return ret
    print(digitDP(N, K))


if __name__ == '__main__':
    # maina()
    # mainb()
    # mainc()
    # maind()
    maine()
