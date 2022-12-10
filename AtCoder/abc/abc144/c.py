N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)
def check(x, K):
    cnt = 0
    for i in range(N):
        ok = 0
        ng = A[i] + 1
        while ng-ok > 1:
            cen = (ok + ng) // 2
            if cen * F[i] <= x:
                ok = cen
            else:
                ng = cen
        cnt += A[i] - ok
    return cnt <= K
ok = 10**18
ng = -1
while ok - ng > 1:
    cen = (ok + ng) // 2
    if check(cen, K):
        ok = cen
    else:
        ng = cen
print(ok)
_name__ == "__main__":
maine()
