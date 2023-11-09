N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())
a, b, c, d = max(1 - A, 1 - B), min(N - A, N - B), max(1 - A, B - N), min(N - A, B - 1)
G = [["0"] * (S - R + 1) for _ in range(Q - P + 1)]
for i in range(P, Q + 1):
    for j in range(R, S + 1):
        t = "."
        if (i - A == j - B and a <= i - A <= b) or (i - A == -(j - B) and c <= i - A <= d):
            t = "#"
        G[i - P][j - R] = t
for i in range(Q - P + 1):
    G[i] = "".join(G[i])
print(*G, sep="\n")
c()
