# 区間最小値を求める
# ABC-185-Fの改題


#####segfunc#####
def segfunc(x, y):
    return min(x, y)
#################


#####ide_ele#####
ide_ele = float('inf')
#################


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    find_rightest(a, b, x): [a,b)区間のx以下となる一番右のインデックスを取り出す O(logN)
    find_leftest(a, b, x): [a,b)区間のx以下となる一番左のインデックスを取り出す O(logN)
    get region(i): iを含み、区間積が tree[num + i - 1] となる区間 [l, r) を取り出す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.n = n
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

    def find_rightest(self, a, b, x):
        """
        [a,b)区間のx以下となる一番右のインデックスを取り出す
        """
        return self.find_rightest_sub(a, b, x, 0, 0, self.n)

    def find_leftest(self, a, b, x):
        """
        [a,r)区間のx以下となる一番左のインデックスを取り出す
        """
        return self.find_leftest_sub(a, b, x, 0, 0, self.n)

    def find_rightest_sub(self, a, b, x, k, l, r):
        """
        find_ringtestのサブルーチン
        [参考サイト]
        https://algo-logic.info/segment-tree/
        """
        if self.tree[k] > x or r <= a or l >= b:
            return max(a - 1, 0)
        elif k >= self.num - 1:
            return k - self.n - 1
        else:
            vr = self.find_rightest_sub(a, b, x, 2 * k + 2, (l + r) // 2, r)
            if vr != a - 1:
                return vr
            else:
                return self.find_rightest_sub(
                    a, b, x, 2 * k + 1, l, (l + r) // 2)

    def find_leftest_sub(self, a, b, x, k, l, r):
        """
        find_leftestのサブルーチン
        [参考サイト]
        https://algo-logic.info/segment-tree/
        """
        if self.tree[k] > x or r <= a or l >= b:
            return min(b, self.n - 1)
        elif k >= self.num - 1:
            return k - self.n - 1
        else:
            vr = self.find_rightest_sub(a, b, x, 2 * k + 1, l, (r + l) // 2)
            if vr != b:
                return vr
            else:
                return self.find_rightest_sub(
                    a, b, x, 2 * k + 2, (l + r) // 2, r)

    def get_region(self, i):
        idx = i + self.num - 1
        return


def routine_1():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    tree = SegTree(a, segfunc, ide_ele)
    for _ in range(q):
        t, x, y = map(int, input().split())
        if t == 1:
            tree.update(x - 1, y)
        else:
            print(tree.query(x - 1, y))


def routine_2():
    n = int(input())
    a = list(map(int, input().split()))
    tree = SegTree(a, segfunc, ide_ele)
    for i in range(n):
        r = tree.find_rightest(i + 1, n, a[i])
        l = tree.find_leftest(0, i, a[i])
        print("r:%s, l:%s, ans:%s" % (r, l, r - l + 1))


if __name__ == "__main__":
    routine_2()
