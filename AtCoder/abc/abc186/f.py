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
    H, W, M = map(int, input().split())
    A = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
    ans = 0
    lowest_w = [H]*W
    lowest_h = [W]*H
    bt = BIT(W+1, lambda x,y: x + y, 0)
    A.sort(key=lambda x:(x[0], x[1]), reverse=True)
    for h,w in A:
        lowest_w[w] = min(lowest_w[w], h)
        lowest_h[h] = min(lowest_h[h], w)
    
    # 横→縦
    flg = False
    for w in range(W):
        if lowest_w[w] == 0:
            flg = True
            break
        ans += lowest_w[w]
    
    # 上記の操作で到達しなかった列のマスは、次の行以降カウントする
    if flg:
        for rest_w in range(w, W):
            bt.add(rest_w, 1)

    # 縦→横
    for h in range(H):
        if lowest_h[h] == 0:
            break
        while A and A[-1][0] < h:
            w = A[-1][1]
            # w列が既にブロックの後ろならスルー
            if w > 0 and bt.sum(w) == bt.sum(w-1) or (w == 0 and bt.sum(w)==0):
                bt.add(w, 1)
            A.pop()
        ans += bt.sum(lowest_h[h]-1)

    print(ans)


if __name__ == '__main__':
    main()