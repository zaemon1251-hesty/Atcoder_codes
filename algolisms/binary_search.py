# 競プロ典型 1
# 最小値の最大化 : O(NlogN)
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split())) + [L]


def check(x):
    cut = 0
    src = 0
    for i in range(N + 1):
        dest = A[i] - src
        if dest >= x:
            cut += 1
            src = A[i]
    if cut >= K + 1:
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
