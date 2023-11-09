class Hash:
    def __init__(self, st, base, mod):
        self.mod = mod

        N = len(st)
        self.pw = pw = [1] * (N + 1)
        self.h = h = [0] * (N + 1)

        for i in range(1, N + 1):
            pw[i] = (pw[i - 1] * base) % mod

        for i in range(1, N + 1):
            h[i] = base * h[i - 1] + (ord(st[i - 1]) - 96)
            h[i] %= mod

    # 文字列のl文字目からr文字目までの部分文字列のハッシュ値を戻す。
    def get_hash(self, l, r):
        return (self.h[r] - (self.pw[r - l + 1] * self.h[l - 1])) % self.mod


# base = 100, mod = 2147483647


N = int(input())
X = input()
Y = X[::-1]
S = Hash(X, 100, 2147483647)
T = Hash(Y, 100, 2147483647)

for i in range(1, N + 1):
    if S.get_hash(1, i) == T.get_hash(N - i + 1, N) and S.get_hash(i + N + 1, 2 * N) == T.get_hash(N + 1, 2 * N - i):
        print(X[:i] + X[i + N :])
        print(i)
        exit()

print(-1)
