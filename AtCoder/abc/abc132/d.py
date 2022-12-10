def Partition(n):
    """
    n個の玉、n個の箱を区別しない、各箱に入る玉の個数に制限なし　P(n, n)
    つまり、n個の要素を何個かの整数の和として表す方法の数
    分割数の、漸化式を用いたO(n**(3/2))の実装
    """
    P = [0 for i in range(n + 1)]
    P[0] = 1
    for i in range(n + 1):
        j = 1
        while i - (j * j * 3 - j) / 2 >= 0:
            #print(i, i - (j * j * 3 - j)//2, i - (j * j * 3 + j)//2)
            if (j - 1) % 2 == 0:
                P[i] += P[i - (j * j * 3 - j) // 2]
                if (i - (j * j * 3 + j) // 2 >= 0):
                    P[i] += P[i - (j * j * 3 + j) // 2]
            else:
                P[i] -= P[i - (j * j * 3 - j) // 2]
                if (i - (j * j * 3 + j) // 2 >= 0):
                    P[i] -= P[i - (j * j * 3 + j) // 2]
            j += 1

    if n < 0:
        return 0
    else:
        return P[n]


class Partition2:
    def __init__(self, n, k_max) -> None:
        if n < 0 or k_max < 0:
            raise ValueError

        P = [[0 for i in range(k_max + 1)] for i in range(n + 1)]
        for i in range(k_max + 1):
            P[0][i] = 1
        for i in range(1, n + 1):
            for j in range(1, k_max + 1):
                P[i][j] = P[i][j - 1] + (P[i - j][j] if i >= j else 0)

        self.n = n
        self.k = k_max
        self.P = P

    def __call__(self, m, s) -> int:
        """分割数P(m,s)"""
        if not (0 <= m <= self.n and 0 <= s <= self.k):
            return 0
        else:
            return self.P[m][s]

    def partitionMinOne(self, m, s) -> int:
        """分割数P(m-s,s)"""
        return self.__call__(m, s)


def Partition2_s(n, k):
    """
    n個の玉、k個の箱を区別しない
    各箱に入る玉の個数に制限なし
    分割数の、漸化式を用いたO(nk)の実装
    """
    P = [[0 for i in range(k + 1)] for i in range(n + 1)]
    for i in range(k + 1):
        P[0][i] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            P[i][j] = P[i][j - 1] + (P[i - j][j] if i >= j else 0)
    if n < 0 or k < 0:
        return 0
    else:
        return P[n][k]


class ModCmb:
    """calc combinations on the conditions of a certain mod
    """

    def __init__(self, N, mod=10**9 + 7):
        # 二項係数テーブル
        fact = [1, 1]
        factinv = [1, 1]
        inv = [0, 1]
        for i in range(2, N + 1):
            fact.append((fact[-1] * i) % mod)
            inv.append((mod - inv[mod % i] * (mod // i)) % mod)
            factinv.append((factinv[i - 1] * inv[-1]) % mod)

        # 初期化
        self.MOD = mod
        self.N = N
        self.fact = fact
        self.factinv = factinv
        self.inv = inv

    def cmb(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.fact[n] * \
            (self.factinv[k] * self.factinv[n - k] % self.MOD) % self.MOD


def main():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N, K = mi()
    MOD = 10**9 + 7
    md = ModCmb(N, mod=MOD)
    for i in range(1, K + 1):
        res = 0
        res += md.cmb(K - 1, i - 1) * md.cmb(N - K + 1, i)
        res %= MOD
        print(res)


if __name__ == '__main__':
    main()
