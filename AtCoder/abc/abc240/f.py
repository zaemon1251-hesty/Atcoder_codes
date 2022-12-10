inf = 1 << 60


def main():
    ans = []
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())

        X, Y = [], []
        for _ in range(N):
            x, y = map(int, input().split())
            X.append(x)
            Y.append(y)

        a = 0
        b = 0
        res = X[0]
        for x, y in zip(X, Y):
            if x != 0 and b > 0 and b + x * y < 0:
                ny = b // -x
                st = b + x
                en = b + x * ny
                tmpa = a + (st + en) * ny // 2
                res = max(tmpa, res)
            st = b + x
            en = b + x * y
            a = a + (st + en) * y // 2
            b = en
        res = max(a, res)
        ans.append(res)
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
