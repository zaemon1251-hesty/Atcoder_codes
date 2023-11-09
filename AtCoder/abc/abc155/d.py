from bisect import bisect, bisect_left


N, K = map(int, input().split())
A = list(map(int, input().split()))
p, m, z = [], [], []
for a in A:
    if a > 0:
        p.append(a)
    elif a < 0:
        m.append(-a)
    else:
        z.append(0)

p.sort()
m.sort()
P, M, Z = len(p), len(m), len(z)


def getMinus(x):
    assert x < 0
    # 単調性を利用した尺取り法
    res = 0
    j = 0
    for mi in m[::-1]:
        while j < P and x < -mi * p[j]:
            j += 1
        res += P - j
    return res


def getZeros():
    return Z * (P + M) + Z * (Z - 1) // 2


def getPlus(x):
    assert x > 0
    res = 0
    # 単調性を利用した尺取り法
    j = P - 1
    for i in range(P):
        while i < j and x < p[i] * p[j]:
            j -= 1
        res += max(0, j - i)

    # 単調性を利用した尺取り法
    j = M - 1
    for i in range(M):
        while i < j and x < m[i] * m[j]:
            j -= 1
        res += max(0, j - i)

    return res


def getCount(x):
    res = getMinus(min(-1, x))
    if x >= 0:
        res += getZeros()
    if x > 0:
        res += getPlus(x)
    return res


ok = 10**18
ng = -(10**18)
while ok - ng > 1:
    cen = (ok + ng) // 2
    if getCount(cen) >= K:
        ok = cen
    else:
        ng = cen
print(ok)
