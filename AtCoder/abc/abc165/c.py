import sys
sys.setrecursionlimit(10**6)
ans = 0

N, M, Q = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(Q)]


def dfs(A):
    if len(A) == N+1:
        global ans
        cand = 0
        for a, b, c, d in P:
            if A[b] - A[a] == c:
                cand += d
        ans = max(ans, cand)
        return
    for i in range(A[-1], M + 1):
        if i < 1:
            continue
        A.append(i)
        dfs(A)
        A.pop()


dfs([0])
print(ans)
