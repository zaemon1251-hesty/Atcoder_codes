N = int(input())
C = list(input())
cntR = [0] * N
inf = 10**9
for i in range(N):
    cntR[i] += 1 if C[i] == "R" else 0
    cntR[i] += cntR[i - 1]
nR = cntR[-1]
ans = inf
cntR = [0] + cntR
for i in range(nR + 1):
    ans = min(ans, nR - cntR[i])
print(ans)
