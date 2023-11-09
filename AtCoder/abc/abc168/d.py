from collections import deque


N, M = map(int, input().split())
G = [[] for _ in range(N)]
ans = [-1] * N
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

todo = deque([0])
ans[0] = 0
while todo:
    p = todo.popleft()
    for to in G[p]:
        if ans[to] != -1:
            continue
        ans[to] = p + 1
        todo.append(to)

if any(i == -1 for i in ans):
    print("No")
else:
    print("Yes")
    print(*ans[1:], sep="\n")
