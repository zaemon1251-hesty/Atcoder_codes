def main():
    MOD = 998244353
    L = list(map(int, input()))[::-1]
    s = sum(L)
    p = pow(2, len(L) - 1, MOD)
    inv2 = pow(2, MOD - 2, MOD)
    ans = 0
    for n in L:
        s -= n
        ans += (n + s * inv2) * p
        ans %= MOD
        p *= 5
        p %= MOD
    print(ans)


if __name__ == "__main__":
    main()
