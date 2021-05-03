#ZONe プログラミングコンテスト　E
#最短経路問題はこの解法を基本にした方がよさそう
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix

R, C = map(int, input().split())
data = []
row = []
colomn = []
for i in range(R):
    a = list(map(int, input().split()))
    for j in range(C - 1):
        x = i * C + j
        y = i * C + j + 1
        row += [x, y]
        colomn += [y, x]
        data += [a[j], a[j]]
for i in range(R - 1):
    a = list(map(int, input().split()))
    for j in range(C):
        x = i * C + j
        y = i * C + j + C
        row += [x, y + R * C]
        colomn += [y, x + R * C]
        data += [a[j], 1]
for i in range(R):
    for j in range(C):
        x = i * C + j
        y = x + R * C
        row += [x, y]
        colomn += [y, x]
        data += [1, 0]
g = csr_matrix((data, (row, colomn)))
print(int(shortest_path(g, indices=0)[R * C - 1]))
