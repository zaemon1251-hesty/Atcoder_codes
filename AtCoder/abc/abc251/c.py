inf = 1 << 60


def main():
    N = int(input())
    A = [list(map(str, input().split())) for _ in range(N)]
    origins = set()
    max_ = -inf
    ans = -1
    for i in range(N):
        a, t = A[i]
        t = int(t)
        if a in origins:
            continue
        if max_ < t:
            ans = i
            max_ = t
        origins.add(a)
    print(ans + 1)


if __name__ == "__main__":
    main()
