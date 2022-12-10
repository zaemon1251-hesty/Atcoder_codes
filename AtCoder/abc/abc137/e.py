# Method 1 (Bellman-Ford)
# 全辺で始点コスト＋辺のコスト＜終点コストを調べて更新していく
# 頂点数繰り返して収束しなければ負の閉回路あり
# 目的地コストが収束したかどうかをベルマンフォード法を２回回して、
# 終点コストの結果を比較、変化してたら -1

from typing import List, Tuple


Costs = List[int]
Edges = List[Tuple[int]]
LowerLimit = bool
Res = Tuple[Costs, LowerLimit]


def bellman_ford(N: int, G: Edges, cost: Costs) -> Res:  # 最大コストを返す
    INF = 10**12
    cnt = 0  # 負の閉経路探索のため
    while cnt < N:
        flag = True
        for ai, bi, ci in G:
            if cost[ai] != INF and cost[bi] > cost[ai] + ci:
                cost[bi] = cost[ai] + ci
                flag = False
        if flag:
            break
        cnt += 1
    else:
        return cost, False
    return cost, True


def bellman_ford2(N: int, G: Edges, cost: Costs) -> Res:  # 破壊的に書き換えを進める
    INF = 10**12
    cnt = 0  # 負の閉経路探索のため
    while cnt < N:
        for ai, bi, ci in G:
            if cost[ai] != INF and cost[bi] > cost[ai] + ci:
                cost[bi] = -INF
        cnt += 1
    return cost, False


INF = 10**12
N, M, P = map(int, input().split())
G: Edges = []
cost: Costs = [INF] * N

for _ in range(M):
    ai, bi, ci = map(int, input().split())
    G.append((ai - 1, bi - 1, P - ci))
cost[0] = 0
cost, stable = bellman_ford(N, G, cost)
prev = cost[N - 1]
cost, stable2 = bellman_ford2(N, G, cost)

if stable or prev == cost[N - 1]:
    print(max(0, -prev))
else:
    print(-1)
