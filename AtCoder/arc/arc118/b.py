import numpy as np

K, N, M = map(int, input().split())
A = np.array(input().split(), np.int64)


def check(x):
    L = np.maximum(0, (M * A - x + N - 1) // N)
    R = (M * A + x) // N
    return L.sum() <= M <= R.sum()


def construct(x):
    B = np.maximum(0, (M * A - x + N - 1) // N)
    R = (M * A + x) // N
    B_sum = B.sum()
    for i in range(K):
        x = min(M - B_sum, R[i] - B[i])
        B[i] += x
        B_sum += x
    return B


ng, ok = -1, N * M
while ng + 1 < ok:
    x = (ng + ok) // 2
    if check(x):
        ok = x
    else:
        ng = x

B = construct(ok)
print(*B)
