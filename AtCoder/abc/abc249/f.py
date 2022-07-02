from heapq import heappop, heappush


class Kth_PQ:
    """
    小さい方からK個の合計を返すPQ。popはできない
    Kは広義単調減少である必要がある
    """

    def __init__(self):
        self.q = []
        self._sum = 0

    def push(self, x):
        heappush(self.q, -x)
        self._sum += x

    def sum(self, k):
        while len(self.q) > k:
            x = -heappop(self.q)
            self._sum -= x
        return self._sum


def main():
    N, K = map(int, input().split())
    Q = [[1, 0]] + [[*map(int, input().split())] for _ in range(N)]

    q = Kth_PQ()
    n_set = 0
    ysum = 0
    ans = -10**20
    while Q:
        t, y = Q.pop()
        if t == 1:
            if K - n_set >= 0:
                s = q.sum(K - n_set)
            else:
                break
            ans = max(ans, y + ysum - s)
            n_set += 1
        else:
            ysum += y
            if y < 0:
                q.push(y)

    print(ans)


if __name__ == '__main__':
    main()
