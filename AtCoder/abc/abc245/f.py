from typing import Union

# import pypyjit
import sys

input = sys.stdin.readline
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(2000000)


def main():
    from collections import deque

    class StronglyConnectedComponent:
        def __init__(self, n):
            self.n = n
            self.g = [[] for _ in range(n)]
            self.gr = [[] for _ in range(n)]  # graph rev

        def addEdge(self, u, v) -> None:
            self.g[u].append(v)
            self.gr[v].append(u)

        def dfs(self, v) -> None:
            # 正方向のDFS
            self.visited[v] = True
            for nxt in self.g[v]:
                if self.visited[nxt]:
                    continue
                self.dfs(nxt)
            self.vs.append(v)

        def solve(self) -> int:
            self.vs = []  # かえりがけ
            self.visited = [False] * self.n
            k = 0
            self.cmp: list[Union[None, int]] = [None] * self.n
            # DFS1

            for i in range(self.n):
                if self.visited[i] is True:
                    continue
                self.dfs(i)

            q = deque([])
            self.visited = [False] * self.n
            for i in self.vs[::-1]:
                if self.visited[i] is True:
                    continue
                q.append(i)
                while len(q) > 0:
                    cur = q.popleft()
                    self.visited[cur] = True
                    self.cmp[cur] = k
                    for nxt in self.gr[cur]:
                        if self.visited[nxt]:
                            continue
                        q.append(nxt)
                k += 1

            return k

    from collections import deque

    class topologicalSort:
        def __init__(self, n):
            self.n = n
            self.g = [[] for _ in range(n)]
            self.edgeNum = [0] * n

        def makeEdge(self, u, v):
            self.g[u].append(v)
            self.edgeNum[v] += 1  # 入次++

        def solve(self):
            q = deque([])
            ans = []
            for i in range(self.n):
                if self.edgeNum[i] != 0:
                    continue
                q.appendleft(i)
                ans.append(i)
            while len(q) > 0:
                cur = q.popleft()
                for nxt in self.g[cur]:
                    self.edgeNum[nxt] -= 1
                    if self.edgeNum[nxt] == 0:
                        ans.append(nxt)
                        q.append(nxt)
            return ans

    n, m = map(int, input().split())
    scc = StronglyConnectedComponent(n)
    edges = []

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))

    for u, v in edges:
        scc.addEdge(u, v)
    scc.solve()  # 強連結成分分解する
    cmp = scc.cmp  # cmp[i] = iの所属する強連結成分の番号
    sccnodes: int = max(cmp) + 1  # 強連結成分の数
    cmpSize = [0] * (sccnodes)  # 各強連結成分のサイズ
    for x in cmp:
        cmpSize[x] += 1  # を計算
    g: list[set] = [set() for _ in range(sccnodes)]  # 強連結成分で表したグラフGscc
    for u, v in edges:
        ucmp = cmp[u]
        vcmp = cmp[v]
        if ucmp == vcmp:
            continue  # 同じ連結成分
        g[ucmp].add(vcmp)  # 重複するのでここはsetで記録

    # トポロジカルソートする
    ts = topologicalSort(sccnodes)
    for u in range(sccnodes):
        for v in g[u]:
            ts.makeEdge(u, v)
    tsres = ts.solve()  # これが0...sccnodeの順にトポロジカルソートされている

    canrearch = [0] * sccnodes  # 求めるべきcanrearch
    for node in tsres[::-1]:  # トポロジカルソートを逆からたどる
        canrearch[node] = cmpSize[node]  # まず、自分の連結成分のサイズ
        for childNode in g[node]:  # 各子相当のmaxを取る
            canrearch[node] = max(canrearch[node], canrearch[childNode])

    # canrearch == 1の数。(+=1にしているのは定義より、その連結成分のサイズが1なのは自明のため)
    a = 0
    for i in range(sccnodes):
        if canrearch[i] == 1:
            a += 1
    print(n - a)  # 全頂点からcanrearch=1(というのが条件を満たさない)の点を抜いた数


main()
