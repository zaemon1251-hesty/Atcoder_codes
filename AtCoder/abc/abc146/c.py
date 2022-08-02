from math import log10, floor
a, b, x = map(int, input().split())


def check(n):
    if a * n + b * (floor(log10(n)) + 1) <= x:
        return True
    else:
        return False


ok = 0
ng = 10**9 + 1
while ng - ok > 1:
    cen = (ok + ng) // 2
    if check(cen):
        ok = cen
    else:
        ng = cen
print(ok)
