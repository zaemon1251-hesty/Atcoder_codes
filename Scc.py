class StronglyConnectedComponent:
    def __init__(self, n, G=None):
        self.n = n
        self.G = G
        self.seen = [False] * n
        self.t = [-1] * n
        self.now = 1
        self.belong = [-1] * n

        self.invG = [[] for _ in range(n)]
        for i in range(n):
            for v in G[i]:
                self.invG[v].append(i)
        self.is_done = False

    def decomp(self):
        """強連結成分分解の実行"""
        self.dfs(0)
        self.seen = [False] * self.n
        rank = sorted(enumerate(self.t), key=lambda x: x[1], reverse=True)

        for i, v in rank:
            self.dfs2(i, v)

        self.is_done = True

    def dfs(self, v):
        self.seen[v] = True
        for next_v in self.G[v]:
            if self.seen[next_v] == True:
                continue
            self.dfs(next_v)
        self.t[v] = self.now
        self.now += 1

    def dfs2(self, v, r):
        self.seen[v] = True
        for next_v in self.invG[v]:
            if self.seen[next_v] == True:
                continue
            self.dfs2(next_v, r)
        self.belong[v] = r

    def grouping(self):
        group = {}
        for i, b in enumerate(self.belong):
            group[b] = group.get(b, []) + [i]
        return group
