

def maina():
    a, b = map(int, input().split())
    print((a - b)/3+b)


def mainb():
    S = set()
    for i in range(4):
        S.add(input())
    print("Yes" if len(S) == 4 else "No")


def mainc():
    from collections import defaultdict
    mod = 10**9 + 7
    S = list(input())
    ord = list("chokudai")
    dp = [0]*8
    for i in range(len(S)):
        dp[0] += bool(S[i] == ord[0])
        dp[0] %= mod
        for j in range(1, 8):
            if S[i] == ord[j]:
                dp[j] += dp[j-1]
                dp[j] %= mod
    print(dp[-1] % mod)


def maind():
    from collections import deque
    mod = 10**9 + 7
    inf = 1 << 60
    N, M = map(int, input().split())
    G = [[]for _ in range(N)]

    for _ in range(M):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        G[a].append(b)
        G[b].append(a)

    cnt = [0]*N
    cnt[0] = 1

    dist = [inf]*N
    todo = deque([0])
    dist[0] = 0

    while todo:
        v = todo.popleft()
        for next_v in G[v]:
            # bfsだから深さd以下の頂点はもう更新されない
            if dist[next_v] == inf:
                dist[next_v] = dist[v]+1
                cnt[next_v] = cnt[v]
                todo.append(next_v)
            # 同じ深さなら加算
            elif dist[next_v] == dist[v]+1:
                cnt[next_v] += cnt[v]
                cnt[next_v] %= mod

    print(cnt[-1] % mod)


def maine():
    from math import gcd
    N, M = map(int, input().split())
    D = []
    for i in range(M):
        a, c = map(int, input().split())
        D.append((a, c))
    D.sort(key=lambda x: x[1])

    ans = 0
    X = N
    #sdgs = N
    for i in range(M):
        a, c = D[i][0], D[i][1]
        tmp = gcd(X, a)
        ans += c * (X - tmp)
        X = tmp

    print(ans if X == 1 else -1)


if __name__ == "__main__":
    mori = 20
    # maina()
    # mainb()
    # mainc()
    maind()
    # maine()
