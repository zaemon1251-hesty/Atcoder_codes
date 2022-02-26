cnt = dict()


class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1 << n, 1 << n)

    def append(self, v):  # v を追加（その時点で v はない前提）
        cnt[v] = 1 + cnt.get(v, 0)

        v += 1
        nd = self.root
        while True:
            if v == nd.value:
                # v がすでに存在する場合に何か処理が必要ならここに書く
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p & -p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p & -p)//2)
                        break

    def leftmost(self, nd):
        if nd.left:
            return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right:
            return self.rightmost(nd.right)
        return nd

    def find_l(self, v):  # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v:
            prev = nd.value
        while True:
            if v < nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return nd
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return nd

    def find_r(self, v):  # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v:
            prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return nd
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return nd

    @property
    def max(self):
        return self.find_l((1 << self.N)-1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd=None, prev=None):  # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        if not nd:
            nd = self.root
        if not prev:
            prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    #####
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    #####
                    return
        if (not nd.left) and (not nd.right):
            if not prev.left:
                prev.right = None
            elif not prev.right:
                prev.left = None
            else:
                if nd.pivot == prev.left.pivot:
                    prev.left = None
                else:
                    prev.right = None

        elif nd.right:
            # print("type A", v)
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)
        else:
            # print("type B", v)
            nd.value = self.rightmost(nd.left).value
            self.delete(nd.value - 1, nd.left, nd)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None

    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.pivot - 1, nd_.left.value - 1 if nd_.left else -1, nd_.right.value - 1 if nd_.right else -1)

        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value:
                re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re
        print("Debug - root =", self.root.value -
              1, debug_node(self.root)[:50])

    def debug_list(self):
        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value:
                re.append(nd.value - 1)
            if nd.right:
                re += debug_node(nd.right)
            return re
        return debug_node(self.root)[:-1]


def main():
    Q = int(input())
    bt = BalancingTree(63)
    db = []
    q = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    for t in q:
        if t[0] == 1:
            x = t[1]
            bt.append(x)
        else:
            v, k = t[1], t[2]
            k -= 1
            if t[0] == 2:
                bt.debug()
                nd = bt.find_l(v)
                db.append(["%s's left" % v, nd.value-1,
                          nd.left.value-1 if nd.left else -1])
                cr = 1
                while nd.left != None and k > 0:
                    k -= 1
                    if cr < cnt[nd.value-1]:
                        cr += 1
                    else:
                        nd = nd.left
                        cr = 1
                if k != 0:
                    ans.append(-1)
                else:
                    ans.append(nd.value-1)
            if t[0] == 3:
                bt.debug()
                nd = bt.find_r(v)
                db.append(["%s's right" % v, nd.value-1,
                          nd.right.value-1 if nd.right else -1])
                cr = 1
                while nd.right != None and k > 0:
                    k -= 1
                    if cr < cnt[nd.value-1]:
                        cr += 1
                    else:
                        nd = nd.right
                        cr = 1
                if k != 0:
                    ans.append(-1)
                else:
                    ans.append(nd.value-1)
    print(*ans, sep="\n")
    print(*db, sep="\n")


if __name__ == '__main__':
    main()
