<<<<<<< HEAD
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
=======
mod = 998244353
N, K, M = map(int, input().split())
if M % mod == 0:
    print(0)
    exit()
S = pow(K, N, mod-1)
S %= mod - 1
ans = pow(M, S, mod)
print(ans)
_name__ == "__main__":
maine()
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
