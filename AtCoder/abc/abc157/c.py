N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(M)]
for i in range(1000):
    w = str(i)
    if len(w) == N and all(w[s - 1] == str(c) for s, c in S):
        print(w)
        return
print(-1)
