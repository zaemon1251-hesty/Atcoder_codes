def maine():
    mod = 10 ** 9 + 7
    N, K = map(int, input().split())
    A = [0] * (K+1)
    for i in range(2, K + 1)[::-1]:
        if A[i]:continue
        A[i] = pow(K // i, N, mod)

        for p in range(2 * i, K + 1, i):
            A[i] -= A[p]

        A[i] %= mod
    ans = 0
    ans += pow(K, N, mod) - sum(A)
    ans %= mod
    for i in range(2, K + 1):
        ans += A[i] * i
        ans %= mod
    print(ans)
    #print(A)

if __name__ == "__main__":
    maine()