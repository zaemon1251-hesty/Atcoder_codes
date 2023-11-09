N = int(input())
C = [tuple(map(int, input().split())) for _ in range(N)]
p, m = [], []
for i in range(N):
    p.append(C[i][0] + C[i][1])
    m.append(C[i][0] - C[i][1])
print(max(max(p) - min(p), max(m) - min(m)))
