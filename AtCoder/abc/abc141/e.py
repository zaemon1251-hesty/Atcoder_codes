from itertools import combinations
from collections import defaultdict


class RollingHash():
    """get substring hash
    """
    mod = 10**9 + 7
    base = 1007

    mod_sub = 998244353
    base_sub = 2009

    def __init__(self, s):
        self.pw = pw = [1] * (len(s) + 1)
        self.pw_sub = pw_sub = [1] * (len(s) + 1)

        l = len(s)
        self.h = h = [0] * (l + 1)
        self.h_sub = h_sub = [0] * (l + 1)

        v = 0
        v_sub = 0
        for i in range(l):
            h[i + 1] = v = (v * self.base + ord(s[i])) % self.mod
            h_sub[i + 1] = v_sub = (v_sub * self.base_sub +
                                    ord(s[i])) % self.mod_sub
        v = 1
        v_sub = 1
        for i in range(l):
            pw[i + 1] = v = v * self.base % self.mod
            pw_sub[i + 1] = v_sub = v_sub * self.base_sub % self.mod_sub

    def get(self, l, r):
        """get s[l:r] hash value

        Args:
            l (int): left index
            r (int): right index

        Returns:
            Tuple[int]: redundantized hash value
        """
        hs = (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod
        hs_sub = (self.h_sub[r] - self.h_sub[l] *
                  self.pw_sub[r - l]) % self.mod_sub
        return hs, hs_sub


def main():
    N = int(input())
    S = input()
    rh = RollingHash(S)

    def check(length):
        his = {}
        for i in range(N - length + 1):
            pair = rh.get(i, i + length)
            # 最初に見つけたpairを保持して、 index が length 以上離れているか を判定する
            if pair in his:
                if i - his[pair] >= length:
                    return True
            else:
                his[pair] = i
        return False

    ok, ng = 0, N // 2 + 1
    while ng - ok > 1:
        cen = (ok + ng) // 2
        if check(cen):
            ok = cen
        else:
            ng = cen

    print(ok)


if __name__ == '__main__':
    main()
