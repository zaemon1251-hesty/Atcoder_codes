from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        # parents[i]にはi番目のノードの親の番号を格納し、
        # 自分が根だった場合は -(自分が属する連結集合のサイズ) とする
        self.n = n
        self.parents = [-1] * n

    #

    def find(self, x):
        # 要素xの根の番号を返す
        if self.parents[x] < 0:
            # 自分が根のとき
            return x
        else:
            # 「要素xの親の根」を「要素xの根」として設定することで次の呼び出しの高速化
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    #

    def union(self, x, y):
        # xとyを結合する
        x = self.find(x)
        y = self.find(y)
        if x == y:
            # すでに結合されている
            return
        # 大きい方(x)に小さい方(y)をぶら下げる
        if self.parents[x] > self.parents[y]:  # 負の数の比較
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    #

    def size(self, x):
        # 要素xの所属するグループの要素数を調べる
        return -self.parents[self.find(x)]

    #

    def same(self, x, y):
        # xとyが同じグループにあるか
        return self.find(x) == self.find(y)

    #

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    #

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    #

    def group_count(self):
        return len(self.roots())

    #

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    #

    def __str__(self):
        return "".join(f"{r}:{m} " for r, m in self.all_group_members().items())


#


def main():
    N, M, E = list(map(int, input().split()))
    #
    U = [0] * E
    V = [0] * E
    for i in range(E):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        if u > N:
            u = N
        if v > N:
            v = N
        U[i] = u
        V[i] = v
    #
    Q = int(input())
    X = [0] * Q
    es = set(range(E))
    for i in range(Q):
        x = int(input())
        x -= 1
        X[i] = x
        es.remove(x)
    #
    uf = UnionFind(N + 1)
    for x in es:
        u = U[x]
        v = V[x]
        uf.union(u, v)
    #
    ans = [0] * Q
    for i in range(Q - 1, -1, -1):
        ans[i] = uf.size(N) - 1
        x = X[i]
        u = U[x]
        v = V[x]
        uf.union(u, v)
    #
    for a in ans:
        print(a)


#
if __name__ == "__main__":
    main()
#
