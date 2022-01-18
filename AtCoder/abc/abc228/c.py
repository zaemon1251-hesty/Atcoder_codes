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
