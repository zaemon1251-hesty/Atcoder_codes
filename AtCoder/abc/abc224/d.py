from collections import deque

inf = 1 << 60
M = int(input())
G = [[] for _ in range(9)]
for _ in range(M):
    x, y = map(lambda x: int(x) - 1, input().split())
    G[x].append(y)
    G[y].append(x)
ans = dict()
p = list(map(lambda x: int(x) - 1, input().split()))
t = ["8"] * 9
for i in range(8):
    t[p[i]] = str(i)
t = "".join(t)
todo = deque([t])
ans[t] = 0
while todo:
    p = todo.popleft()
    w = p
    p = list(p)
    movable = p.index("8")
    for i in G[movable]:
        j = movable
        s = p.copy()
        s[i], s[j] = s[j], s[i]
        s = "".join(s)
        if s in ans:
            continue
        ans[s] = ans[w] + 1
        todo.append(s)
print(ans["012345678"] if "012345678" in ans else -1)
