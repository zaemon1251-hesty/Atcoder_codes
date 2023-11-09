from heapq import heappush, heappop
from collections import deque

Q = int(input())
A = deque([])
heap = []
ANS = []
for _ in range(Q):
    tmp = input()
    if tmp[0] == "1":
        x = int(tmp[2])
        A.append(x)
    elif tmp[0] == "2":
        if len(heap) > 0:
            z = heappop(heap)
        else:
            z = A.popleft()
        ANS.append(z)
    else:
        for i in A:
            heappush(heap, i)
        A = deque([])
print(*ANS, sep="\n")
e()
