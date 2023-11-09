mod = 10**9 + 7
N, K = map(int, input().split())
A = [0] * (K + 1)
for i in range(2, K + 1)[::-1]:
    if A[i]:
        continue
    # 1~K のうちiの倍数 を N 個並べると、gcdは少なくともiの倍数になる
    A[i] = pow(K // i, N, mod)
    for p in range(2 * i, K + 1, i):
        # gcdが p (= i * k) となる場合の数を引く
        A[i] -= A[p]
    # A[i] は　gcdがちょうどiになる並べ方の数
    A[i] %= mod
# 全事象
ans = pow(K, N, mod)
# gcdが1になる並べ方の数を求める (sum(A) = A[2] + ... + A[K] を全事象から引くと、余事象としてgcdが1になる並べ方の数が求まる)
ans -= sum(A)
ans %= mod
for i in range(2, K + 1):
    ans += A[i] * i
    ans %= mod
print(ans)
