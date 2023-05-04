import sys
sys.setrecursionlimit(10**7)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
<<<<<<< HEAD
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
=======
for _ in range(N-1):
    a,b = map(int,input().split())
    a,b = a-1,b-1
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
    G[a].append(b)
    G[b].append(a)
# Euler Tour Technique
S = []
<<<<<<< HEAD
FS = [0] * N
depth = [0] * N


=======
FS = [0]*N
depth = [0]*N
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
def dfs(v, p, d):
    depth[v] = d
    FS[v] = len(S)
    S.append(v)
    for w in G[v]:
        if w == p:
            continue
<<<<<<< HEAD
        dfs(w, v, d + 1)
        S.append(v)


dfs(0, -1, 0)
# Sparse Table
L = len(S)
lg = [0] * (L + 1)
for i in range(2, L + 1):
    lg[i] = lg[i >> 1] + 1
st = [None] * (lg[L] + 1)
st0 = st[0] = S
b = 1
for i in range(lg[L]):
    st0 = st[i + 1] = [p if depth[p] <= depth[q]
                       else q for p, q in zip(st0, st0[b:])]
    b <<= 1


def query(u, v):
    # LCA O(1)

    x = FS[u]
    y = FS[v]
    if x > y:
        x, y = y, x
    l = lg[y - x + 1]
    px = st[l][x]
    py = st[l][y - (1 << l) + 1]
    return px if depth[px] <= depth[py] else py


q = [list(map(int, input().split())) for _ in range(Q)]
for x, y in q:
    x, y = x - 1, y - 1
    z = query(x, y)
=======
        dfs(w, v, d+1)
        S.append(v)
dfs(0, -1, 0)
# Sparse Table
L = len(S)
lg = [0]*(L + 1)
for i in range(2, L+1):
    lg[i] = lg[i >> 1] + 1
st = [None]*(lg[L] + 1)
st0 = st[0] = S
b = 1
for i in range(lg[L]):
    st0 = st[i+1] = [p if depth[p] <= depth[q] else q for p, q in zip(st0, st0[b:])]
    b <<= 1
# LCA O(1)
def query(u, v):
    x = FS[u]; y = FS[v]
    if x > y:
        x, y = y, x
    l = lg[y - x + 1]
    px = st[l][x]; py = st[l][y - (1 << l) + 1]
    return px if depth[px] <= depth[py] else py
q = [list(map(int,input().split())) for _ in range(Q)]
for x,y in q:
    x,y = x-1,y-1
    z = query(x,y)
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
    if (depth[x] - depth[z]) % 2 == (depth[y] - depth[z]) % 2:
        print("Town")
    else:
        print("Road")
