inf = 1 << 60


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = inf
    for i in range(1 << (N - 1)):
        res = 0
        tmp = A[0]
        for j in range(N - 1):
            if (i >> j) & 1:
                res ^= tmp
                tmp = 0
            tmp |= A[j + 1]
        if tmp > 0:
            res ^= tmp
        ans = min(ans, res)

    print(ans)


if __name__ == "__main__":
    main()
