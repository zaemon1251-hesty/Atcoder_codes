def maina():
    N, L, R = map(int, input().split())
    t = 1
    ans = 0
    while t <= N:
        if not((t << 1)-1 < L or R < t):
            if (N & t) != 0:
                ans += min(R, (t << 1) - 1) - max(L, t) + 1
        t <<= 1
    print(ans)


def mainb():
    from math import ceil
    N = int(input())
    inf = float('inf')
    r = inf
    l = -inf
    ans = []
    for i in range(N):
        L, R = map(int, input().split())
        r = min(r, R)
        l = max(l, L)
        if l <= r:
            ans.append(0)
        else:
            ans.append(ceil((l - r) / 2))
    print(*ans, sep='\n')


def mainc():
    from bisect import bisect

    N = int(input())
    A = [float('inf')]*N
    A[-1] = 0
    for i in range(N):
        A[i] = A[i-1]+i+1

    B = []
    while N > 0:
        idx = bisect(A, N)
        N -= A[idx-1]
        B.append(idx)
    M = len(B)-1
    if M == 0:
        exit(print('7'*B[0]))

    C = [1, 2, 3, 4, 5, 6, 8, 9]

    def dfs(idx=1, pre=[]):
        if len(pre) == 2*M+1:
            exit(print(''.join(pre)))

        for c in C:
            fit = True
            for i in range(len(pre)):
                a = ''.join(pre[i:])+str(c)
                if int(a) % 7 == 0:
                    fit = False
                    break

            if fit:
                dfs(idx+1, pre+[str(c), '7'*B[idx]])

    dfs(1, ['7'*B[0]])


mainc()
