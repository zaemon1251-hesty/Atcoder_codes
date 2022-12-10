import heapq
from collections import defaultdict
import sys


def input():
    return sys.stdin.readline().rstrip()


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
            return
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

    def get_min(self):
        return self.h[0]


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    A = sorted(set(li()))
    residual = N - len(A)
    hd = HeapDict()
    for a in A:
        hd.insert(-a)

    for i in range(1, N + 1):
        if not hd.h and residual == 0:
            i -= 1
            break

        if hd.is_exist(-i):
            hd.erase(-i)
        elif residual >= 2:
            residual -= 2
        else:
            cnt = residual
            while hd.h and cnt < 2:
                hd.erase(hd.get_min())
                cnt += 1
            if cnt != 2:
                i -= 1
                break
            residual = 0
    print(i)


if __name__ == '__main__':
    main()
