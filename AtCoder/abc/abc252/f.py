import heapq


n, l = map(int, input().split())
a = list(map(int, input().split()))
b = l - sum(a)
if b:
    a.append(b)
heapq.heapify(a)

ans = 0
while len(a) > 1:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    ans += x + y
    heapq.heappush(a, x + y)
print(ans)
