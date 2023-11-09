from collections import deque

N, M = map(int, input().split())
C = [[] for _ in range(N)]
block = [0] * M
for i in range(M):
    k = int(input())
    balls = list(map(int, input().split()))
    for j in range(k):
        C[balls[j] - 1].append([i, j])
C.sort(key=lambda Z: max(Z[0][1], Z[1][1]), reverse=True)
height = 0
rest = None
while C:
    x, y = C.pop()
    if rest:
        C.append(rest)
    if max(x[1], y[1]) > height:
        print("No")
        exit()
    if x[1] - block[x[0]] == y[1] - block[y[0]] == 0:
        rest = None
        block[x[0]] += 1
        block[y[0]] += 1
        height += 1
    else:
        rest = [x, y]
else:
    print("Yes")
