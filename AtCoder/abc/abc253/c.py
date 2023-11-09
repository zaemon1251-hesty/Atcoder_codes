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
            return
        self.d[x] -= 1
        # 最小値を更新
        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self, x):
        if x not in self.d or self.d[x] != 0:
            return True
        else:
            return False

    def get_min(self, default=0):
        if len(self.h):
            return self.h[0]
        else:
            return default


def main():
    Q = int(input())
    q = [list(map(str, input().split())) for _ in range(Q)]
    mins = HeapDict()
    maxs = HeapDict()
    outputs = []
    for k in q:
        if k[0] == "1":
            _, x = k
            x = int(x)
            mins.insert(x)
            maxs.insert(-x)
        elif k[0] == "2":
            _, x, c = k
            x, c = int(x), int(c)
            for _ in range(min(c, mins.d[x])):
                mins.erase(x)
                maxs.erase(-x)
        elif k[0] == "3":
            outputs.append(-maxs.get_min() - mins.get_min())

    print(*outputs, sep="\n")


if __name__ == "__main__":
    main()
