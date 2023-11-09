def main():
    MOD = 998244353
    N, L = map(int, input().split())
    S = [list(input()) for _ in range(N)]
    ans = 0

    # 包除原理
    for i in range(1, 1 << N):
        used = [0] * 26
        for j in range(N):
            if i >> j & 1:
                ws = S[j]
                for w in ws:
                    used[ord(w) - ord("a")] += 1
        lenght = bin(i).count("1")
        ans += pow(sum(u == lenght for u in used), L, MOD) * (-1) ** (lenght - 1)
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
