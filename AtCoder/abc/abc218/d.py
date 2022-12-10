from collections import defaultdict
N = int(input())
S = defaultdict(set)
for i in range(N):
    x, y = map(int, input().split())
    S[x].add(y)
X = S.keys()
ans = 0
for x1 in X:
    for x2 in X:
        if x1 == x2:
            continue
        tmp = len(S[x1] & S[x2])
        ans += tmp * (tmp - 1) // 2
print(ans // 2)
