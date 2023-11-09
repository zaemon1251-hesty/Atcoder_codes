import sys

sys.setrecursionlimit(10**7)
readline = sys.stdin.readline
read = sys.stdin.read

mod = 998244353


class SegmentTree:
    def __init__(self, init_val, monoid, identity_element):
        n = len(init_val)
        self.monoid = monoid
        self.identity_element = identity_element
        self.num = 1 << (n - 1).bit_length()
        self.tree = [identity_element] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.monoid(self.tree[2 * i], self.tree[2 * i + 1])

    def __getitem__(self, i):
        return self.tree[self.num + i]

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        # while k > 1:
        #   self.tree[k >> 1] = self.monoid(self.tree[k], self.tree[k | 1])
        #   k >>= 1
        while k > 1:
            k >>= 1
            self.tree[k] = self.monoid(self.tree[k << 1], self.tree[k << 1 | 1])

    def get(self, l, r):
        resl = self.identity_element
        resr = self.identity_element
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                resl = self.monoid(resl, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                resr = self.monoid(self.tree[r], resr)
            l >>= 1
            r >>= 1
        return self.monoid(resl, resr)


def main():
    N, Q = map(int, readline().split())
    S = input()
    init = [(0, 0)] * N

    for i in range(N):
        if S[i] == "(":
            init[i] = (1, 1)
        else:
            init[i] = (-1, -1)

    STQ = SegmentTree(init, monoid=(lambda x, y: (min(x[0], x[1] + y[0]), x[1] + y[1])), identity_element=(0, 0))

    for _ in range(Q):
        q, l, r = map(int, readline().split())
        if q == 1:
            a = STQ[l - 1]
            b = STQ[r - 1]
            if a != b:
                STQ.update(l - 1, b)
                STQ.update(r - 1, a)
        else:
            if STQ.get(l - 1, r) == (0, 0):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
