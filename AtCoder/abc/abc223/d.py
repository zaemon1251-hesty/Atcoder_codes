n, m = map(int, input().split())
N = [0] * n
A = [list() for _ in range(n)]
ans = []
for i in range(m):
    a, b = map(int, input().split())
    N[b - 1] += 1
    A[a - 1].append(b)
import heapq

q = [i + 1 for i in range(n) if N[i] == 0]
heapq.heapify(q)
while q != []:
    v = heapq.heappop(q)
    ans.append(v)
    for j in A[v - 1]:
        N[j - 1] -= 1
        if N[j - 1] == 0:
            heapq.heappush(q, j)
if N.count(0) == n:
    print(*ans)
else:
    print(-1)
