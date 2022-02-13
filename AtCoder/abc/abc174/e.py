from math import floor


N, K = map(int, input().split())
A = list(map(int, input().split()))


def check(x):
    cut = 0
    for t in A:
        cut += floor(t/x)
        if t % x == 0:
            cut -= 1
    if cut > K:
        return False
    else:
        return True


ok = 10**9 + 1
ng = 0
while ok - ng > 1:
    cen = (ok + ng) // 2
    if check(cen):
        ok = cen
    else:
        ng = cen
print(ok)
