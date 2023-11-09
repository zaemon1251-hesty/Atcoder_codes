def cmb(n, r):
    if n < 2:
        return 0
    r = min(n - r, r)  # nCrでもnCn-rでも一緒のことなので小さい方を取ることで高速化を図る
    a = 1
    b = 1
    for k in range(r):
        a *= n - r + 1 + k
        b *= k + 1
    return a // b


N, M = map(int, input().split())
print(cmb(N, 2) + cmb(M, 2))
