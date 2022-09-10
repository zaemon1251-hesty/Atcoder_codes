import sys


sys.setrecursionlimit(10**6)


def main():
    MOD = 10**9 + 7
    N, K = map(int, input().split())
    E = [
        list(map(lambda x: int(x) - 1, input().split()))
        for _ in range(N - 1)
    ]
    G = [
        []
        for _ in range(N)
    ]
    for u, v in E:
        G[u].append(v)
        G[v].append(u)

    def dfs(v, p, rest):
        res = rest

        # 自分の色
        used = 1

        # 親の色
        if (p > -1):
            used += 1

        for to in G[v]:
            if to == p:
                continue
            res *= dfs(to, v, K - used)
            res %= MOD

            # 自分(v)を通して繋がっている子の色
            used += 1

        return res

    print(dfs(0, -1, K))


if __name__ == '__main__':
    main()
