import sys
sys.setrecursionlimit(10**9)

N = int(input())
A = [list(map(int, input().split())) for _ in range(2*N-1)]

used = [False] * (2*N)
X = []
ans = 0


def dfs():
    global ans
    if len(X) == N:
        t = 0
        for a, b in X:
            t ^= A[a][b-a-1]
        ans = max(ans, t)

        return

    for l in range(2*N):
        if not used[l]:
            break

    used[l] = True
    for r in range(l+1, 2*N):
        if used[r]:
            continue

        used[r] = True
        X.append((l, r))
        dfs()
        X.pop()
        used[r] = False

    used[l] = False


dfs()
print(ans)
