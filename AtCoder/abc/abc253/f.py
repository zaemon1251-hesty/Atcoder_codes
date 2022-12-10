class BIT:
    """
    <Attention> 0-indexed.
    query ... return the sum [0 to m]
    sum ... return the sum [a to b]
    sumall ... return the sum [all]
    add ... 'add' number to element (be careful that it doesn't set a value.)
    search ... the sum version of bisect.right
    output ... return the n-th element
    listout ... return the BIT list
    """

    def query(self, m):
        res = 0
        while m > 0:
            res += self.bit[m]
            m -= m & (-m)
        return res

    def sum(self, a, b):
        return self.query(b) - self.query(a)

    def sumall(self):
        bitlen = self.bitlen - 1
        return self.query(bitlen)

    def add(self, m, x):
        m += 1
        bitlen = len(self.bit)
        while m <= bitlen - 1:
            self.bit[m] += x
            m += m & (-m)
        return

    def search(self, a):
        tmpsum = 0
        i = 0
        k = (self.bitlen - 1).bit_length()
        while k >= 0:
            tmpk = 2**k
            if i + tmpk <= self.bitlen - 1:
                if tmpsum + self.bit[i + tmpk] < a:
                    tmpsum += self.bit[i + tmpk]
                    i += tmpk
            k = k - 1
        return i + 1

    def output(self, a):
        return self.query(a + 1) - self.query(a)

    def listout(self):
        return self.bit

    def __init__(self, a):
        self.bitlen = a
        self.bit = [0] * a


n, m, Q = map(int, input().split())
bit = BIT(m + 3)
q = [list(map(int, input().split())) for i in range(Q)]

cnt = 0
for i in range(Q):
    if q[i][0] == 3:
        cnt += 1

ans = [0] * cnt
waiting = [[] for i in range(n + 3)]

for i in range(Q - 1, -1, -1):
    if q[i][0] == 1:
        bit.add(q[i][1], q[i][3])
        bit.add(q[i][2] + 1, -q[i][3])
    elif q[i][0] == 3:
        cnt -= 1
        ans[cnt] -= bit.query(q[i][2] + 1)
        waiting[q[i][1]].append((cnt, q[i][2]))
    else:
        for j in waiting[q[i][1]]:
            ans[j[0]] += bit.query(j[1] + 1) + q[i][2]
        waiting[q[i][1]] = []

for i in range(n + 3):
    for j in waiting[i]:
        ans[j[0]] += bit.query(j[1] + 1)

print(*ans, sep="\n")
