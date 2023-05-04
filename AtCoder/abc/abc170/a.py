<<<<<<< HEAD
X = list(map(int, input().split()))
print(X.index(0) + 1)
=======
import sys
from MultSet import HeapDict
sys.path.append('../')
from Segtree import SegTree
def segfunc(x, y): return min(x, y)
ide_ele = float('inf')
order = [ide_ele]*(1 << 18)
st = SegTree(order, segfunc, ide_ele)
N, Q = map(int, input().split())
kinds = [HeapDict() for _ in range(2*10**5)]
rate = [0]*N
whereBaby = [0]*N
for i in range(N):
    a, b = map(int, input().split())
    b -= 1
    rate[i] = a
    whereBaby[i] = b
    kinds[b].insert(-a)
    st.update(b, -kinds[b].get_min())
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    prek = whereBaby[c]
    whereBaby[c] = d
    kinds[prek].erase(-rate[c])
    kinds[d].insert(-rate[c])
    st.update(prek, -kinds[prek].get_min(t=-ide_ele))
    st.update(d, -kinds[d].get_min())
    ans = st.query(0, 2*10**5)
    print(ans)
e()
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
