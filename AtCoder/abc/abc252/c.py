inf = 1 << 60


def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]
    ans = inf
    for s in range(10):
        s = str(s)
        t = 0
        times = [0] * 10
        for i in range(N):
            j = S[i].index(s)
            times[j] += 1
        mt = max(times)
        w = 9
        for i in range(9, -1, -1):
            if mt == times[i]:
                w = i
                break
        ans = min(ans, 10 * (mt - 1) + w)
    print(ans)


if __name__ == "__main__":
    main()
