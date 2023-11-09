def main():
    N, L = map(int, input().split())
    t = 2 * 3 ** (L - 1) + N - 1
    s1m = {i: j for i, j in zip("012", "120")}
    s2m = {i: j for i, j in zip("012", "201")}
    s = []
    for i in range(N):
        tmp = t - i
        res = []
        for i in range(L):
            tmp, d = tmp // 3, tmp % 3
            res.append(d)
        s.append("".join(map(str, reversed(res))))
    s_ = list(map(lambda x: "".join(map(lambda w: s1m[w], x)), s))
    s__ = list(map(lambda x: "".join(map(lambda w: s2m[w], x)), s))

    ans = s + s_ + s__
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
