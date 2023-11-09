class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


def main():
    ans = []
    N, Q = map(int, input().split())
    C = list(map(lambda x: int(x) - 1, input().split()))
    S = [{C[i]: 1} for i in range(N)]
    uf = UnionFind(N)
    query = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]
    for t, x, y in query:
        if t == 0:
            x = uf.find(x)
            y = uf.find(y)
            if x == y:
                continue
            if uf.parents[x] > uf.parents[y]:
                x, y = y, x
            for k, v in S[y].items():
                S[x][k] = v + S[x].get(k, 0)
            uf.union(x, y)
        else:
            ans.append(S[uf.find(x)].get(y, 0))
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
