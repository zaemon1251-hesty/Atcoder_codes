#最適二分探索木
#配列の順番を崩さずに2分探索木の期待値？の最小化をする

def optcost(A):
    N = len(A)
    dp = [[0]*N for _ in range(N)]
    from itertools import accumulate
    F = [0] + list(accumulate(A))

    for width in range(1, N):

        for i in range(N - width):
            Acc = F[i + width + 1] - F[i]
            div = float("inf")

            for k in range(i, i + width):
                div = min(div, dp[i][k] + dp[k + 1][i + width])

            dp[i][i + width] = div + Acc

    return dp[0][-1]

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(optcost(A))