def maina():
    from math import ceil
    t, N = map(int, input().split())

    print(N - 1 + ceil(N*100/t))

def mainb():
    from math import ceil,floor
    K, N, M = map(int, input().split())
    A = list(map(int, input().split()))
    diva = [val * M for val in A]
    def check(x):
        l = 0
        r = 0
        for i in range(K):
            l += max(0, ceil((diva[i] - x)/N))
            r += floor((diva[i] + x)/N)
        if l <= M <= r:
            return True
        else:
            return False

    ok = N * M
    ng = 0
    while ok - ng > 1:
        cen = (ok + ng) // 2
        if check(cen):
            ok = cen
        else:
            ng = cen

    def construct(x):
        import numpy as np
        B = np.maximum(0, (M * A - x + N - 1) // N)
        R = (M * A + x) // N
        B_sum = B.sum()
        for i in range(K):
            x = min(M - B_sum, R[i] - B[i])
            B[i] += x
            B_sum += x
        return B
    B = construct(ok)
    print(*B)



if __name__ == "__main__":
    mainb()