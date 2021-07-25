# -*- coding:utf-8 -*-

def get_prime(n, get_sieve=False):
    prime = [False] * 2 + [True] * (n-2)
    for i in range(2, n):
        if prime[i]:
            for j in range(i*2, n, i):
                prime[j] = False
    if get_sieve:
        return [i for i in range(2, n) if prime[i]]
    else:
        return prime


def mainc():
    from bisect import bisect
    x = int(input())
    prime = get_prime(2*pow(10, 5))
    while not prime[x]:
        x += 1
    print(x)


def maind():
    N, K = map(int, input().split())
    r, s, p = map(int, input().split())
    ch = {"r": "p", "s": "r", "p": "s"}
    point = {"r": r, "s": s, "p": p}
    t = list(input())
    binds = [[] for _ in range(K)]

    for i in range(N):
        binds[i % K].append(ch[t[i]])

    ans = 0
    for bind in binds:
        pre = -1
        for pt in bind:
            if pt != pre:
                ans += point[pt]
                pre = pt
            else:
                pre = -1

    print(ans)


if __name__ == '__main__':
    # mainc()
    maind()
