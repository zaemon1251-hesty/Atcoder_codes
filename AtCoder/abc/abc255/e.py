from collections import defaultdict


def main():
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    X = list(map(int, input().split()))
    res = defaultdict(int)
    for i in range(N - 2):
        S[i + 1] -= S[i]

    for x in X:
        res[x] += 1

    flg = -1
    for i in range(N - 1):
        for k in range(M):
            res[(X[k] - S[i]) * flg] += 1
        flg *= -1
    print(max(res.values()))


if __name__ == "__main__":
    main()
