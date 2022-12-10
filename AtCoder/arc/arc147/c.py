def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    L = sorted([S[i][0] for i in range(N)], reverse=True)
    R = sorted([S[i][1] for i in range(N)])
    ans = 0
    for i in range(N):
        ans += max(L[i] - R[i], 0) * (N - 2 * i - 1)
    print(ans)


if __name__ == '__main__':
    main()
