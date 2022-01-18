import sys
from collections import deque
sys.setrecursionlimit(10**6)


def mainc():
    from math import log10, floor
    a, b, x = map(int, input().split())

    def check(n):
        if a*n+b*(floor(log10(n))+1) <= x:
            return True
        else:
            return False
    ok = 0
    ng = 10**9+1
    while ng - ok > 1:
        cen = (ok + ng) // 2
        if check(cen):
            ok = cen
        else:
            ng = cen
    print(ok)


def maind():
    n = int(input())
    G = [[] for _ in range(n)]
    E = []

    for i in range(n-1):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)
        E.append([a, b])

    m_c = max(len(G[i]) for i in range(n))
    R = list(range(1, m_c + 1))

    todo = deque([0])
    C = [-1]*n
    C[0] = -2
    prev = -1

    while todo:
        current = todo.popleft()
        stock = m_c
        for next_v in G[current]:
            if C[next_v] != -1:
                continue
            if stock == C[current]:
                stock -= 1
            C[next_v] = stock
            stock -= 1
            todo.append(next_v)

    print(m_c)
    for e in E:
        a, b = e[0], e[1]
        print(C[b])
