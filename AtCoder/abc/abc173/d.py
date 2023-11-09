from heapq import heappop, heappush

heap = []
ans = 0
N = int(input())
(*A,) = map(int, input().split())
A.sort(reverse=True)
B = []
B.append(A[0])
for i in range(1, N):
    B.append(A[i])
    B.append(A[i])
print(sum(B[: N - 1]))
