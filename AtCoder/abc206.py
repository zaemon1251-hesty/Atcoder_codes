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
    n = int(input())
    if int(n*1.08)<206:
        print("Yay!")
    elif int(n*1.08)==206:
        print('so-so')
    else:
        print(":(")
    print()


def mainb():
    N = int(input())
    ans=0
    i=0
    while True:
        if ans >= N:
            print(i)
            exit()
        i += 1
        ans += i

def mainc():
    from collections import defaultdict
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for i in range(N):
        d[A[i]] += 1
    ans = 0
    for k,v in d.items():
        ans += v * (v - 1) // 2
    print(ans)


def maind():
    from collections import Counter
    N = int(input())
    A = list(map(int, input().split()))
    uf = UnionFind(max(A) + 1)
    for i in range(N // 2):
        if A[i] != A[- 1 - i]:
            uf.union(A[i], A[- 1 - i])
    roots = uf.roots()
    ans = 0
    for p in roots:
        ans += uf.size(p) - 1
    print(ans)
    #print(roots)


def maine():
    L, R = map(int, input().split())
    A = [0] * (R + 1)
    for i in range(2, R + 1)[::-1]:
        if A[i]:continue
        k = R // i - (L - 1) // i
        A[i] = k * (k - 1) // 2

        for p in range(2 * i, R + 1, i):
            A[i] -= A[p]

    ans = sum(A)
    x = 0
    for g in range(max(2, L), R + 1)[::-1]:
        x += max(R // g - 1, 0)

    ans -= x
    ans *= 2
    print(ans)

if __name__ =="__main__":
    mori = 20
    #maina()
    #mainb()
    #mainc()
    #maind()
    maine()