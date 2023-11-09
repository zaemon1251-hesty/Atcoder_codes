n, k = map(int, input().split())
A = []
ok = 0
ng = -1
for _ in range(n):
    a = list(map(int, input().split()))
    ok = max(ok, max(a))
    A.append(a)
# import numpy as np
# print(np.array(A))
while ok - ng > 1:
    # print('--------------------')
    cen = (ok + ng) // 2
    # print(cen)
    f = two_cumsum(A, cen)
    # print(check(f, k, n))
    if check(f, k, n):
        ok = cen
    else:
        ng = cen
print(ok)
