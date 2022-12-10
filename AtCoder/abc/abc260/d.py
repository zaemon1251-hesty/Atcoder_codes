from collections import defaultdict
import sys
input = sys.stdin.buffer.readline


class VEBTree:
    def __init__(self, lg_u):
        self.lg_u = lg_u
        self.min = self.max = None
        if lg_u == 1:
            return

        self.summary = VEBTree(lg_u >> 1)
        # self.cluster = [VEBTree(lg_u // 2) for _ in range(1 << (lg_u // 2))]
        self.cluster = {}

    def split(self, x):
        shift = self.lg_u >> 1
        hi = x >> shift
        lo = x & ((1 << shift) - 1)
        return (hi, lo)

    def merge(self, hi, lo):
        shift = self.lg_u >> 1
        return (hi << shift) + lo

    def add(self, x):
        if self.min is None:
            self.min = self.max = x
            return

        if self.lg_u == 1:
            if self.min is None:
                self.min = self.max = x
            elif self.min > x:
                self.min = x
            elif self.max < x:
                self.max = x
            return

        if x < self.min:
            self.min, x = x, self.min

        if x > self.max:
            self.max = x

        hi, lo = self.split(x)
        if hi not in self.cluster:
            self.cluster[hi] = VEBTree(self.lg_u >> 1)

        if self.cluster[hi].min is None:
            self.summary.add(hi)

        self.cluster[hi].add(lo)

    def discard(self, x):
        if self.min is None:
            return

        if self.lg_u == 1:
            if self.min == self.max:
                if x == self.min:
                    self.min = self.max = None
            else:
                if x == self.min:
                    self.min = self.max
                elif x == self.max:
                    self.max = self.min
            return

        if x == self.min:
            if self.summary.min is None:
                self.min = self.max = None
                return

            hi = self.summary.min
            x = self.min = self.merge(hi, self.cluster[hi].min)

        hi, lo = self.split(x)
        if hi not in self.cluster:
            return

        self.cluster[hi].discard(lo)
        if self.cluster[hi].min is None:
            self.summary.discard(hi)

        if x == self.max:
            if self.summary.max is None:
                self.max = self.min
            else:
                hi = self.summary.max
                self.max = self.merge(hi, self.cluster[hi].max)

    def remove(self, x):
        if self.has(x):
            self.discard(x)
        else:
            raise KeyError(x)

    def successor(self, x):
        if self.min is None:
            return None
        if x < self.min:
            return self.min
        if x >= self.max:
            return None

        if self.lg_u == 1:
            return 1 if x == 0 and self.max == 1 else None

        hi, lo = self.split(x)
        if (
                hi in self.cluster
                and self.cluster[hi].max is not None
                and lo < self.cluster[hi].max
        ):
            i = hi
            j = self.cluster[hi].successor(lo)
        else:
            i = self.summary.successor(hi)
            if i is None:
                return None
            j = self.cluster[i].min

        return self.merge(i, j)

    def predecessor(self, x):
        if self.min is None:
            return None
        if x > self.max:
            return self.max
        if x <= self.min:
            return None

        if self.lg_u == 1:
            return 0 if x == 1 and self.min == 0 else None

        hi, lo = self.split(x)
        if (
                hi in self.cluster
                and self.cluster[hi].min is not None
                and lo > self.cluster[hi].min
        ):
            i = hi
            j = self.cluster[hi].predecessor(lo)
            if j is None:
                j = self.cluster[hi].min
        else:
            i = self.summary.predecessor(hi)
            if i is None:
                return self.min if x > self.min else None
            j = self.cluster[i].max

        return self.merge(i, j)

    def has(self, x):
        if self.min is None:
            return False
        if x == self.min or x == self.max:
            return True

        return x != 0 and self.successor(x - 1) == x

    def min_gt(self, x):
        return self.successor(x)

    def min_ge(self, x):
        if x == 0:
            return 0 if self.min == 0 else self.successor(0)

        return self.successor(x - 1)

    def max_lt(self, x):
        return self.predecessor(x)

    def max_le(self, x):
        if (x + 1) >> self.lg_u:
            return x if self.max == x else self.predecessor(x)

        return self.predecessor(x + 1)


def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    if K == 1:
        for i in range(N):
            ans[P[i] - 1] = i + 1
        print(*ans, sep="\n")
        exit()

    vs = VEBTree(32)
    ans = [-1] * N
    deck = defaultdict(list)
    fin = defaultdict(lambda: -1)
    for i, p in enumerate(P):
        v = vs.min_gt(p)
        if not v:
            deck[p].append(p)
            vs.add(p)
        else:
            deck[v], deck[p] = deck[p], deck[v]
            deck.pop(v)
            deck[p].append(p)
            vs.remove(v)
            vs.add(p)
            if len(deck[p]) == K:
                fin[p] = i + 1
                vs.remove(p)

    for p in deck.keys():
        for card in deck[p]:
            ans[card - 1] = fin[p]
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
