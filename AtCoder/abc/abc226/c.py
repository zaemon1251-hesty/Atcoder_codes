from heapq import heappush, heappop
from collections import deque

inf = 1 << 60
N = int(input())
G = [[] for _ in range(N)]
E = [0] * N
ans = 0
got = [False] * N
for i in range(N):
    A = list(map(int, input().split()))
    l = A[0]
    E[i] = l
    if A[1] != 0:
        for j in range(2, len(A)):
            A[j] -= 1
            G[i].append(A[j])
r = N - 1
todo = [r]
short = [0] * N
short[r] = E[r]
while todo:
    dd = heappop(todo)
    flg = True
    ans += E[dd]
    for to in G[dd]:
        if not got[to]:
            heappush(todo, to)
            got[to] = True
print(ans)
