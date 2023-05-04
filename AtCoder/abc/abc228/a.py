<<<<<<< HEAD
s, t, x = map(int, input().split())
if t < s:
    t += 24
for i in range(s, t):
    if x % 24 == i % 24:
        print("Yes")
        exit()
print("No")
=======
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
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
