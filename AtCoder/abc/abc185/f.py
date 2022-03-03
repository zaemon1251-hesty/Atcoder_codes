class BIT:
    """
    Binary Indexed Tree
    """

    def __init__(self, n, func, ele) -> None:
        self.n = n
        self.ele = ele
        self.func = func
        self.bit = [ele]*(n+1)

    def add(self, i, x) -> None:
        i += 1
        while i <= self.n:
            self.bit[i] = self.func(self.bit[i], x)
            i += i & -i

    def sum(self, i):
        # [0, i] での演算
        i += 1
        res = self.ele
        while i > 0:
            res = self.func(res, self.bit[i])
            i -= i & -i
        return res


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    bt = BIT(N, lambda x, y: x ^ y, 0)
    for i in range(N):
        bt.add(i, A[i])

    ans = []
    for i in range(Q):
        t, x, y = map(int, input().split())
        if t == 1:
            x -= 1
            bt.add(x, y)
        else:
            x -= 1
            y -= 1
            ans.append(bt.sum(y) ^ (bt.sum(x-1) if x > 0 else 0))
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
