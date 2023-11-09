# 素数列挙
from bisect import bisect_left, bisect


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
    N = int(input())
    P = get_prime(min(N + 1, 10**6))
    s_p = list()
    ans = 0
    for q, f in enumerate(P):
        if not f:
            continue
        a = N // q**3
        if s_p:
            ans += bisect(s_p, a)
        s_p.append(q)
    print(ans)


if __name__ == "__main__":
    main()
