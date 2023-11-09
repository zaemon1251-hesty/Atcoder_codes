from math import inf, sqrt


def dist(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        res = inf
        for k in range(K):
            res = min(res, dist(S[i], S[A[k] - 1]))
        ans = max(ans, res)
    print(sqrt(ans))


if __name__ == "__main__":
    main()
