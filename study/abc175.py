N, K = map(int, input().split())
P = list(map(lambda x:int(x) - 1, input().split()))
C = list(map(int, input().split()))
ans = 0
seen = [False]*N
for i in range(N):
    if seen[i]:continue
    _max = -10**14
    loop = [0]*N
    src = i
    cnt = 0
    while cnt <= K and loop[P[src]] == 0:
        dst = P[src]
        loop[dst] += P[src] + C[dst]