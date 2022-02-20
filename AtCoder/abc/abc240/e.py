from sys import setrecursionlimit
setrecursionlimit(10**6)

# 行きがけ、帰りがけに使う変数
now = 1


def main():
    N = int(input())
    G = [[] for i in range(N)]
    G[0].append(-1)
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)

    before = [0] * N
    after = [0] * N

    def dfs(v, p):
        global now
        if v != 0 and len(G[v]) == 1:
            before[v] = now
            after[v] = now
            return
        before[v] = now
        for next_v in G[v]:
            if next_v == p:
                continue
            dfs(next_v, v)
            now += 1
        now -= 1
        after[v] = now

    # global変数の初期化
    global now
    now = 1
    dfs(0, -1)

    lr = [(l, r) for l, r in zip(before, after)]
    for i in range(N):
        print(*lr[i], sep=' ')


if __name__ == '__main__':
    main()
