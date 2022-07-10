from itertools import combinations


class UnionFind():
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
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

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
        return '\n'.join('{}: {}'.format(r, self.members(r))
                         for r in self.roots())


def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())

    circles = [list(map(int, input().split())) for _ in range(N)]

    uf = UnionFind(N)

    def onTheCircle(x, y, a, b, r):
        return (x - a) ** 2 + (y - b)**2 == r**2

    def distanceBetween(i, j):
        return (circles[i][0] - circles[j][0])**2 + \
            (circles[i][1] - circles[j][1])**2

    def hasCommonPoint(i, j):
        return (circles[i][2] - circles[j][2])**2 <= \
            distanceBetween(i, j) <= (circles[i][2] + circles[j][2])**2

    for i, j in combinations(range(N), 2):
        if hasCommonPoint(i, j):
            uf.union(i, j)

    for st_idx, (xx, yy, rr) in enumerate(circles):
        if onTheCircle(sx, sy, xx, yy, rr):
            break
    else:
        raise

    for en_idx, (xx, yy, rr) in enumerate(circles):
        if onTheCircle(tx, ty, xx, yy, rr):
            break
    else:
        raise

    print("Yes" if uf.same(st_idx, en_idx) else "No")


if __name__ == '__main__':
    main()
