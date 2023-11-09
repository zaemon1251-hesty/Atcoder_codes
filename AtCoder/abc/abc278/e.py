import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    H, W, N, h, w = mi()
    A = [li() for _ in range(H)]
    Colors = [0] * N

    # 二次元累積和
    S = [[[0] * N for _ in range(W + 1)] for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            Colors[A[i][j] - 1] += 1
            for k in range(N):
                S[i + 1][j + 1][k] += S[i + 1][j][k] + S[i][j + 1][k] - S[i][j][k] + (A[i][j] - 1 == k)

    ans = [[0] * (W - w + 1) for _ in range(H - h + 1)]

    for i in range(H - h + 1):
        for j in range(W - w + 1):
            res = 0
            for k in range(N):
                res += (S[i + h][j + w][k] - S[i][j + w][k] - S[i + h][j][k] + S[i][j][k]) != Colors[k]
            ans[i][j] = res

    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()
