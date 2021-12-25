
def maina():
    def cmb(n, r):
        if n < 2:
            return 0
        r = min(n-r, r)  # nCrでもnCn-rでも一緒のことなので小さい方を取ることで高速化を図る
        a = 1
        b = 1
        for k in range(r):
            a *= (n-r+1+k)
            b *= (k+1)
        return a // b
    N, M = map(int, input().split())
    print(cmb(N, 2) + cmb(M, 2))


def mainb():
    S = list(input())
    N = len(S)
    a = (N - 1) // 2
    b = (N + 3) // 2 - 1

    def iskaibun(arr):
        return all(i == j for i, j in zip(arr, arr[::-1]))
    print("Yes" if all([iskaibun(S), iskaibun(
        S[:a]), iskaibun(S[b:])]) else "No")


def mainc():
    L = int(input())
    print(pow(L, 3)/27)


def maind():
    from collections import Counter
    N = int(input())
    A = list(map(int, input().split()))
    cntr = Counter(A)
    ans = sum(i * (i - 1) // 2 for i in cntr.values())
    for i in range(N):
        n_ans = ans - cntr[A[i]] * (cntr[A[i]] - 1) // 2 + \
            max(0, (cntr[A[i]] - 2) * (cntr[A[i]] - 1) // 2)
        print(n_ans)


def maine():
    from collections import defaultdict

    H, W, K = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    ans = float('inf')
    for i in range(1 << H):
        bag = defaultdict(int)
        sep = []
        for j in range(H):
            if (i >> j) & 1:
                sep.append(j)
        for y in range(W):
            for x in range(H):
                if G[x][y] == "1":
                    print()


maine()
