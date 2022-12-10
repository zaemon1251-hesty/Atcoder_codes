inf = 1 << 60


def main():
    N, K = map(int, input().split())
    S = map(lambda s: ord(s) - ord("a"), list(input()))
    S = list(S)
    p = []
    for i in range(1, N - 1):
        if N % i == 0:
            p.append(i)

    ans = N
    for i in p:
        s = [[0] * 26 for _ in range(i)]

        for j in range(N):
            s[j % i][S[j]] += 1

        rest = 0
        for d in s:
            t = N // i - max(d)
            rest += t
        if rest <= K:
            ans = min(ans, i)

    print(ans)


if __name__ == '__main__':
    main()
