<<<<<<< HEAD
from heapq import heappop, heappush
from sys import stdin


def input():
    return stdin.readline().rstrip()


n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b, c, d = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((b, c, d))
    g[b].append((a, c, d))

infty = 10 ** 20


def get_dist(now, c, d):
    to = int(d ** .5) - 1
    return min(t - now + c + d // (t + 1)
               for t in [to, to + 1, now] if t >= now)


q = []
dist = [infty] * n
q.append((0, 0))
dist[0] = 0
while q:
    t, v = heappop(q)
    if dist[v] != t:
        continue
    for nv, c, d in g[v]:
        nd = get_dist(t, c, d)
        if dist[nv] > t + nd:
            dist[nv] = t + nd
            heappush(q, (t + nd, nv))
ans = dist[n - 1]
if ans == infty:
    ans = -1
print(ans)
=======
n, m = map(int, input().split())
x = []
for i in range(m):
    n1, k1 = map(int, input().split())
    x.append((n1, k1))
x = sorted(x, key = lambda x:(x[0], x[1]))
ans = set()
ans.add(n)
now = x[0][0]
black = set()
for i in range(m):
    xi, yi = x[i]
    if now == xi:
        black.add(yi)
        continue
    else:
        a = set()
        b = set()
        for Y in black:
            if ((Y - 1 in ans) or (Y + 1 in ans)) and (Y not in ans):
                a.add(Y)
            elif ((Y - 1 not in ans) and (Y + 1 not in ans)) and (Y in ans):
                b.add(Y)
        for j in a:ans.add(j)
        for j in b:ans.discard(j)
        now = xi
        black = set([yi])
a = set()
b = set()
for Y in black:
    if ((Y - 1 in ans) or (Y + 1 in ans)) and (Y not in ans):
        a.add(Y)
    elif ((Y - 1 not in ans) and (Y + 1 not in ans)) and (Y in ans):
        b.add(Y)
for j in a:ans.add(j)
for j in b:ans.discard(j)
print(len(ans))
_name__ == '__main__':
#maina()
#mainb()
#mainc()
maind()
#maine()
mori = True
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
