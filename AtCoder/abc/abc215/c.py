from itertools import permutations
S, K = map(str, input().split())
S = permutations(list(S), len(S))
S = set(S)
A = []
for item in list(S):
    y = ""
    for w in item:
        y += w
    A.append(y)
A = sorted(A)
# print(S)
K = int(K)
print(A[K-1])
gcd(m, n):
m, n = max(m, n), min(m, n)
r = m % n
return gcd(n, r) if r else n
