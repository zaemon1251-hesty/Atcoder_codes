import bisect
N, K = map(int, input().split())
P = []
S = []
for i in range(N):
    t = sum(list(map(int, input().split())))
    P.append(t)
    S.append(t)
S.sort()
ans = []
for i in range(N):
    a = P[i]
    idx = N - bisect.bisect_left(S, a + 301)
    ans.append('Yes' if K > idx else 'No')
print(*ans, sep="\n")
