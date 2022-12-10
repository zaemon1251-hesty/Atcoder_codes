import sys
import heapq
from collections import defaultdict


class HeapDict:

    """
    O(logn)で要素の挿入
    O(logn)で要素の削除
    O(1)で要素の存在確認
    O(1)で最小値の取得
    """

    def __init__(self):
        """
        h : 最小値を保持すするヒープ
        d : (値:重複個数) の連想配列
        """
        self.h = []
        self.d = defaultdict(int)

    def insert(self, x):
        heapq.heappush(self.h, x)
        self.d[x] += 1

    def erase(self, x):
        if not self.is_exist(x):
            raise RuntimeError(f"{x} not in Dict.")
        self.d[x] -= 1
        # 最小値を更新
        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self, x):
        if x in self.d and self.d[x] != 0:
            return True
        else:
            return False

    def get_min(self, default=None):
        if len(self.h):
            return self.h[0]
        else:
            return default


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, Q = mi()
    events = []
    for _ in range(N):
        s, t, x = mi()
        events.append((s - x, 1, x))
        events.append((t - x, -1, x))
    D = [ii() for _ in range(Q)]
    heapq.heapify(D)
    obs = HeapDict()
    events.sort(key=lambda x: (x[0], -x[1]), reverse=True)

    while D:
        d = heapq.heappop(D)
        while events and events[-1][0] <= d:
            _, q, loc = events.pop()
            if q == 1:
                obs.insert(loc)
            else:
                obs.erase(loc)
        loc = obs.get_min()
        print(loc if loc is not None else -1)


if __name__ == '__main__':
    main()
