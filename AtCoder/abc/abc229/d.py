from itertools import accumulate

S = list(input())
S = [int(S[i] == ".") for i in range(len(S))]
N = len(S)
S = [0] + list(accumulate(S))
K = int(input())
ans = 0
r = 0
for l in range(N):
    while r < N and S[r + 1] - S[l] <= K:
        r += 1
    ans = max(ans, r - l)
print(ans)
d()
