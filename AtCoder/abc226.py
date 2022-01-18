import math


def maina():
    import math
    x = float(input())
    print(math.floor(x + 0.5))


def mainb():
    from collections import defaultdict
    ans = 0

    n = int(input())
    A = []
    S = defaultdict(set)
    for i in range(n):
        A.append(list(map(int, input().split())))
    for i in range(n):
        l = A[i][0]
        d = tuple(A[i][1:])
        S[l].add(d)
    for k, v in S.items():
        ans += len(v)
    print(ans)


def mainc():
    from heapq import heappush, heappop
    from collections import deque
    inf = 1 << 60
    N = int(input())
    G = [[] for _ in range(N)]
    E = [0] * N
    ans = 0
    got = [False] * N
    for i in range(N):
        A = list(map(int, input().split()))
        l = A[0]
        E[i] = l
        if A[1] != 0:
            for j in range(2, len(A)):
                A[j] -= 1
                G[i].append(A[j])
    r = N - 1
    todo = [r]
    short = [0] * N
    short[r] = E[r]
    while todo:
        dd = heappop(todo)
        flg = True
        ans += E[dd]
        for to in G[dd]:
            if not got[to]:
                heappush(todo, to)
                got[to] = True
    print(ans)


def maind():
    from math import gcd
    n = int(input())
    a = []
    ans = set()
    for _ in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n-1):
        for j in range(i + 1, n):
            x, y = a[i][0] - a[j][0], a[i][1] - a[j][1]
            x, y = x//gcd(x, y), y//gcd(x, y)
            ans.add((x, y))
            ans.add((-x, -y))
    print(len(ans))


def maine():


mainc()
