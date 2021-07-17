class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())



def maina():
    a,b = map(int, input().split())
    print(b-a+1)


def mainb():
    N = map(int, input().split())
    S = list(input())
    print("Takahashi" if S.index(1) % 2 == 0 else "Aoki")


def mainc():
    from collections import defaultdict
    mod = 10**9 + 7
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    dic = defaultdict(int)
    ans = 0
    for i in range(K):
        if dic[i] ==0:
            ans += 1
        dic[i] += 1
    ma = ans
    for i in range(K, N):
        dic[i - K] -= 1
        if dic[i - K] == 0:
            ans -= 1

        if dic[i] == 0:
            ans += 1
        dic[i] += 1

        ma = max(ma, ans)
    print(ma)

def maind():
    inf = 1<<60
    H, W, C = map(int, input().split())
    G = []
    dp = [[inf]*W for _ in range(H)]
    X = [[inf]*W for _ in range(H)]

    for _ in range(H):
        w = list(map(int,input().split()))
        G.append(w)

    ans = inf
    for i in range(H):
        for j in range(W):
            if i == 0  and j == 0:
                dp[i][j] = G[i][j]
                X[i][j] = inf
            elif i == 0:
                dp[i][j] = min(dp[i][j-1] + C, G[i][j])
                X[i][j] = min(dp[i][j-1] + C + G[i][j], X[i][j])
            elif j == 0:
                dp[i][j] = min(dp[i-1][j] + C, G[i][j])
                X[i][j] = min(dp[i-1][j] + C + G[i][j], X[i][j])
            else:
                dp[i][j] = min(dp[i-1][j] + C, dp[i][j-1] + C, G[i][j])
                X[i][j] = min(dp[i][j-1] + C + G[i][j],  dp[i-1][j] + C + G[i][j], X[i][j])

    print(X[-1][-1])

def maine():
    from math import gcd
    N, M = map(int, input().split())
    D = []
    for i in range(M):
        a,c = map(int, input().split())
        D.append((a,c))
    D.sort(key = lambda x:x[1])

    ans = 0
    X = N
    #sdgs = N
    for i in range(M):
        a, c = D[i][0], D[i][1]
        tmp = gcd(X, a)
        ans += c * (X - tmp)
        X = tmp

    print(ans if X == 1 else -1)


if __name__ =="__main__":
    mori = 20
    #maina()
    #mainb()
    #mainc()
    maind()
    #maine()